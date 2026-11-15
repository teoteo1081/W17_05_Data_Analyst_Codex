from pathlib import Path
import json,sys,subprocess,socket,time,urllib.request,tempfile,math,shutil
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
WIDTHS=[320,375,390,768,1024,1440]
LOCALES=['vi','en','es','zh']
RESULTS=[]
def record(name,ok,detail=''):
 RESULTS.append({'name':name,'status':'PASS' if ok else 'FAIL','detail':detail})
 print(('PASS ' if ok else 'FAIL ')+name+(' '+detail if not ok else ''),flush=True)
def main():
 out=ROOT/'docs/verification';out.mkdir(parents=True,exist_ok=True)
 model=json.loads((ROOT/'profile.json').read_text(encoding='utf-8'))
 ui=json.loads((ROOT/'assets/site_ui.json').read_text(encoding='utf-8'))
 record('four complete locales / three scoped offers',set(model['locales'])==set(LOCALES) and all(len(v['services'])==3 for v in model['locales'].values()) and all(set(ui[l])==set(ui['vi']) for l in LOCALES))
 html=(ROOT/'index.html').read_text(encoding='utf-8');js=(ROOT/'assets/app.js').read_text(encoding='utf-8');css=(ROOT/'assets/style.css').read_text(encoding='utf-8')
 record('safe structured rendering / no empty anchors / no overflow masking','innerHTML' not in js and 'href="#"' not in html and 'overflow-x:hidden' not in css.replace(' ','') and 'overflow-x: hidden' not in css)
 record('professional public profile; no learner verdict in UI',all(term not in html for term in ['NOT_ASSESSED','Draft service profile','Hồ sơ định hướng','Confirm fit before a pilot']))
 for rel in ['training/START_HERE.md','training/LEARNING_PATH.md','training/AI_PLAYBOOK.md','training/CLIENT_PLAYBOOK.md','training/EXAM.md','training/RUBRIC.md','training/lab/input.json','COACHING.md']:
  assert (ROOT/rel).is_file(),rel
 record('role-specific learning / AI / client / lab / rubric pack exists',True)
 ignored=subprocess.run(['git','check-ignore','training/assessment_state.local.json','training/submissions/probe.md','training/coach_answer_key.local.md'],cwd=ROOT,capture_output=True,text=True)
 record('personal assessment files excluded from Git',len(ignored.stdout.splitlines())==3)
 with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
 proc=subprocess.Popen([sys.executable,'-m','http.server',str(port),'--bind','127.0.0.1','--directory',str(ROOT)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 base=f'http://127.0.0.1:{port}/'
 for _ in range(50):
  try:urllib.request.urlopen(base,timeout=1);break
  except Exception:time.sleep(.1)
 try:
  with sync_playwright() as p:
   browser=p.chromium.launch()
   errors=[];bad=[];cases=0
   for width in WIDTHS:
    ctx=browser.new_context(viewport={'width':width,'height':900},reduced_motion='reduce')
    page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
    assert page.goto(base).status==200
    for lang in LOCALES:
     page.select_option('#language',lang)
     info=page.evaluate('''() => ({width:document.documentElement.scrollWidth, viewport:innerWidth, lang:document.documentElement.lang, lines:document.querySelectorAll('h1 > span').length, services:document.querySelectorAll('#services-grid article').length, headings:[...document.querySelectorAll('h1,h2,.hero-lead')].every(e=>getComputedStyle(e).textWrap.includes('balance')), blank:[...document.querySelectorAll('[data-ui]')].some(e=>!e.textContent.trim()), labels:[...document.querySelector('#language').options].map(e=>e.textContent), role:document.getElementById('role').textContent, rows:document.querySelectorAll('#case-body tr').length})''')
     cases+=1
     if not(info['width']<=width+1 and info['lang']==lang and info['lines']==2 and info['services']==3 and info['headings'] and not info['blank'] and info['labels']==['VI','EN','ES','ZH'] and info['rows']==6):bad.append({'width':width,'locale':lang,'probe':info})
    page.select_option('#language','vi')
    page.screenshot(path=str(out/f'hero-vi-{width}.png'))
    if width==375:
     page.locator('#services').screenshot(path=str(out/'services-vi-375.png'))
     page.locator('#case').screenshot(path=str(out/'case-vi-375.png'))
    if width==1440:
     page.select_option('#language','en');page.screenshot(path=str(out/'hero-en-1440.png'))
     page.click('#theme');page.screenshot(path=str(out/'hero-en-1440-light.png'))
    ctx.close()
   record(f'responsive / i18n / preserved headline structure ({cases} viewport-locale combinations)',not bad,json.dumps(bad,ensure_ascii=False))
   ctx=browser.new_context(viewport={'width':390,'height':844});page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.goto(base)
   page.click('#filter-review');record('review filter / aria state',page.locator('#case-body tr').count()==4 and page.locator('#filter-review').get_attribute('aria-pressed')=='true')
   page.select_option('#language','en');record('filter remains coherent after language change',page.locator('#case-body tr').count()==4)
   page.click('#filter-all');record('reset filter',page.locator('#case-body tr').count()==6)
   page.click('#theme');page.reload();record('theme and language persist',page.locator('#language').input_value()=='en' and page.evaluate('document.documentElement.classList.contains("light")'))
   page.keyboard.press('Tab');record('visible keyboard skip link',page.evaluate('document.activeElement.classList.contains("skip")') and page.locator('.skip').bounding_box()['y']>=0)
   page.locator('a[href="#contact"]:visible').first.click();record('contact anchor and mailto target',page.url.endswith('#contact') and page.locator('#email-cta').get_attribute('href').startswith('mailto:teoteo1081@gmail.com?subject='))
   with page.expect_download() as dl:page.locator('a[download]').click()
   record('sample JSON download',dl.value.suggested_filename=='sample_data.json')
   sentinel={'w17_04_lang':'zh','w17_04_theme':'light','OTHER_APP':'keep'}
   page.evaluate('(v)=>Object.entries(v).forEach(([k,x])=>localStorage.setItem(k,x))',sentinel);page.reload()
   record('source/sibling storage untouched',page.evaluate('(v)=>Object.entries(v).every(([k,x])=>localStorage.getItem(k)===x)',sentinel))
   page.evaluate('''() => {config.locales.en.services[0][0]='<img src=x onerror="window.pwned=1">';profileApp.render('en')}''')
   record('untrusted text cannot create HTML or execute',page.locator('img[src=x]').count()==0 and page.evaluate('!window.pwned'))
   record('no page JavaScript errors',not errors,str(errors));ctx.close();browser.close()
   profile=Path(tempfile.mkdtemp(prefix='w17_profile_zoom_'));(profile/'Default').mkdir()
   (profile/'Default/Preferences').write_text(json.dumps({'partition':{'default_zoom_level':{'x':math.log(2)/math.log(1.2)}}}),encoding='utf-8')
   try:
    ctx=p.chromium.launch_persistent_context(str(profile),channel='chromium',headless=True,viewport=None,args=['--window-size=1280,900'])
    page=ctx.pages[0];page.goto(base);page.select_option('#language','en')
    zoom=page.evaluate('() => ({inner:innerWidth,outer:outerWidth,dpr:devicePixelRatio,width:document.documentElement.scrollWidth})')
    record('native 200% zoom applied with no page overflow',zoom['dpr']>=1.99 and zoom['inner']<=zoom['outer']*.55 and zoom['width']<=zoom['inner']+1,json.dumps(zoom))
    page.screenshot(path=str(out/'native-zoom-200.png'));ctx.close()
   finally:
    assert profile.resolve().parent==Path(tempfile.gettempdir()).resolve() and profile.name.startswith('w17_profile_zoom_')
    shutil.rmtree(profile,ignore_errors=True)
 finally:
  proc.terminate();proc.wait(timeout=10)
 (out/'results.json').write_text(json.dumps(RESULTS,ensure_ascii=False,indent=2),encoding='utf-8')
 failed=[r for r in RESULTS if r['status']!='PASS'];print(f'{len(RESULTS)-len(failed)}/{len(RESULTS)} PASS')
 sys.exit(bool(failed))
if __name__=='__main__':main()

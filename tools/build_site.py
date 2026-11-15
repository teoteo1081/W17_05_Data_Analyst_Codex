from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]
UI=json.loads((ROOT/'assets/site_ui.json').read_text(encoding='utf-8'))
ISSUES=json.loads((ROOT/'assets/review_issues.json').read_text(encoding='utf-8'))
def esc(v): return html.escape(str(v),quote=True)
def tail(v):
    words=str(v).rsplit(' ',2)
    return esc(words[0])+' '+esc(words[1])+'&nbsp;'+esc(words[2]) if len(words)==3 else esc(v)

def build(p):
    t=UI['vi'];v=p['locales']['vi'];url=f'https://teoteo1081.github.io/{p["folder"]}/'
    packed={**p,'ui':UI,'issues':ISSUES}
    payload=json.dumps(packed,ensure_ascii=False).replace('<','\\u003c')
    def u(key):return f'<span data-ui="{key}">{tail(t[key])}</span>'
    cards=''.join(f'<article class="card"><span class="index">0{i+1}</span><h3>{tail(s[0])}</h3><p>{tail(s[1])}</p></article>' for i,s in enumerate(v['services']))
    steps=''.join(f'<li><h3 data-ui="step{i}">{tail(t[f"step{i}"])}</h3><p data-ui="step{i}_desc">{tail(t[f"step{i}_desc"])}</p></li>' for i in range(1,4))
    headers=''.join(f'<th scope="col" data-ui="{k}">{tail(t[k])}</th>' for k in ['col_id','col_value','col_issue','col_status'])
    return f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Thao Nguyen (TJ) | {esc(v['role'])}</title><meta name="description" content="{esc(v['lead'])}"><meta property="og:title" content="Thao Nguyen (TJ) | {esc(v['role'])}"><meta property="og:description" content="{esc(v['lead'])}"><meta property="og:url" content="{url}"><link rel="stylesheet" href="assets/style.css"><script id="profile-data" type="application/json">{payload}</script><script src="assets/app.js" defer></script></head>
<body><a class="skip" href="#main" data-ui="skip">{tail(t['skip'])}</a>
<header class="header"><div class="wrap header-inner"><a class="brand" href="#main"><span class="brand-mark">TJ</span><span>Thao Nguyen<span class="brand-detail"> · {esc(p['id'].upper())}</span></span></a><nav><a href="#services">{u('nav_services')}</a><a href="#case">{u('nav_case')}</a><a href="#contact">{u('nav_contact')}</a></nav><div class="preferences"><label class="sr-only" for="language">{esc(t['lang_label'])}</label><select id="language" aria-label="{esc(t['lang_label'])}"><option value="vi">VI</option><option value="en">EN</option><option value="es">ES</option><option value="zh">ZH</option></select><button id="theme" type="button" aria-pressed="false" aria-label="{esc(t['theme_label'])}">◐</button></div></div></header>
<main id="main" tabindex="-1"><section class="wrap hero"><div class="hero-label" data-ui="badge">{tail(t['badge'])}</div><p class="hero-role" id="role">{tail(v['role'])}</p><h1><span id="line-one">{tail(v['h1a'])}</span><span id="line-two">{tail(v['h1b'])}</span></h1><p class="hero-lead" id="lead">{tail(v['lead'])}</p><div class="actions"><a class="button" href="#contact">{u('nav_contact')}</a><a class="button secondary" href="#case">{u('nav_case')}</a></div></section>
<section id="services" class="wrap section"><div class="section-head"><h2 data-ui="services_heading">{tail(t['services_heading'])}</h2><p data-ui="services_intro">{tail(t['services_intro'])}</p></div><div id="services-grid" class="cards">{cards}</div><p class="boundary" id="boundary">{tail(v['boundary'])}</p></section>
<section id="case" class="wrap section"><div class="case"><p class="case-badge" data-ui="case_badge">{tail(t['case_badge'])}</p><h2 id="case-title">{tail(v['case_title'])}</h2><div class="case-toolbar"><div class="filters"><button id="filter-all" type="button" aria-pressed="true" data-ui="filter_all">{tail(t['filter_all'])}</button><button id="filter-review" type="button" aria-pressed="false" data-ui="filter_review">{tail(t['filter_review'])}</button></div><p id="counts" class="counts" role="status" aria-live="polite"></p></div><div class="table-scroll" id="case-region" role="region" tabindex="0" aria-label="{esc(v['case_title'])}"><table><caption data-ui="case_badge">{tail(t['case_badge'])}</caption><thead><tr>{headers}</tr></thead><tbody id="case-body"></tbody></table><p id="empty" class="empty" data-ui="empty" hidden>{tail(t['empty'])}</p></div><p class="case-note" data-ui="case_note">{tail(t['case_note'])}</p><div class="actions"><a class="button secondary" href="assets/sample_data.json" download>{u('download')}</a></div></div></section>
<section class="wrap section"><div class="section-head"><h2 data-ui="process_heading">{tail(t['process_heading'])}</h2></div><ol class="steps">{steps}</ol></section>
<section id="contact" class="wrap section"><div class="contact"><h2 data-ui="nav_contact">{tail(t['nav_contact'])}</h2><p data-ui="contact_desc">{tail(t['contact_desc'])}</p><div class="actions"><a id="email-cta" class="button" href="mailto:teoteo1081@gmail.com">{u('contact_button')}</a><a class="button secondary" href="https://teoteo1081.github.io/W17_04_Porfolio_Codex/" target="_blank" rel="noopener noreferrer">{u('prior_work')}</a></div><p class="contact-email">teoteo1081@gmail.com · Zalo <a href="https://zalo.me/0855239805" target="_blank" rel="noopener noreferrer">0855 239 805</a></p></div></section></main><footer class="footer"><div class="wrap">Thao Nguyen (TJ) · <span data-ui="location">{tail(t['location'])}</span></div></footer></body></html>'''

if __name__=='__main__':
    p=json.loads((ROOT/'profile.json').read_text(encoding='utf-8'))
    (ROOT/'index.html').write_text(build(p),encoding='utf-8',newline='\n')
    print('Built index.html from profile.json and local UI dictionaries.')

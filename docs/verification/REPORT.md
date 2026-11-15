# Verification — W17_05_Data_Analyst_Codex

Code / UI audit: AUDIT_PASS. These results describe website behavior, not a judgment of the owner's professional competence.

- Automated: 17/17 PASS; results.json contains individual checks.
- Responsive + i18n: 24 combinations, six widths (320/375/390/768/1024/1440) and four locales (VI/EN/ES/ZH).
- Native 200% zoom: actual browser preference, not viewport emulation; no horizontal page overflow.
- Filters, reset, language/theme persistence, visible keyboard focus, contact anchor, mailto and JSON download exercised.
- No raw innerHTML rendering, empty href, page JS errors, or overflow-x masking.
- Personal assessment state and submissions excluded by Git.
- Build reproducibility checked: profile.json + local UI dictionaries generate the identical index.html.
- Visual inspection: four mobile hero profiles, desktop hero and light mode, sample case table and native zoom. Remaining viewport captures retained for review.
- A cleanup-path guard was added to the test harness after the behavior run; Python syntax verified. Application files were unchanged by that guard.

Files: index.html, profile.json, assets/*, tools/build_site.py, tests/verify_profile.py, README.md, AGENTS.md, COACHING.md, training/*, docs/*.

UI impact: focused specialist landing page with three service offers, clearly labeled synthetic case, scoped delivery process, and real contact links. Public pages have no draft / learning-readiness labels. No fabricated customer results, credentials or testimonials.

Learning: role-specific curriculum, AI controls, client scripts, guided lab, independent capstone and grading rubric are separate from client-facing UI. Actual personal answers and judgments stay local and are not committed.

Limits: Chromium on Windows; no physical-device or full assistive-technology audit. The sample case is illustrative and static, not a live customer integration. Email links open the user's mail application; no automatic sending.

Protected source: W17_04 @ 73c1810 preserved. This repository starts from a new Git root with no copied .git, source history or shared runtime. Remote and published URL are verified during the final delivery step.

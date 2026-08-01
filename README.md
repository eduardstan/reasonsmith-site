# reasonsmith-site

The reasonsmith website: a WebGL proof-graph flight (`index.html`) and the generated
conformance dossier (`report.html`). Deploys to Vercel.

- `index.html`, `site/`, `vendor/`, `assets/` — hand-authored here. Edit directly.
- `report.html` — **generated, never hand-edited.** It is produced by
  `python docs/build_example.py` in [eduardstan/reasonsmith](https://github.com/eduardstan/reasonsmith)
  and held byte-for-byte to `render_html()` by that repo's test suite. Update it by
  copying a freshly built file from there.
- `vendor/` — pinned Three.js r180 (+ core), GSAP 3.13 + ScrollTrigger, Lenis. No CDN,
  no build step: the site is plain static files.

Deploy: `vercel --prod` (project linked to Vercel account `sandrohub013`).

## Brand

- **Logomark** (`assets/mark.svg`): the proof graph of the demo case — five reason nodes
  under the decision node, four struck by the deletion bar, one surviving (green).
  Favicon (`assets/favicon.svg`) is the simplified three-node version for small sizes.
- **Palette**: paper `oklch(96.6% 0.005 95)`, ink `oklch(24% 0.012 260)`,
  deletion red `oklch(50% 0.19 25)` (one accent, one meaning), ok green `oklch(44% 0.11 155)`.
- **Type**: Newsreader (self-hosted variable) for display/body, system mono for data/labels.

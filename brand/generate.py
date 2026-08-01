"""Generate logomark variants for reasonsmith. Run: python brand/generate.py

The mark is the proof graph of the demo case: five reason nodes under the decision
node, four struck by the deletion bar, one surviving (green). Variants explore
color roles, geometry and strike placement while keeping that one idea.
"""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).parent

INK = "#1c1f25"
PAPER = "#f5f4f0"
RED = "#b71824"
GREEN = "#2e7d5b"

REASONS = [(10, 47), (21, 47), (32, 47), (43, 47), (54, 47)]
DECISION = (32, 15)


def classic(ink=INK, paper=None, strike=RED, live=GREEN, radius=5, dr=6.5, sw=1.5, suffix=""):
    """The v1 geometry: fan of five reasons under the decision node."""
    bg = f'<rect width="64" height="64" rx="10" fill="{paper}"/>' if paper else ""
    lines = "".join(
        f'<line x1="{x}" y1="{y}" x2="{DECISION[0]}" y2="{DECISION[1]}"/>' for x, y in REASONS
    )
    nodes = "".join(
        f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{live if i == 0 else ink}"/>'
        for i, (x, y) in enumerate(REASONS)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  {bg}
  <g stroke="{ink}" stroke-opacity="0.35" stroke-width="{sw}">{lines}</g>
  <circle cx="{DECISION[0]}" cy="{DECISION[1]}" r="{dr}" fill="{ink}"/>
  {nodes}
  <rect x="15" y="44.8" width="45" height="4.4" rx="1.2" fill="{strike}" transform="rotate(-3 37.5 47)"/>
</svg>
"""


def horizontal(ink=INK, strike=RED, live=GREEN):
    """One-row proof line: decision at left, reasons in a row, strike through the last four."""
    nodes = "".join(
        f'<circle cx="{12 + i * 10}" cy="32" r="5" fill="{live if i == 0 else ink}"/>'
        for i in range(5)
    )
    lines = "".join(f'<line x1="8" y1="14" x2="{12 + i * 10}" y2="32"/>' for i in range(5))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <g stroke="{ink}" stroke-opacity="0.35" stroke-width="1.5">{lines}</g>
  <circle cx="8" cy="12" r="6" fill="{ink}"/>
  {nodes}
  <rect x="18" y="29.5" width="42" height="5" rx="1.4" fill="{strike}"/>
</svg>
"""


def ring(ink=INK, strike=RED, live=GREEN):
    """Reasons on a ring around the decision node; the strike is a chord."""
    import math

    pts = [(32 + 20 * math.cos(a), 32 + 20 * math.sin(a)) for a in
           [math.radians(90 + i * 72) for i in range(5)]]
    lines = "".join(f'<line x1="32" y1="32" x2="{x:.1f}" y2="{y:.1f}"/>' for x, y in pts)
    nodes = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{live if i == 0 else ink}"/>'
        for i, (x, y) in enumerate(pts)
    )
    # chord covering nodes 1..4 (all but the top one, which survives)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <g stroke="{ink}" stroke-opacity="0.35" stroke-width="1.5">{lines}</g>
  <circle cx="32" cy="32" r="6" fill="{ink}"/>
  {nodes}
  <rect x="10" y="40" width="44" height="4.4" rx="1.2" fill="{strike}" transform="rotate(8 32 42)"/>
</svg>
"""


def dotgrid(ink=INK, strike=RED, live=GREEN):
    """Minimal: five dots ascending like a proof tree, strike cancels four."""
    dots = "".join(
        f'<circle cx="{10 + i * 11}" cy="{50 - i * 9}" r="4.5" fill="{live if i == 0 else ink}"/>'
        for i in range(5)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  {dots}
  <rect x="18" y="28" width="42" height="4.6" rx="1.4" fill="{strike}" transform="rotate(-24 39 30)"/>
</svg>
"""


VARIANTS = {
    "mark-v1-classic.svg": classic(),
    "mark-v2-badge.svg": classic(paper=PAPER),
    "mark-v3-mono.svg": classic(strike=INK, live=INK),
    "mark-v4-darkmode.svg": classic(ink=PAPER, strike=RED, live=GREEN),
    "mark-v5-horizontal.svg": horizontal(),
    "mark-v6-ring.svg": ring(),
    "mark-v7-ascending.svg": dotgrid(),
    "mark-v8-nogreen.svg": classic(live=INK),
}


def contact_sheet(names: list[str]) -> str:
    cells = "".join(
        f'<figure><img src="{n}" width="128"><figcaption>{n}</figcaption></figure>' for n in names
    )
    return f"""<!DOCTYPE html><html><body style="background:#f5f4f0;font-family:monospace">
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;padding:2rem">
{cells}
</div></body></html>"""


if __name__ == "__main__":
    for name, svg in VARIANTS.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print("wrote", name)
    (OUT / "contact-sheet.html").write_text(contact_sheet(list(VARIANTS)), encoding="utf-8")
    print("wrote contact-sheet.html")

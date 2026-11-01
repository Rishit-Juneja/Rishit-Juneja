# Generates cards/*.svg (vial "build" cards for the README). Run: python3 scripts/cards.py
from html import escape as e
C = {"Vision": "#35b4ea", "Agents": "#5ddf6a", "Signal": "#f2df1a"}
B = [
 ("sentinel", "Vision", "Live demo", "Attendance", "Sentinel", "Eyes on every classroom.",
  ["Face-recognition attendance on live CCTV, 100+ students.", "Catches photo spoofs and covered faces."], ["YOLO", "ArcFace", "ByteTrack", "FAISS"]),
 ("office", "Agents", "Shipping", "AI", "Office", "A company that ships itself.",
  ["Manager agent assigns work; reviewers run in parallel.", "Security scans, render checks, git checkpoints."], ["Python", "LLM agents", "SQLite", "Playwright"]),
 ("jarvis", "Signal", "Runs local", "", "Jarvis", "It listens before you speak.",
  ["Clap wake-up, Whisper STT, edge-tts voice.", "Ollama reasons over Redis memory. No cloud."], ["Whisper", "Ollama", "Redis", "n8n"]),
 ("sixth-sense", "Vision", "36h build", "Sixth", "Sense", "The web, for every pair of eyes.",
  ["Blind, colorblind, ADHD and low-vision modes.", "Claude API voice navigation steers the page."], ["Chrome ext", "Claude API", "a11y"]),
 ("gagan", "Agents", "Weekly", "Gagan", "Express", "A newsroom in a script.",
  ["Live RSS feeds into an 8-page Hindi broadsheet.", "Devanagari typography, print-ready PDF."], ["Python", "RSS", "Jinja2", "WeasyPrint"]),
 ("clipper", "Agents", "Live", "The", "Clipper", "One command, a finished short.",
  ["Whisper transcribes, AI picks the viral moment.", "ffmpeg edits, auto-uploads at peak time."], ["Whisper", "ffmpeg", "YouTube API"]),
]
SERIF = "'Bodoni Moda','Bodoni 72',Didot,Georgia,serif"
MONO = "ui-monospace,'SF Mono','IBM Plex Mono',Menlo,Consolas,monospace"
VIAL = "M52 84 L88 84 L90 112 C112 118 116 132 116 150 L116 340 C116 356 104 364 88 364 L52 364 C36 364 24 356 24 340 L24 150 C24 132 28 118 50 112Z"

for i, (slug, spirit, state, w1, w2, tag, pts, stack) in enumerate(B):
    c = C[spirit]
    x = 24; chips = []
    for s in stack:
        wd = len(s) * 7.6 + 18
        chips.append(f'<rect x="{x}" y="244" width="{wd:.0f}" height="24" fill="#fff" stroke="#0e0b0b" stroke-width="1.5"/>'
                     f'<text x="{x + 9}" y="260" class="m" font-size="10.5">{e(s)}</text>')
        x += wd + 6
    title = (f'{e(w1)} <tspan font-style="italic" font-weight="700" fill="#c8141f">{e(w2)}</tspan>' if w1
             else f'<tspan font-style="italic" font-weight="700" fill="#c8141f">{e(w2)}</tspan>')
    bullets = "".join(f'<text x="24" y="{186 + j * 24}" font-family="Archivo,Helvetica,Arial,sans-serif" font-size="14.5" fill="#0e0b0b">'
                      f'<tspan fill="#c8141f" font-weight="700">›</tspan>  {e(p)}</text>' for j, p in enumerate(pts))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="310" viewBox="0 0 600 310" role="img" aria-label="{e(w1 + ' ' + w2)}: {e(tag)}">
<defs><pattern id="h" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(38)"><rect width="1.7" height="7" fill="#0e0b0b"/></pattern>
<clipPath id="v"><path d="{VIAL}"/></clipPath>
<style>.m{{font-family:{MONO};font-weight:600;letter-spacing:.12em;text-transform:uppercase;fill:#0e0b0b}}
.f{{animation:f 3.6s ease-in-out {-i * .6:.1f}s infinite}}@keyframes f{{50%{{transform:translateY(-8px)}}}}
.b{{opacity:0;animation:b 2.8s ease-in infinite}}@keyframes b{{0%{{transform:translate(0,0);opacity:0}}15%{{opacity:1}}100%{{transform:translate(6px,-150px);opacity:0}}}}
.in{{opacity:0;animation:in .7s cubic-bezier(.2,.8,.2,1) {i * .15:.2f}s forwards}}@keyframes in{{from{{opacity:0;transform:translateY(40px) rotate(-1.5deg)}}to{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important}}.b{{display:none}}}}</style></defs>
<g class="in">
<rect x="10" y="10" width="580" height="290" fill="#0e0b0b"/>
<rect x="2" y="2" width="580" height="290" fill="#f4efe6" stroke="#0e0b0b" stroke-width="3"/>
<rect x="24" y="22" width="11" height="15" rx="3" fill="{c}" stroke="#0e0b0b" stroke-width="1.5"/>
<text x="43" y="35" class="m" font-size="11">{e(spirit)}</text>
<rect x="{330 - len(state) * 7.8:.0f}" y="18" width="{len(state) * 7.8 + 20:.0f}" height="24" rx="12" fill="none" stroke="#0e0b0b" stroke-width="1.5"/>
<text x="{340 - len(state) * 7.8:.0f}" y="34" class="m" font-size="10.5">{e(state)}</text>
<text x="22" y="98" font-family="{SERIF}" font-size="{50 if len(w1 + w2) < 16 else 42}" font-weight="900" fill="#0e0b0b" letter-spacing="-1">{title}</text>
<text x="24" y="138" font-family="{SERIF}" font-size="20" font-style="italic" fill="#675b54">{e(tag)}</text>
{bullets}
{"".join(chips)}
<g transform="translate(420 18) scale(.68)"><g class="f">
<path d="{VIAL}" fill="{c}"/>
<g clip-path="url(#v)"><rect y="80" width="140" height="300" fill="url(#h)" opacity=".26"/><rect x="34" y="140" width="9" height="140" rx="4.5" fill="#fff" opacity=".5"/><rect y="292" width="140" height="80" fill="#0e0b0b"/></g>
<path d="{VIAL}" fill="none" stroke="#0e0b0b" stroke-width="4" stroke-linejoin="round"/>
<g fill="rgba(255,255,255,.65)" stroke="#0e0b0b" stroke-width="1.5"><circle class="b" cx="60" cy="280" r="6"/><circle class="b" cx="80" cy="290" r="4" style="animation-delay:.7s"/><circle class="b" cx="66" cy="285" r="5" style="animation-delay:1.4s"/><circle class="b" cx="88" cy="270" r="3.5" style="animation-delay:2.1s"/></g>
<rect x="46" y="48" width="48" height="38" rx="5" fill="#efe8dc" stroke="#0e0b0b" stroke-width="3.5"/><path d="M46 58H94M46 67H94M46 76H94" stroke="#0e0b0b" stroke-width="2"/>
<ellipse cx="70" cy="30" rx="25" ry="22" fill="#d8d2c8" stroke="#0e0b0b" stroke-width="3.5"/>
<text x="70" y="330" text-anchor="middle" font-family="'Pinyon Script','Snell Roundhand',cursive" font-size="34" fill="#f4efe6">{e(w2[:1])}</text>
</g></g>
</g></svg>'''
    open(f"cards/{slug}.svg", "w").write(svg)
    print("cards/" + slug + ".svg")

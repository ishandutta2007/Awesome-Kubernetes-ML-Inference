import random, math

random.seed(7)
W, H = 1200, 300
parts = []

# Floating particles (behind everything else)
for i in range(26):
    x = random.randint(0, W)
    y = random.randint(10, H - 10)
    r = random.choice([1.5, 2, 2, 2.5, 3])
    dur = round(random.uniform(3.5, 9.0), 2)
    delay = round(random.uniform(0, 4), 2)
    dy = random.choice([-40, -30, 30, 40, -50, 50])
    op = round(random.uniform(0.25, 0.75), 2)
    color = random.choice(["#7dd3fc", "#a78bfa", "#34d399", "#f0abfc"])
    parts.append(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="{op}">'
        f'<animate attributeName="cy" values="{y};{y + dy};{y}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="{op};0.05;{op}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>'
        f'</circle>'
    )

# Pulsing "cluster nodes" with links (K8s-style graph feel)
nodes = [(120, 70), (240, 40), (330, 120), (900, 60), (1010, 110), (1100, 50),
         (90, 240), (210, 270), (950, 250), (1080, 210), (1150, 275), (400, 40)]
edges = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (6, 7), (8, 9), (9, 10), (8, 10), (1, 11)]
for a, b in edges:
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    parts.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#38bdf8" stroke-width="1" opacity="0.28">'
        f'<animate attributeName="opacity" values="0.1;0.5;0.1" dur="4s" begin="{random.uniform(0,3):.2f}s" repeatCount="indefinite"/>'
        f'</line>'
    )
for idx, (x, y) in enumerate(nodes):
    dur = round(random.uniform(2.2, 4.4), 2)
    parts.append(
        f'<circle cx="{x}" cy="{y}" r="4.5" fill="#38bdf8" opacity="0.55">'
        f'<animate attributeName="r" values="3.5;6;3.5" dur="{dur}s" begin="{random.uniform(0,2):.2f}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0.6;0.2;0.6" dur="{dur}s" repeatCount="indefinite"/>'
        f'</circle>'
    )

# Packets travelling along two long links (data-flow animation)
flows = [(0, 40, 380, 150, "#7dd3fc", "0s", "3.2s"),
         (1200, 70, 760, 170, "#a78bfa", "0.6s", "3.8s"),
         (0, 250, 400, 210, "#34d399", "1.2s", "3.5s"),
         (1200, 260, 780, 205, "#f0abfc", "0.3s", "4.1s")]
for (x1, y1, x2, y2, color, begin, dur) in flows:
    parts.append(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1" stroke-dasharray="6 10" opacity="0.35">'
        f'<animate attributeName="stroke-dashoffset" values="0;-160" dur="{dur}" begin="{begin}" repeatCount="indefinite"/>'
        f'</line>'
    )

# Flowing sine waves along the bottom (throughput feel)
def wave(y0, amp, phase, color, op):
    pts = []
    for x in range(0, W + 20, 20):
        pts.append(f"{x},{y0 + amp * math.sin(x / 90 + phase):.1f}")
    d = "M" + " L".join(pts)
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6" opacity="{op}" '
            f'stroke-dasharray="14 260"><animate attributeName="stroke-dashoffset" values="0;-548" dur="6s" repeatCount="indefinite"/></path>')

waves = [wave(268, 10, 0.0, "#38bdf8", 0.5),
         wave(278, 8, 1.4, "#a78bfa", 0.45),
         wave(258, 7, 2.6, "#34d399", 0.4)]

# Scanning light beam sweeping across the background
beam = ('<rect x="-260" y="0" width="220" height="300" fill="url(#beam)" opacity="0.5">'
        '<animate attributeName="x" values="-260;1200" dur="9s" begin="0s" repeatCount="indefinite"/></rect>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Awesome Kubernetes ML Inference banner">
  <title>Awesome Kubernetes ML Inference — LLM &amp; Model Serving on Kubernetes</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1220">
        <animate attributeName="stop-color" values="#0b1220;#111a33;#0b1220" dur="12s" repeatCount="indefinite"/>
      </stop>
      <stop offset="55%" stop-color="#101c36">
        <animate attributeName="stop-color" values="#101c36;#16233f;#101c36" dur="12s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#0d1b2a">
        <animate attributeName="stop-color" values="#0d1b2a;#131f3a;#0d1b2a" dur="12s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b1220" stop-opacity="0.88"/>
      <stop offset="100%" stop-color="#0b1220" stop-opacity="0.80"/>
    </linearGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="55%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#7dd3fc"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="18"/>
    </filter>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <ellipse cx="250" cy="60" rx="220" ry="90" fill="#1d4ed8" opacity="0.22" filter="url(#soft)">
    <animate attributeName="cx" values="250;420;250" dur="14s" repeatCount="indefinite"/>
  </ellipse>
  <ellipse cx="980" cy="260" rx="230" ry="95" fill="#7c3aed" opacity="0.20" filter="url(#soft)">
    <animate attributeName="cx" values="980;820;980" dur="16s" repeatCount="indefinite"/>
  </ellipse>
  {beam}
  {"".join(parts)}
  {"".join(waves)}

  <g aria-hidden="true">
    <rect x="200" y="78" width="800" height="150" rx="18" fill="url(#panel)" stroke="#38bdf8" stroke-opacity="0.35"/>
    <rect x="200" y="78" width="800" height="150" rx="18" fill="none" stroke="url(#title)" stroke-opacity="0.25" stroke-width="1">
      <animate attributeName="stroke-opacity" values="0.1;0.45;0.1" dur="5s" repeatCount="indefinite"/>
    </rect>
    <text x="600" y="140" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="40" font-weight="700" fill="url(#title)">Awesome Kubernetes ML Inference</text>
    <text x="600" y="182" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="18" fill="#94a3b8">LLM &amp; Model Serving on Kubernetes · SaaS pricing vs. open-source engines, compared</text>
    <g font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="13" font-weight="600">
      <rect x="418" y="198" width="86" height="22" rx="11" fill="#38bdf8" opacity="0.16"/>
      <text x="461" y="213" text-anchor="middle" fill="#7dd3fc">vLLM</text>
      <rect x="512" y="198" width="86" height="22" rx="11" fill="#a78bfa" opacity="0.16"/>
      <text x="555" y="213" text-anchor="middle" fill="#c4b5fd">SGLang</text>
      <rect x="606" y="198" width="86" height="22" rx="11" fill="#34d399" opacity="0.16"/>
      <text x="649" y="213" text-anchor="middle" fill="#6ee7b7">KServe</text>
      <rect x="700" y="198" width="86" height="22" rx="11" fill="#f0abfc" opacity="0.16"/>
      <text x="743" y="213" text-anchor="middle" fill="#f5d0fe">Triton</text>
    </g>
  </g>
</svg>
'''

import os
os.makedirs("assets", exist_ok=True)
with open("assets/banner.svg", "w", encoding="utf-8", newline="\n") as f:
    f.write(svg)
print("wrote assets/banner.svg", len(svg), "bytes")

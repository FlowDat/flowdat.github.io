#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://flowdat.github.io"

NAV = """
<header class="site-header" id="header">
  <a class="skip" href="#main">Skip to content</a>
  <div class="header-inner">
    <a class="brand" href="/">
      <svg class="mark" viewBox="0 0 32 32" fill="none" aria-hidden="true">
        <rect width="32" height="32" rx="6" fill="#08090c"/>
        <g stroke="#5ee0c8" stroke-width="1.4" stroke-linecap="square">
          <path d="M6 9h8M10 6v6"/>
          <path d="M14 16h10M19 12v8" opacity=".85"/>
          <path d="M8 24h6M11 21v6" opacity=".65"/>
        </g>
        <circle cx="24.5" cy="23.5" r="1.4" fill="#d08a5a"/>
      </svg>
      <span>Flowdat</span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav id="menu" class="nav">
      <a href="/work.html" data-page="work">Work</a>
      <a href="/publications.html" data-page="papers">Papers</a>
      <a href="/codes.html" data-page="codes">Codes</a>
      <a href="/about.html" data-page="about">About</a>
      <a class="nav-cv" href="/assets/cv.pdf">CV</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="brand-foot">Flowdat</p>
      <p>The computational practice of Syed Muhammad Usama — turbulence, mixing, and molecular reaction, computed.</p>
    </div>
    <div>
      <p class="kicker">Contact</p>
      <div class="foot-list">
        <a href="mailto:usama@dicp.ac.cn">usama@dicp.ac.cn</a>
        <a href="mailto:usama784@gmail.com">usama784@gmail.com</a>
        <span>Dalian, China</span>
      </div>
    </div>
    <div>
      <p class="kicker">Elsewhere</p>
      <div class="foot-list">
        <a href="https://www.linkedin.com/in/syedusama8386/">LinkedIn</a>
        <a href="https://orcid.org/0000-0002-8181-4369">ORCID</a>
        <a href="https://scholar.google.com/citations?user=XrRe2kkAAAAJ">Google Scholar</a>
        <a href="https://github.com/FlowDat">GitHub</a>
        <a href="https://www.researchgate.net/profile/Syed-Usama">ResearchGate</a>
      </div>
    </div>
  </div>
  <p class="colophon"><span>© <span id="year">2026</span> Syed Muhammad Usama</span><span>State Key Laboratory of Molecular Reaction Dynamics, DICP–CAS</span></p>
</footer>
<script src="/assets/js/site.js"></script>
"""


def page(path, title, desc, body, page_id="", extra_head=""):
    canonical = SITE + (path if path != "/index.html" else "/")
    og = f"{SITE}/assets/img/og.jpg"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/site.css">
  {extra_head}
</head>
<body data-page="{page_id}">
{NAV}
<main id="main">
{body}
</main>
{FOOT}
</body>
</html>
"""
    out = ROOT / path.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


JSONLD = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Syed Muhammad Usama",
  "honorificSuffix": "Ph.D.",
  "jobTitle": "Computational Scientist",
  "affiliation": {
    "@type": "Organization",
    "name": "Dalian Institute of Chemical Physics, Chinese Academy of Sciences"
  },
  "url": "https://flowdat.github.io/",
  "email": "usama@dicp.ac.cn",
  "sameAs": [
    "https://orcid.org/0000-0002-8181-4369",
    "https://www.linkedin.com/in/syedusama8386/",
    "https://scholar.google.com/citations?user=XrRe2kkAAAAJ",
    "https://github.com/FlowDat",
    "https://www.researchgate.net/profile/Syed-Usama"
  ]
}
</script>
"""

HOME = r"""
<section class="hero">
  <canvas id="flow" aria-hidden="true"></canvas>
  <div class="hero-inner">
    <p class="kicker">Flowdat · Laboratory</p>
    <h1>Syed Muhammad <em>Usama</em></h1>
    <p class="lead">Computational scientist at the Dalian Institute of Chemical Physics, Chinese Academy of Sciences. I design numerical methods for turbulence, mixing, and molecular reaction — from burst-buffer DNS of 3D sparse grids to quantum wavepackets on stair-shaped meshes.</p>
    <div class="hero-actions">
      <a class="btn btn-solid" href="/work.html">Selected work</a>
      <a class="btn btn-ghost" href="/assets/cv.pdf">Download CV</a>
    </div>
  </div>
  <ul class="hero-stats">
    <li><b>15+</b><span>Years in research and teaching</span></li>
    <li><b>Principal Scientist</b><span>DICP · Chinese Academy of Sciences, 2023</span></li>
    <li><b>Almarai</b><span>Best Thesis Award, KFUPM, 2019</span></li>
    <li><b>Computers &amp; Fluids</b><span>Burst-buffer DNS of 3DS grids, 2026</span></li>
  </ul>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">01 — Methods</p>
    <div class="section-head">
      <h2>What I compute with.</h2>
      <p>Direct numerical simulation, kinematic simulation, quantum wavepackets, physics-constrained learning, and OpenFOAM — usually on large parallel machines.</p>
    </div>
    <div class="methods">
      <span>DNS</span><span>OpenFOAM</span><span>RANS / SST / LES</span><span>Kinematic simulation</span>
      <span>Quantum wavepackets</span><span>Hyperspherical coordinates</span><span>PINNs / SPECTRE</span>
      <span>Burst buffers · HPC</span><span>POD / ROM</span><span>Multiphase &amp; FSI</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap-wide">
    <div class="wrap" style="margin-bottom:1.6rem">
      <p class="num">02 — Research</p>
      <div class="section-head">
        <h2>Selected work.</h2>
        <a class="link-more" href="/work.html">All projects →</a>
      </div>
    </div>

    <a class="feature" href="/work/3ds.html">
      <img src="/assets/img/work-3ds.jpg" alt="Three-dimensional sparse multiscale grid generating a turbulent wake">
      <div class="feature-body">
        <p class="kicker">Turbulence · HPC</p>
        <h3>Burst-buffer DNS of 3D sparse grids</h3>
        <p>A 3DSG with 24% blockage matches the turbulence intensity of classical and fractal grids that block far more of the tunnel. The burst-buffer algorithm cut wall time fivefold and raised parallel efficiency eightfold.</p>
        <div class="meta"><span class="tag">Computers &amp; Fluids, 2026</span><span>Re = 4000 · GitHub/FlowDat/3DS</span></div>
      </div>
    </a>

    <div class="grid-2">
      <a class="card" href="/work/spectre.html">
        <div class="thumb"><img src="/assets/img/work-spectre.jpg" alt="Neural lattice over a turbulent mixing layer"></div>
        <div class="card-body">
          <p class="kicker">Learning · Mixing</p>
          <h3>SPECTRE</h3>
          <p>A scale-aware, physics-constrained network that emulates turbulent mixing layers across Reynolds numbers from 2,500 to 30,000.</p>
          <div class="meta"><span class="tag">Under review</span><span>Results in Engineering, 2026</span></div>
        </div>
      </a>
      <a class="card" href="/work/quantum.html">
        <div class="thumb"><img src="/assets/img/work-quantum.jpg" alt="Quantum wavepacket on a stair-shaped grid"></div>
        <div class="card-body">
          <p class="kicker">Quantum dynamics</p>
          <h3>Stair-shaped grids</h3>
          <p>Time-dependent wavepackets in hyperspherical coordinates, with 18–33% fewer grid points on F+HCl, O+O₂ and Cl+H₂.</p>
          <div class="meta"><span class="tag">Chem. Phys. Lett. 2024</span><span>Theor. Chem. Acc. 2024</span></div>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap now">
    <div>
      <p class="num">03 — Now</p>
      <h2>State Key Laboratory of Molecular Reaction Dynamics.</h2>
    </div>
    <div>
      <p class="lead">I am a computational scientist at DICP, Chinese Academy of Sciences, in Dalian. The lab sits at the intersection of fluid mechanics, combustion, and quantum chemistry — Nature Index rank 1 worldwide.</p>
      <p>Before Dalian I was Lecturer-B at KFUPM, where the Almarai Best Thesis Award recognized my Ph.D. on 3D sparse-grid turbulence and inertial particle-pair diffusion. Earlier I taught and consulted at COMSATS Islamabad. The through-line is the same: efficient numerics for flows that mix, burn, or scatter.</p>
      <div class="hero-actions">
        <a class="btn btn-ghost" href="/about.html">Biography &amp; CV</a>
        <a class="btn btn-ghost" href="/publications.html">Publication list</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">04 — Papers</p>
    <div class="section-head">
      <h2>Recent writing.</h2>
      <a class="link-more" href="/publications.html">Full list →</a>
    </div>
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Burst buffer accelerated direct numerical simulation of turbulence generated by 3D sparse multiscale grids</h3>
        <p class="authors">S. M. Usama, N. A. Malik, U. Umer, A. Shaikh, Z. Sun</p>
        <p class="venue"><em>Computers &amp; Fluids</em> 308, 106985</p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Published</span></div>
    </article>
    <article class="pub">
      <div class="year">2024</div>
      <div>
        <h3>A time-dependent quantum wavepacket method on stair-shaped grids for reactive scattering using the hyperspherical coordinates</h3>
        <p class="authors">U. Umer, S. K. Usman, S. M. Usama, H. Zhao, Z. Sun</p>
        <p class="venue"><em>Chemical Physics Letters</em> 837, 141060</p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Published</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Turbulence behind 3D multi-scale sparse grids</h3>
        <p class="authors">S. M. Usama, J. Tellez-Alvarez, J. Kopec, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue"><em>J. Phys.: Conf. Series</em> 1101, 012048</p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Open access</span></div>
    </article>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">05 — Contact</p>
    <h2 style="font-size:clamp(2rem,4vw,3.2rem);max-width:16ch;margin-bottom:0.8rem">If the problem involves a flow, write.</h2>
    <p class="lead">Collaborations, students, and industrial CFD are welcome — mixing, combustion, reservoirs, turbines, batteries, or quantum reactive scattering.</p>
    <div class="contact-row">
      <a class="btn btn-solid" href="mailto:usama@dicp.ac.cn">usama@dicp.ac.cn</a>
      <a class="btn btn-ghost" href="https://www.linkedin.com/in/syedusama8386/">LinkedIn</a>
      <a class="btn btn-ghost" href="https://orcid.org/0000-0002-8181-4369">ORCID</a>
    </div>
  </div>
</section>
"""

WORK = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Research &amp; applications</p>
    <h1>Work.</h1>
    <p class="lead">Peer-reviewed numerics, industrial CFD, and open codes. Filter by theme, or open a case for the method, the result, and the paper.</p>
    <div class="filters" role="tablist">
      <button data-filter="all" class="is-on">All</button>
      <button data-filter="turbulence">Turbulence</button>
      <button data-filter="quantum">Quantum</button>
      <button data-filter="energy">Energy</button>
      <button data-filter="code">Codes</button>
    </div>
  </div>
</section>
<section style="padding-bottom:5rem">
  <div class="wrap-wide grid-3">
    <a class="card" href="/work/3ds.html" data-filter-item="turbulence code">
      <div class="thumb"><img src="/assets/img/work-3ds.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Turbulence · HPC</p>
        <h3>3D sparse-grid DNS</h3>
        <p>Burst-buffer accelerated Navier–Stokes. 3DSG at 24% blockage rivals denser fractal and classical grids.</p>
        <div class="meta"><span class="tag">Computers &amp; Fluids</span></div>
      </div>
    </a>
    <a class="card" href="/work/spectre.html" data-filter-item="turbulence code">
      <div class="thumb"><img src="/assets/img/work-spectre.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Learning</p>
        <h3>SPECTRE</h3>
        <p>Scale-aware deep emulator for turbulent mixing layers, trained on DNS from Re 2,500–30,000.</p>
        <div class="meta"><span class="tag">Under review</span></div>
      </div>
    </a>
    <a class="card" href="/work/quantum.html" data-filter-item="quantum">
      <div class="thumb"><img src="/assets/img/work-quantum.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Quantum dynamics</p>
        <h3>Stair-shaped grids</h3>
        <p>Wavepacket reactive scattering in hyperspherical coordinates for F+HCl, O+O₂, Cl+H₂.</p>
        <div class="meta"><span class="tag">CPL · TCA 2024</span></div>
      </div>
    </a>
    <a class="card" href="/work/particles.html" data-filter-item="turbulence">
      <div class="thumb"><img src="/assets/img/work-particles.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Dispersion</p>
        <h3>Inertial particle pairs</h3>
        <p>Kinematic simulation of pair diffusion — pollen, sandstorms, industrial aerosols — locality versus non-locality.</p>
        <div class="meta"><span class="tag">Ph.D. thesis · AMMCS</span></div>
      </div>
    </a>
    <a class="card" href="/work/wind.html" data-filter-item="energy">
      <div class="thumb"><img src="/assets/img/work-wind.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Wind energy</p>
        <h3>Blade flow control &amp; ROM</h3>
        <p>CFD of turbine blades with passive/active devices, plus POD-based reduced-order models of the near-blade flow.</p>
        <div class="meta"><span class="tag">Blade_pod</span></div>
      </div>
    </a>
    <a class="card" href="/work/battery.html" data-filter-item="energy">
      <div class="thumb"><img src="/assets/img/work-battery.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Thermal</p>
        <h3>Battery thermal management</h3>
        <p>Multiscale CFD and computational chemistry to diagnose thermal runaway in lithium-ion packs.</p>
        <div class="meta"><span class="tag">BTMS</span></div>
      </div>
    </a>
    <a class="card" href="/work/reservoir.html" data-filter-item="energy code">
      <div class="thumb"><img src="/assets/img/work-reservoir.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Subsurface</p>
        <h3>Reservoir simulation</h3>
        <p>OpenFOAM tutorials and cases for multiphase reservoir flow, well control, and parallel I/O.</p>
        <div class="meta"><span class="tag">OpenFOAM</span></div>
      </div>
    </a>
    <a class="card" href="/work/hydrotwin.html" data-filter-item="code turbulence">
      <div class="thumb"><img src="/assets/img/work-hydrotwin.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Product</p>
        <h3>HydroTwin Studio</h3>
        <p>A desktop layer over CFD so case setup, meshing, and post-processing stop being the bottleneck.</p>
        <div class="meta"><span class="tag">In development</span></div>
      </div>
    </a>
  </div>
</section>
"""


def case(kicker, title, lead, img, alt, side, copy):
    return f"""
<section class="case-hero">
  <div class="wrap">
    <a class="back" href="/work.html">← All work</a>
    <p class="kicker">{kicker}</p>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
  <div class="wrap-wide case-cover">
    <img src="{img}" alt="{alt}">
  </div>
</section>
<section class="wrap case-layout">
  <aside>
    <dl class="case-side">{side}</dl>
  </aside>
  <article class="case-copy">{copy}</article>
</section>
"""


CASE_3DS = case(
    "Turbulence · High-performance computing",
    "Burst-buffer DNS of 3D sparse multiscale grids",
    "A new grid family, a faster I/O path, and a wind-tunnel-scale DNS that shows sparse 3D grids can punch above their blockage.",
    "/assets/img/work-3ds.jpg",
    "Sparse 3D grid and turbulent wake",
    """
    <div><dt>Venue</dt><dd><em>Computers &amp; Fluids</em> 308 (2026) 106985</dd></div>
    <div><dt>DOI</dt><dd><a href="https://doi.org/10.1016/j.compfluid.2026.106985">10.1016/j.compfluid.2026.106985</a></dd></div>
    <div><dt>With</dt><dd>Nadeem A. Malik, Umair Umer, Amjad Shaikh, Zhigang Sun</dd></div>
    <div><dt>Code &amp; data</dt><dd><a href="https://github.com/FlowDat/3DS">github.com/FlowDat/3DS</a></dd></div>
    <div><dt>Thesis</dt><dd><a href="https://eprints.kfupm.edu.sa/140958/">KFUPM ePrints, 2019</a></dd></div>
    """,
    r"""
    <p>Grid-generated turbulence is the workhorse of wind-tunnel research: a simple blockage that turns a uniform stream into a controllable cascade. Classical square grids do it at one scale. Flat fractal grids inject several scales at once, at the cost of a high blockage ratio. The <strong>3D sparse grid (3DS)</strong> — patented by N. A. Malik — puts each scale on its own co-frame, spaced along the tunnel, so the effective blockage can drop well below a 2D fractal of similar intensity.</p>
    <p>I have spent much of the last decade asking whether that geometric idea survives a genuine Navier–Stokes test. Direct numerical simulation of the full grid, the developing wakes, and the downstream decay is expensive: the files are huge, the parallel filesystem saturates, and wall-clock time is dominated by I/O. The <strong>burst-buffer accelerated DNS algorithm (BBDSA)</strong> parks those bursts on fast intermediate storage. In the 2026 <em>Computers &amp; Fluids</em> study it delivered a fivefold cut in compute time and an eightfold gain in parallel efficiency, with no loss of accuracy.</p>
    <figure class="figure">
      <img src="/assets/img/figures/turb36.png" alt="Isosurfaces of vorticity in a turbulent channel from DNS">
      <figcaption class="caption">Vorticity field from a related DNS — the kind of volume the burst-buffer path is built to swallow.</figcaption>
    </figure>
    <h2>What the comparison showed</h2>
    <p>We ran a uniform inflow at Reynolds number 4000 in a conduit the size of a laboratory tunnel, and compared two-dimensional classical grids, two-dimensional fractal grids, and 3DSG. A 3DSG with only 24% blockage produced turbulence intensities and Reynolds stresses comparable to classical and fractal grids with substantially higher blockage. That is the practical claim: <strong>the same free-stream turbulence for less energy dumped into drag</strong>.</p>
    <p>Earlier conference DNS — <em>J. Phys.: Conf. Series</em> 1101, 012048 (2018) — had already shown the 3-frame 3DS parameter space (blockage, effective mesh size, inter-frame spacing, bar thickness). The 2026 paper is the production run: a tuned I/O stack, a clean three-way comparison, and data on GitHub.</p>
    <h2>Why it matters</h2>
    <p>Wind tunnels, combustion rigs, and mixing vessels all need homogeneous, intense turbulence without paying for it in pressure drop. Sparse 3D grids, and the HPC path that makes their DNS affordable, are a way to design that turbulence instead of inheriting it.</p>
    """,
)

CASE_SPECTRE = case(
    "Scientific machine learning · Mixing",
    "SPECTRE — a scale-aware emulator of turbulent mixing layers",
    "Direct numerical simulation remains the truth. SPECTRE is the fast twin: a physics-constrained network that reconstructs mixing layers from Re 2,500 to 30,000.",
    "/assets/img/work-spectre.jpg",
    "Neural overlay on a mixing layer",
    """
    <div><dt>Status</dt><dd>Under review, <em>Results in Engineering</em>, 2026</dd></div>
    <div><dt>Model</dt><dd>SPECTRE — scale-aware deep-learning turbulence emulator</dd></div>
    <div><dt>With</dt><dd>N. A. Malik, U. Umer, A. Shaikh, M. Z. Akhter, S. A. Ali, Z. Sun</dd></div>
    <div><dt>Code &amp; data</dt><dd><a href="https://github.com/FlowDat/SMLG">github.com/FlowDat/SMLG</a></dd></div>
    <div><dt>Data</dt><dd><a href="https://zenodo.org/records/21234013">Zenodo 21234013</a></dd></div>
    """,
    r"""
    <p>Mixing layers are simple enough to DNS and hard enough to matter: two streams, a shear, a scalar, a growing thickness. They are also a brutal test for a surrogate. A network that only fits one Reynolds number has learned a picture, not a flow.</p>
    <p><strong>SPECTRE</strong> is a scale-separated, physics-constrained deep network trained on DNS of turbulent mixing layers at seven Reynolds numbers — 2,500, 5,000, 10,000, 15,000, 20,000, 25,000, 30,000. The fields stored with the model are streamwise and wall-normal velocity, pressure, and scalar concentration, together with the mean, the temporal coefficients of a reduced-order model, and the reconstruction. The public analysis stack plots spectral content, stresses, coherent structures, and mixing metrics against the original DNS.</p>
    <p>The companion manuscript on the CV, <em>Scale-separated, physics constrained, deep neural network for turbulent mixing layer simulations</em>, is under review at <em>Results in Engineering</em> (2026). The SMLG repository is the working digital twin of that paper: copy the Zenodo dump into <code>data/</code>, run the analysis, and the figures of the manuscript come back.</p>
    <h2>The point of a twin</h2>
    <p>DNS of a mixing layer at Re 30,000 is not something you rerun to try a new Schmidt number over lunch. An emulator that respects scale separation and the conservation structure of the flow is how you explore the neighbourhood of a validated case — and how a platform like HydroTwin can feel interactive without lying about the physics.</p>
    """,
)

CASE_QUANTUM = case(
    "Quantum molecular dynamics",
    "Stair-shaped grids for reactive scattering",
    "Hyperspherical wavepackets that stop wasting points on regions the reaction never visits — and still resolve long-lived resonances.",
    "/assets/img/work-quantum.jpg",
    "Wavepacket on stair-shaped domains",
    """
    <div><dt>Papers</dt><dd><em>Chem. Phys. Lett.</em> 837, 141060 (2024)<br><em>Theor. Chem. Acc.</em> 143, 61 (2024)</dd></div>
    <div><dt>DOI</dt><dd><a href="https://doi.org/10.1016/j.cplett.2023.141060">10.1016/j.cplett.2023.141060</a><br><a href="https://doi.org/10.1007/s00214-024-03133-w">10.1007/s00214-024-03133-w</a></dd></div>
    <div><dt>With</dt><dd>Umair Umer, Syed Kazim Usman, Hailin Zhao, Zhigang Sun</dd></div>
    <div><dt>Lab</dt><dd>State Key Laboratory of Molecular Reaction Dynamics, DICP</dd></div>
    """,
    r"""
    <p>Three atoms meet; a bond breaks; another forms. In hyperspherical coordinates the whole story — reactants, products, every arrangement in between — lives on one map. That elegance has a cost. As the hyper-radius grows, the angular grid must densify, and long-range potentials or long absorption tails make the calculation prohibitive.</p>
    <p>We split the hyper-radius into <strong>stair-shaped domains</strong>. Each step keeps its own number of angular points. Regions where the energy is too high for the reaction to live are simply not stored. The wavepacket still sees a continuous physics; the computer sees a staircase.</p>
    <figure class="figure" style="background:#000">
      <img src="/assets/img/figures/wave-packet.gif" alt="Animated quantum wave packet">
      <figcaption class="caption">A time-dependent wavepacket from the related Schrödinger solvers in <a href="https://github.com/FlowDat/schrod">FlowDat/schrod</a>.</figcaption>
    </figure>
    <h2>Reactions, and the saving</h2>
    <p>On F + HCl the stair grid cut the mesh by about 18% against the usual method, with results matching established techniques. O + O₂ saved nearly 30%. Cl + H₂ more than 33%. The 2024 <em>Theoretical Chemistry Accounts</em> paper then takes the same idea to product state-resolved probabilities, including long-lived resonances that stretch over long-range grids — the regime where a naïve time-dependent method usually fails.</p>
    <p>This is the molecular counterpart of the 3DS story: do not pay for points that do not carry the physics.</p>
    """,
)

CASE_PARTICLES = case(
    "Turbulent dispersion",
    "Inertial particle-pair diffusion",
    "How massive particles, not tracers, separate in a turbulent flow — and what that means for pollen, sand, and industrial aerosols.",
    "/assets/img/work-particles.jpg",
    "Inertial particles in a turbulent flow",
    """
    <div><dt>Thesis</dt><dd>KFUPM Ph.D., 2019 — kinematic simulation of inertial particle-pair diffusion</dd></div>
    <div><dt>Talks</dt><dd>AMMCS 2017 · EGU 2017</dd></div>
    <div><dt>With</dt><dd>Nadeem A. Malik</dd></div>
    <div><dt>Method</dt><dd>Kinematic simulation (KS)</dd></div>
    """,
    r"""
    <p>Tracers follow the fluid. Inertial particles do not. Their Stokes number decides whether they ride eddies or cut through them, and pair dispersion — how two particles forget each other — changes accordingly. Richardson’s 1926 locality picture is the textbook; a non-local theory of pair diffusion, developed with Nadeem Malik, is the alternative we tested.</p>
    <p><strong>Kinematic simulation</strong> builds a synthetic turbulence that is cheap enough to track millions of pairs, yet rich enough in scales to distinguish local from non-local spreading. Low-St particles behave like dyes. High-St particles filter the small eddies and remember ballistic stretches. The applications are not abstract: pollen in a canopy, sand in a haboob, droplets in a spray, catalysts in a reactor.</p>
    <p>This half of the KFUPM dissertation sits beside the 3DS DNS. One chapter asks how to generate turbulence. The other asks how matter, once released, occupies it.</p>
    """,
)

CASE_WIND = case(
    "Wind energy · Reduced-order modelling",
    "Turbine blades, flow control, and POD",
    "Larger rotors capture more power and carry more load. Blade-resolved CFD, flow-control devices, and a POD/ROM stack are how those loads get designed rather than endured.",
    "/assets/img/work-wind.jpg",
    "Wind turbine blade with streamlines",
    """
    <div><dt>Code</dt><dd><a href="https://github.com/FlowDat/Blade_pod">github.com/FlowDat/Blade_pod</a></dd></div>
    <div><dt>Methods</dt><dd>CFD · POD · ML-ROM · SST</dd></div>
    <div><dt>Focus</dt><dd>Aerodynamics, loads, noise, transition</dd></div>
    """,
    r"""
    <p>Rotor diameter has grown faster than the materials that have to live with it. Flow-control devices — vortex generators, trailing-edge flaps, active blowing — exist to keep the boundary layer attached, to move transition, and to cut unsteady loads. None of that is visible without a blade-resolved CFD campaign.</p>
    <p>I use RANS (typically SST k–ω and its transition variants) for design sweeps, and proper orthogonal decomposition to compress the near-blade field into a reduced-order model. The <strong>Blade_pod</strong> repository is that ROM experiment: KOSST is a solid turbulence closure; a well-built ROM is what you actually iterate with.</p>
    <p>The same toolkit applies to vertical-axis machines with dynamic pitching, and to the quieter question of whether a device that helps power also helps fatigue.</p>
    """,
)

CASE_BATTERY = case(
    "Energy storage · Safety",
    "Multiscale battery thermal management",
    "A lithium-ion pack fails thermally at the cell, the module, and the chemistry at once. The diagnosis has to as well.",
    "/assets/img/work-battery.jpg",
    "Battery pack with thermal field",
    """
    <div><dt>Methods</dt><dd>CFD heat transfer · computational chemistry · multiscale entropy</dd></div>
    <div><dt>Aim</dt><dd>Early detection of thermal runaway</dd></div>
    """,
    r"""
    <p>Battery thermal management is not only a cooling problem. Thermal runaway is a chemical cascade that CFD alone cannot see and that a 0D equivalent-circuit model will not locate in a pack. The useful picture is multiscale: computational fluid dynamics for the coolant and the cell-to-cell coupling; computational chemistry for the reactions that start the runaway; data-driven diagnostics (modified multiscale entropy on temperature traces) for the pattern that says the pack is leaving the safe manifold.</p>
    <p>I treat BTMS the way I treat combustion chambers: a flow, a reaction, and a prognosis. The industrial stake is obvious — electric vehicles, grid storage, and any chemistry that would rather not become a fire.</p>
    """,
)

CASE_RES = case(
    "Subsurface flow · OpenFOAM",
    "Reservoir simulation",
    "From mixing in a pipe to saturations in a reservoir: OpenFOAM cases for multiphase subsurface flow, well control, and parallel runs.",
    "/assets/img/work-reservoir.jpg",
    "Subsurface reservoir saturations",
    """
    <div><dt>Code</dt><dd><a href="https://github.com/FlowDat/Reservoir">github.com/FlowDat/Reservoir</a></dd></div>
    <div><dt>Also</dt><dd><a href="https://github.com/FlowDat/3DSPipe">3DSPipe</a> — mixing, CoV versus Reynolds number</dd></div>
    <div><dt>Stack</dt><dd>OpenFOAM · blockMesh · parallel I/O</dd></div>
    """,
    r"""
    <p>KFUPM sits on hydrocarbon engineering; DICP sits on chemical physics. Reservoir simulation is where those habits meet: Darcy-scale transport, wells as internal boundary conditions, saturations that must be conservative. The <strong>Reservoir</strong> repository is a set of OpenFOAM tutorials I use for teaching and for my own case templates — basic single-phase setup, multiphase and well control, then domain decomposition and parallel I/O.</p>
    <figure class="figure paper">
      <img src="/assets/img/figures/cov-re.png" alt="Coefficient of variation versus Reynolds number at several downstream stations">
      <figcaption class="caption">Mixing quality (CoV) versus Reynolds number at successive downstream stations, from the 3DSPipe campaign — the same conservation mindset, in a pipe instead of a reservoir.</figcaption>
    </figure>
    <p>Related industrial CFD from the KFUPM years covers static mixers, wellbores and wellheads, reduction cells, heat exchangers, and rotating machinery. The repository is the part I can show; the method is the part I take to the next field.</p>
    """,
)

CASE_HT = case(
    "Software · Digital twins",
    "HydroTwin Studio",
    "The physics of CFD is hard. The workflow is harder. HydroTwin is a desktop layer that keeps the solver and hides the obstacle course.",
    "/assets/img/work-hydrotwin.jpg",
    "Holographic digital twin of a fluid experiment",
    """
    <div><dt>Status</dt><dd>In development</dd></div>
    <div><dt>Related</dt><dd><a href="/work/spectre.html">SPECTRE</a> · OpenFOAM cases · SMLG</dd></div>
    """,
    r"""
    <p>Anyone who has taught OpenFOAM has watched a capable student drown in dictionaries, meshes, and log files. The Navier–Stokes part was never the whole problem. HydroTwin Studio is my answer: a desktop environment for interactive CFD that still talks to real solvers underneath.</p>
    <p>The scientific backbone is the same work as this site — 3DS grids, mixing layers, SPECTRE as a fast twin of DNS, reservoir and blade cases as the industrial end. The product question is narrower: can a researcher change a blockage ratio, a Stokes number, or a blade pitch and see a trustworthy field without spending the afternoon on <code>fvSchemes</code>?</p>
    <p>It is not finished. It is the direction of travel.</p>
    """,
)

PUBS = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Writing</p>
    <h1>Publications.</h1>
    <p class="lead">Selected papers, proceedings, and manuscripts. Google Scholar and ORCID carry the archival record; this list follows the CV.</p>
    <div class="contact-row">
      <a class="btn btn-ghost" href="https://scholar.google.com/citations?user=XrRe2kkAAAAJ">Google Scholar</a>
      <a class="btn btn-ghost" href="https://orcid.org/0000-0002-8181-4369">ORCID</a>
      <a class="btn btn-ghost" href="https://www.researchgate.net/profile/Syed-Usama">ResearchGate</a>
    </div>
  </div>
</section>
<section style="padding-bottom:5rem">
  <div class="wrap">
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Well-posedness diagnostics and staged numerical solution of MHD buoyant flow over a bi-axially stretching surface with Cattaneo–Christov thermal relaxation</h3>
        <p class="authors">S. M. Usama, M. A. Tahir, U. Umer, Z. Sun</p>
        <p class="venue"><em>Scientific Reports</em> (Nature), 2026</p>
      </div>
      <div class="pub-side"><span class="badge badge-review">Under review</span></div>
    </article>
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Scale-separated, physics constrained, deep neural network for turbulent mixing layer simulations</h3>
        <p class="authors">S. M. Usama, N. A. Malik, M. Z. Akhter, U. Umer, Z. Sun</p>
        <p class="venue"><em>Results in Engineering</em>, 2026 · model &amp; data: <a href="https://github.com/FlowDat/SMLG">SPECTRE / SMLG</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-review">Under review</span></div>
    </article>
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Burst buffer accelerated direct numerical simulation of turbulence generated by 3D sparse multiscale grids</h3>
        <p class="authors">S. M. Usama, N. A. Malik, U. Umer, A. Shaikh, Z. Sun</p>
        <p class="venue"><em>Computers &amp; Fluids</em> 308, 106985 · <a href="https://doi.org/10.1016/j.compfluid.2026.106985">doi:10.1016/j.compfluid.2026.106985</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Published</span></div>
    </article>
    <article class="pub">
      <div class="year">2024</div>
      <div>
        <h3>Product state-resolved reactive scattering calculations using stair-shaped grids in hyperspherical coordinates for the quantum wave packet method</h3>
        <p class="authors">U. Umer, S. M. Usama, H. Zhao, Z. Sun</p>
        <p class="venue"><em>Theoretical Chemistry Accounts</em> 143, 61 · <a href="https://doi.org/10.1007/s00214-024-03133-w">doi:10.1007/s00214-024-03133-w</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Published</span></div>
    </article>
    <article class="pub">
      <div class="year">2024</div>
      <div>
        <h3>A time-dependent quantum wavepacket method on stair-shaped grids for reactive scattering using the hyperspherical coordinates</h3>
        <p class="authors">U. Umer, S. K. Usman, S. M. Usama, H. Zhao, Z. Sun</p>
        <p class="venue"><em>Chemical Physics Letters</em> 837, 141060 · <a href="https://doi.org/10.1016/j.cplett.2023.141060">doi:10.1016/j.cplett.2023.141060</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Published</span></div>
    </article>
    <article class="pub">
      <div class="year">2019</div>
      <div>
        <h3>A comparison of turbulence generated by 3DS sparse grids with different blockage ratios and different co-frame arrangements</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue">AMMCS / <em>Recent Developments in Mathematical, Statistical and Computational Sciences</em>, 2021</p>
      </div>
      <div class="pub-side"><span class="badge">Proceedings</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Turbulence behind 3D multi-scale sparse grids</h3>
        <p class="authors">S. M. Usama, J. Tellez-Alvarez, J. Kopec, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue"><em>J. Phys.: Conf. Series</em> 1101, 012048 · <a href="https://doi.org/10.1088/1742-6596/1101/1/012048">doi:10.1088/1742-6596/1101/1/012048</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Open access</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Fractal intermittent wakes in a wind tunnel</h3>
        <p class="authors">J. M. Redondo, J. Tellez, J. Kopec, K. Kwiatkowski, P. Lopez, M. Tijera, S. Strihjak, N. Malik, O. B. Mahjoub, S. M. Usama</p>
        <p class="venue"><em>Topical Problems of Fluid Mechanics</em>, 2018</p>
      </div>
      <div class="pub-side"><span class="badge">Proceedings</span></div>
    </article>
    <article class="pub">
      <div class="year">2017</div>
      <div>
        <h3>Mixing in 3D sparse multi-scale grid generated turbulence</h3>
        <p class="authors">S. M. Usama, J. Kopec, J. Tellez, K. Kwiatkowski, J. Redondo, N. Malik</p>
        <p class="venue">EGU General Assembly, 2017</p>
      </div>
      <div class="pub-side"><span class="badge">Abstract</span></div>
    </article>
    <article class="pub">
      <div class="year">2017</div>
      <div>
        <h3>Turbulent diffusion of inertial particle pairs such as in pollen and sandstorms</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue">AMMCS, Waterloo · EGU 2017 (poster)</p>
      </div>
      <div class="pub-side"><span class="badge">Talk / poster</span></div>
    </article>
    <article class="pub">
      <div class="year">2019</div>
      <div>
        <h3>Direct numerical simulation of 3D sparse multiscale grid generated turbulence and kinematic simulation of inertial particle pair diffusion</h3>
        <p class="authors">S. M. Usama</p>
        <p class="venue">Ph.D. dissertation, King Fahd University of Petroleum and Minerals · <a href="https://eprints.kfupm.edu.sa/140958/">eprints.kfupm.edu.sa/140958</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Thesis</span></div>
    </article>
  </div>
</section>
"""

ABOUT = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Biography</p>
    <h1>About.</h1>
    <p class="lead">Syed Muhammad Usama is a computational scientist at the Dalian Institute of Chemical Physics, Chinese Academy of Sciences. Ph.D. in mathematics, KFUPM. Principal Scientist, 2023.</p>
    <div class="contact-row">
      <a class="btn btn-solid" href="/assets/cv.pdf">Download CV (PDF)</a>
      <a class="btn btn-ghost" href="mailto:usama@dicp.ac.cn">Email</a>
    </div>
  </div>
</section>

<section class="section" style="border-top:0;padding-top:0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem">
    <div class="prose">
      <p>I work where fluids mix and molecules react: direct numerical simulation of turbulence, kinematic simulation of inertial particles, quantum wavepackets for triatomic scattering, and physics-constrained learning that makes those simulations cheaper to live with.</p>
      <p>The current home is the <strong>State Key Laboratory of Molecular Reaction Dynamics</strong> and the Center for Theoretical and Computational Chemistry at DICP in Dalian — Nature Index rank 1 worldwide. I arrived in 2019 as a Young International Talent, was named Principal Scientist in 2023, and continue as a research scientist on NSFC-supported work.</p>
      <p>Before China I spent five years at <strong>KFUPM</strong> in Dhahran as Lecturer-B and R&amp;D specialist: industrial CFD for mixers, wellbores, heat exchangers and reservoirs, plus the Ph.D. that became the 3DS and particle-pair programme. The Almarai Best Thesis Award (2019) and a first-prize research prize (2018) came out of that period, as did an EUHIT exchange at the Max Planck Institute and an HPC/AI allocation at KAUST.</p>
      <p>Still earlier I lectured at <strong>COMSATS University Islamabad</strong> (2010–2014), after an M.S. and B.S. in mathematics there. Teaching has never been a side job: distinctive recognition as a TA at KFUPM, a data-science trainer, a COMSATS faculty-development certificate, and a mathematics olympiad I helped run.</p>
    </div>
    <div>
      <p class="kicker">Research interests</p>
      <div class="methods" style="margin-bottom:2rem">
        <span>Fluid dynamics &amp; HPC</span>
        <span>Mathematical methods in molecular dynamics</span>
        <span>Combustion</span>
        <span>Efficient numerics for flow</span>
        <span>Scientific machine learning</span>
      </div>
      <p class="kicker">Coordinates</p>
      <div class="prose">
        <p>State Key Laboratory of Molecular Reaction Dynamics<br>Dalian Institute of Chemical Physics, CAS<br>116023 Dalian, China</p>
        <p><a href="mailto:usama@dicp.ac.cn">usama@dicp.ac.cn</a><br>
        <a href="mailto:usama784@gmail.com">usama784@gmail.com</a><br>
        ORCID <a href="https://orcid.org/0000-0002-8181-4369">0000-0002-8181-4369</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">Appointments</p>
    <h2 style="margin-bottom:1.4rem">Experience.</h2>
    <div class="timeline">
      <article class="tl">
        <div class="when">2025 — present</div>
        <div>
          <h3>Research Assistant / Computational Scientist</h3>
          <p class="org">Dalian Institute of Chemical Physics, Chinese Academy of Sciences</p>
          <p>Molecular reaction dynamics, DNS, quantum scattering, and physics-constrained learning. NSFC–RFIS-I project award, 2025.</p>
        </div>
      </article>
      <article class="tl">
        <div class="when">2019 — 2025</div>
        <div>
          <h3>Postdoctoral scientist</h3>
          <p class="org">DICP · Young International Talent (2019–23) · Tier-A International Scholar (2022–23)</p>
          <p>Multidisciplinary research in the State Key Laboratory of Molecular Reaction Dynamics. Principal Scientist, 2023. Research mentor certificate, 2024.</p>
        </div>
      </article>
      <article class="tl">
        <div class="when">2014 — 2019</div>
        <div>
          <h3>Lecturer-B &amp; R&amp;D specialist</h3>
          <p class="org">King Fahd University of Petroleum and Minerals, Dhahran</p>
          <p>Industrial CFD and FEA: static mixers, multiscale grids, wellbores, vehicles, particles, electrochemical processes. Taught; trained data science and machine learning (2016–17).</p>
        </div>
      </article>
      <article class="tl">
        <div class="when">2010 — 2014</div>
        <div>
          <h3>Lecturer / associate researcher</h3>
          <p class="org">COMSATS University Islamabad</p>
          <p>Numerical methods for flow and optimization; industrial mechanical-design problems; faculty development and the COMSATS Mathematics Olympiad.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">Degrees</p>
    <h2 style="margin-bottom:1.4rem">Education.</h2>
    <div class="timeline">
      <article class="tl">
        <div class="when">2014 — 2018</div>
        <div>
          <h3>Ph.D. Mathematics</h3>
          <p class="org">King Fahd University of Petroleum and Minerals · QS ~69 worldwide</p>
          <p>Dissertation: <em>Direct Numerical Simulation of 3D Sparse Multiscale Grid Generated Turbulence and Kinematic Simulation of Inertial Particle Pair Diffusion.</em> Almarai Best Thesis Award, 2019.</p>
        </div>
      </article>
      <article class="tl">
        <div class="when">2008 — 2010</div>
        <div>
          <h3>M.S. Mathematics</h3>
          <p class="org">COMSATS University Islamabad</p>
        </div>
      </article>
      <article class="tl">
        <div class="when">2004 — 2008</div>
        <div>
          <h3>B.S. Mathematics</h3>
          <p class="org">COMSATS University Islamabad</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="num">Recognition</p>
    <div class="section-head"><h2>Honors, awards, grants.</h2></div>
    <div class="honors">
      <div class="honor"><b>Principal Scientist</b><span>DICP–Chinese Academy of Sciences, 2023</span></div>
      <div class="honor"><b>Young International Talent</b><span>Multidisciplinary research, DICP–CAS, 2019–23</span></div>
      <div class="honor"><b>Tier-A International Scholar</b><span>International Talent Program, CAS, 2022–23</span></div>
      <div class="honor"><b>Almarai Best Thesis Award</b><span>KFUPM, 2019</span></div>
      <div class="honor"><b>NSFC–RFIS-I Project Award</b><span>Chinese Academy of Sciences, 2025</span></div>
      <div class="honor"><b>Research &amp; Innovation Award, first prize</b><span>Interdepartmental competition, KFUPM, 2018</span></div>
      <div class="honor"><b>National Natural Science Foundation Grant</b><span>China, 2022</span></div>
      <div class="honor"><b>International Scholars Funding</b><span>DICP–CAS, 2020</span></div>
      <div class="honor"><b>EUHIT Research Exchange</b><span>Max Planck Institute, 2018</span></div>
      <div class="honor"><b>HPC and artificial intelligence allocation</b><span>KAUST, 2017</span></div>
      <div class="honor"><b>NSTIP Research Grant</b><span>KFUPM, 2016</span></div>
      <div class="honor"><b>DSR Student Grant</b><span>KFUPM, 2015</span></div>
    </div>
  </div>
</section>
"""

CODES = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Open science</p>
    <h1>Codes.</h1>
    <p class="lead">Public repositories under <a href="https://github.com/FlowDat">github.com/FlowDat</a>. MATLAB, C++, Python, OpenFOAM. Data for SPECTRE lives on Zenodo.</p>
  </div>
</section>
<section style="padding-bottom:5rem">
  <div class="wrap grid-3">
    <a class="code-card" href="https://github.com/FlowDat/3DS">
      <span class="lang">MATLAB</span>
      <h3>3DS</h3>
      <p>Sparse 3D multiscale grid geometries and companion results for the burst-buffer DNS paper. 15% blockage cases, compared with 2D fractal grids.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/SMLG">
      <span class="lang">Python</span>
      <h3>SMLG / SPECTRE</h3>
      <p>Scale-aware digital twin of turbulence. Analysis scripts for mixing-layer DNS at seven Reynolds numbers. Data: Zenodo 21234013.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/3DSPipe">
      <span class="lang">C++ · OpenFOAM</span>
      <h3>3DSPipe</h3>
      <p>Mixing in a pipe: STL geometries, system dictionaries, coefficient-of-variation versus Reynolds number.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/Blade_pod">
      <span class="lang">C++</span>
      <h3>Blade_pod</h3>
      <p>POD / machine-learning reduced-order model of a wind-turbine blade flow.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/Reservoir">
      <span class="lang">C++ · OpenFOAM</span>
      <h3>Reservoir</h3>
      <p>Tutorial cases for reservoir simulation: grid and wells, multiphase control, parallel scaling.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/schrod">
      <span class="lang">MATLAB</span>
      <h3>schrod</h3>
      <p>1D time-dependent Schrödinger solvers for different potentials, masses, and reaction-inspired domains.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/phaseChangeCondEvapHeat">
      <span class="lang">C++</span>
      <h3>phaseChangeCondEvapHeat</h3>
      <p>Phase-change, condensation, evaporation, and heat-transfer cases.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/contina">
      <span class="lang">Python</span>
      <h3>contina</h3>
      <p>Continuum / visualization experiments — mean profiles, wavepackets, and geometry studies.</p>
    </a>
  </div>
</section>
"""

LOST = r"""
<section class="lost">
  <div>
    <p class="kicker">404</p>
    <h1>This streamline left the domain.</h1>
    <p class="lead" style="margin-inline:auto">The page is not in the mesh. Try the work, the papers, or home.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-solid" href="/">Home</a>
      <a class="btn btn-ghost" href="/work.html">Work</a>
    </div>
  </div>
</section>
"""

ABOUT_FIX = ABOUT.replace(
    'style="display:grid;grid-template-columns:1fr 1fr;gap:3rem"',
    'class="now"',
)

page(
    "/index.html",
    "Syed Muhammad Usama — Flowdat",
    "Computational scientist at DICP–CAS. DNS of 3D sparse grids, quantum reactive scattering, and physics-constrained turbulence learning.",
    HOME,
    "home",
    JSONLD,
)
page("/work.html", "Work — Syed Muhammad Usama", "Research and applied CFD: 3DS DNS, SPECTRE, quantum scattering, particles, wind, batteries, reservoirs.", WORK, "work")
page("/work/3ds.html", "3D sparse-grid DNS — Usama", "Burst-buffer accelerated DNS of turbulence generated by 3D sparse multiscale grids.", CASE_3DS, "work")
page("/work/spectre.html", "SPECTRE — Usama", "Scale-aware deep-learning emulator of turbulent mixing layers.", CASE_SPECTRE, "work")
page("/work/quantum.html", "Stair-shaped grids — Usama", "Quantum wavepacket reactive scattering on stair-shaped hyperspherical grids.", CASE_QUANTUM, "work")
page("/work/particles.html", "Inertial particle pairs — Usama", "Kinematic simulation of inertial particle-pair diffusion.", CASE_PARTICLES, "work")
page("/work/wind.html", "Wind turbine blades — Usama", "Blade-resolved CFD, flow control, and POD reduced-order models.", CASE_WIND, "work")
page("/work/battery.html", "Battery thermal management — Usama", "Multiscale CFD and chemistry for lithium-ion thermal runaway.", CASE_BATTERY, "work")
page("/work/reservoir.html", "Reservoir simulation — Usama", "OpenFOAM reservoir and mixing cases.", CASE_RES, "work")
page("/work/hydrotwin.html", "HydroTwin Studio — Usama", "A desktop environment for interactive CFD.", CASE_HT, "work")
page("/publications.html", "Publications — Syed Muhammad Usama", "Papers on 3DS turbulence, burst-buffer DNS, quantum scattering, and mixing-layer learning.", PUBS, "papers")
page("/about.html", "About — Syed Muhammad Usama", "Computational scientist at DICP, Chinese Academy of Sciences. Ph.D. KFUPM. Principal Scientist, 2023.", ABOUT_FIX, "about")
page("/codes.html", "Codes — Flowdat", "Open repositories for 3DS, SPECTRE, OpenFOAM, Schrödinger solvers, and blade ROMs.", CODES, "codes")
page("/404.html", "Page not found — Flowdat", "The page is not in the mesh.", LOST, "")

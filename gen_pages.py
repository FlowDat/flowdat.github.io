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
      <a href="/" data-page="home">Archive</a>
      <a href="/papers.html" data-page="papers">Papers</a>
      <a href="/codes.html" data-page="codes">Codes</a>
      <a href="/plots.html" data-page="plots">Plots</a>
      <a href="/notes.html" data-page="notes">Notes</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="brand-foot">Flowdat</p>
      <p>Research archive: turbulence, mixing, molecular reaction, scientific computing. Papers, codes, figures. 2017–2026.</p>
    </div>
    <div>
      <p class="kicker">Correspondence</p>
      <div class="foot-list">
        <a href="mailto:usama@dicp.ac.cn">usama@dicp.ac.cn</a>
      </div>
    </div>
    <div>
      <p class="kicker">Records</p>
      <div class="foot-list">
        <a href="https://orcid.org/0000-0002-8181-4369">ORCID</a>
        <a href="https://scholar.google.com/citations?user=XrRe2kkAAAAJ">Google Scholar</a>
        <a href="https://github.com/FlowDat">GitHub</a>
        <a href="https://www.researchgate.net/profile/Syed-Usama">ResearchGate</a>
        <a href="https://www.linkedin.com/in/syedusama8386/">LinkedIn</a>
      </div>
    </div>
  </div>
  <p class="colophon"><span>© <span id="year">2026</span> Flowdat</span><span>Computational research archive</span></p>
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
  "@type": "Collection",
  "name": "Flowdat research archive",
  "url": "https://flowdat.github.io/",
  "creator": {
    "@type": "Person",
    "name": "Syed Muhammad Usama",
    "url": "https://flowdat.github.io/",
    "email": "usama@dicp.ac.cn",
    "sameAs": [
      "https://orcid.org/0000-0002-8181-4369",
      "https://scholar.google.com/citations?user=XrRe2kkAAAAJ",
      "https://github.com/FlowDat",
      "https://www.researchgate.net/profile/Syed-Usama"
    ]
  }
}
</script>
"""

HOME = r"""
<section class="hero">
  <canvas id="flow" aria-hidden="true"></canvas>
  <div class="hero-inner">
    <p class="kicker">Research archive · 2017–2026</p>
    <h1>Flowdat.</h1>
    <p class="lead">A chronological record of computational research in grid-generated turbulence, inertial particle diffusion, quantum reactive scattering, and physics-constrained learning — papers, codes, and figures.</p>
    <div class="hero-actions">
      <a class="btn btn-solid" href="#chronicle">Chronicle</a>
      <a class="btn btn-ghost" href="/papers.html">Bibliography</a>
      <a class="btn btn-ghost" href="/plots.html">Figures</a>
    </div>
    <div class="year-nav">
      <a href="#y2026">2026</a>
      <a href="#y2025">2025</a>
      <a href="#y2024">2024</a>
      <a href="#y2021">2021</a>
      <a href="#y2019">2019</a>
      <a href="#y2018">2018</a>
      <a href="#y2017">2017</a>
    </div>
  </div>
  <ul class="hero-stats">
    <li><b>17</b><span>Papers, proceedings, and manuscripts</span></li>
    <li><b>8</b><span>Public codes (MATLAB, C++, Python, OpenFOAM)</span></li>
    <li><b>DNS · QMD · ROM</b><span>Burst buffers, stair grids, SPECTRE</span></li>
    <li><b>2017—2026</b><span>Record ordered by year</span></li>
  </ul>
</section>

<section class="section" id="chronicle">
  <div class="wrap">
    <p class="num">Chronicle</p>
    <div class="section-head">
      <h2>Work in time.</h2>
      <p>Newest first. Each year lists the papers, codes, and figures attached to that interval.</p>
    </div>

    <div class="entry" id="y2026">
      <div class="yr">2026</div>
      <div class="stack">
        <h2>Burst-buffer DNS, mixing-layer emulation, MHD diagnostics.</h2>
        <article>
          <h3>Burst buffer accelerated direct numerical simulation of turbulence generated by 3D sparse multiscale grids</h3>
          <p>S. M. Usama, N. A. Malik, U. Umer, A. Shaikh, Z. Sun. <em>Computers &amp; Fluids</em> 308, 106985. BBDSA: fivefold wall-time reduction, eightfold parallel efficiency. 3DSG at 24% blockage matches denser classical and fractal grids at Re = 4000. <a href="https://doi.org/10.1016/j.compfluid.2026.106985">doi:10.1016/j.compfluid.2026.106985</a> · <a href="/notes/grid-turbulence.html">note</a></p>
        </article>
        <article>
          <h3>Scale-separated, physics constrained, deep neural network for turbulent mixing layer simulations (SPECTRE)</h3>
          <p>S. M. Usama, N. A. Malik, M. Z. Akhter, U. Umer, Z. Sun. <em>Results in Engineering</em>, under review. DNS mixing layers at Re 2,500–30,000. Data: <a href="https://zenodo.org/records/21234013">Zenodo 21234013</a> · code: <a href="https://github.com/FlowDat/SMLG">SMLG</a> · <a href="/notes/spectre.html">note</a></p>
        </article>
        <article>
          <h3>Well-posedness diagnostics and staged numerical solution of MHD buoyant flow over a bi-axially stretching surface with Cattaneo–Christov thermal relaxation</h3>
          <p>S. M. Usama, M. A. Tahir, U. Umer, Z. Sun. <em>Scientific Reports</em>, under review.</p>
        </article>
        <div class="plot-grid">
          <figure>
            <img src="/assets/img/figures/turb36.png" alt="DNS vorticity isosurfaces">
            <figcaption>DNS vorticity volume — the I/O load BBDSA is built to absorb.</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/figures/figure01_global_error_benchmark.jpg" alt="SPECTRE global error versus Reynolds number">
            <figcaption>SPECTRE global reconstruction error versus Reynolds number.</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/figures/figure13_mixing_performance.jpg" alt="Mixing performance metrics">
            <figcaption>Mixing-layer performance metrics from the SPECTRE analysis stack.</figcaption>
          </figure>
        </div>
      </div>
    </div>

    <div class="entry" id="y2025">
      <div class="yr">2025</div>
      <div class="stack">
        <h2>Codes, twins, OpenFOAM cases.</h2>
        <article>
          <h3>SMLG — scale-aware digital twin of turbulence</h3>
          <p>Public analysis stack for SPECTRE. Seven Reynolds-number DNS files, reconstruction, stresses, spectra, coherent structures. <a href="https://github.com/FlowDat/SMLG">github.com/FlowDat/SMLG</a></p>
        </article>
        <article>
          <h3>phaseChangeCondEvapHeat</h3>
          <p>OpenFOAM cases for condensation, evaporation, and heat transfer. <a href="https://github.com/FlowDat/phaseChangeCondEvapHeat">repository</a></p>
        </article>
        <article>
          <h3>HydroTwin Studio</h3>
          <p>Desktop development for interactive CFD over existing solvers — case setup, mesh, post-processing. <a href="/notes/hydrotwin.html">note</a></p>
        </article>
        <article>
          <h3>OpenFOAM Rayleigh–Taylor</h3>
          <p>interFoam VOF, 128 × 512 structured mesh, Atwood-number RTI: linear growth, mushroom caps, secondary Kelvin–Helmholtz roll-ups.</p>
        </article>
        <div class="plot-grid">
          <figure>
            <img src="/assets/img/figures/figure08_coherent_structures.jpg" alt="Coherent structures in a mixing layer">
            <figcaption>Coherent structures, SPECTRE versus DNS.</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/figures/figure06_turbulent_intensities.jpg" alt="Turbulent intensity profiles">
            <figcaption>Turbulent intensities across the mixing layer.</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/figures/figure10_spectral_comparison.jpg" alt="Spectral comparison">
            <figcaption>Spectral comparison of emulator and DNS.</figcaption>
          </figure>
        </div>
      </div>
    </div>

    <div class="entry" id="y2024">
      <div class="yr">2024</div>
      <div class="stack">
        <h2>Stair-shaped grids for quantum reactive scattering.</h2>
        <article>
          <h3>A time-dependent quantum wavepacket method on stair-shaped grids for reactive scattering using the hyperspherical coordinates</h3>
          <p>U. Umer, S. K. Usman, S. M. Usama, H. Zhao, Z. Sun. <em>Chemical Physics Letters</em> 837, 141060. Grid reductions: F+HCl ~18%, O+O₂ ~30%, Cl+H₂ &gt;33%. <a href="https://doi.org/10.1016/j.cplett.2023.141060">doi:10.1016/j.cplett.2023.141060</a> · <a href="/notes/quantum.html">note</a></p>
        </article>
        <article>
          <h3>Product state-resolved reactive scattering calculations using stair-shaped grids in hyperspherical coordinates for the quantum wave packet method</h3>
          <p>U. Umer, S. M. Usama, H. Zhao, Z. Sun. <em>Theoretical Chemistry Accounts</em> 143, 61. Long-lived resonances on long-range grids; comparison with RCB and IARD. <a href="https://doi.org/10.1007/s00214-024-03133-w">doi:10.1007/s00214-024-03133-w</a></p>
        </article>
        <div class="plot-grid two">
          <figure>
            <img src="/assets/img/figures/wave-packet.gif" alt="Time-dependent wave packet">
            <figcaption>Time-dependent wavepacket, Schrödinger solvers (<a href="https://github.com/FlowDat/schrod">schrod</a>).</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/work-quantum.jpg" alt="Stair-shaped computational domains">
            <figcaption>Stair-shaped hyper-radial domains for reactive scattering.</figcaption>
          </figure>
        </div>
      </div>
    </div>

    <div class="entry" id="y2021">
      <div class="yr">2021</div>
      <div class="stack">
        <h2>3DS parameter space, blockage, co-frames.</h2>
        <article>
          <h3>A comparison of turbulence generated by 3DS sparse grids with different blockage ratios and different co-frame arrangements</h3>
          <p>S. M. Usama, N. A. Malik. <em>Recent Developments in Mathematical, Statistical and Computational Sciences</em>, 2021 (AMMCS 2019 contribution).</p>
        </article>
      </div>
    </div>

    <div class="entry" id="y2019">
      <div class="yr">2019</div>
      <div class="stack">
        <h2>Dissertation record: 3DS DNS and kinematic pair diffusion.</h2>
        <article>
          <h3>Direct numerical simulation of 3D sparse multiscale grid generated turbulence and kinematic simulation of inertial particle pair diffusion</h3>
          <p>S. M. Usama. Ph.D. dissertation, King Fahd University of Petroleum and Minerals. <a href="https://eprints.kfupm.edu.sa/140958/">eprints.kfupm.edu.sa/140958</a></p>
        </article>
        <article>
          <h3>AMMCS — 3DS blockage ratios and co-frame arrangements</h3>
          <p>Conference presentation of the 3DS parameter study later collected in the 2021 volume.</p>
        </article>
      </div>
    </div>

    <div class="entry" id="y2018">
      <div class="yr">2018</div>
      <div class="stack">
        <h2>Sparse grids, fractal wakes, kinematic pair diffusion.</h2>
        <article>
          <h3>Turbulence behind 3D multi-scale sparse grids</h3>
          <p>S. M. Usama, J. Tellez-Alvarez, J. Kopec, K. Kwiatkowski, J. M. Redondo, N. A. Malik. <em>J. Phys.: Conf. Series</em> 1101, 012048. Open access. <a href="https://doi.org/10.1088/1742-6596/1101/1/012048">doi:10.1088/1742-6596/1101/1/012048</a></p>
        </article>
        <article>
          <h3>Fractal intermittent wakes in a wind tunnel</h3>
          <p>J. M. Redondo, J. Tellez, J. Kopec, K. Kwiatkowski, P. Lopez, M. Tijera, S. Strihjak, N. Malik, O. B. Mahjoub, S. M. Usama. <em>Topical Problems of Fluid Mechanics</em>, 2018.</p>
        </article>
        <article>
          <h3>Turbulence characteristics generated by 3D sparse grids</h3>
          <p>S. M. Usama, J. M. Kopec, J. Tellez, K. Kwiatkowski, J. M. Redondo, N. A. Malik. ICEFM, 2018.</p>
        </article>
        <article>
          <h3>Turbulent pair diffusion of inertial particles using kinematic simulations</h3>
          <p>S. M. Usama, N. A. Malik. Locality versus non-locality for inertial pairs. <a href="/notes/particles.html">note</a></p>
        </article>
      </div>
    </div>

    <div class="entry" id="y2017">
      <div class="yr">2017</div>
      <div class="stack">
        <h2>First 3DS mixing results; inertial particle pairs.</h2>
        <article>
          <h3>Mixing in 3D sparse multi-scale grid generated turbulence</h3>
          <p>S. M. Usama, J. Kopec, J. Tellez, K. Kwiatkowski, J. Redondo, N. Malik. EGU General Assembly, 2017.</p>
        </article>
        <article>
          <h3>Turbulence generated by 3D sparse multi-scale grid</h3>
          <p>S. M. Usama, J. M. Kopec, J. Tellez, K. Kwiatkowski, J. M. Redondo, N. A. Malik. 2017.</p>
        </article>
        <article>
          <h3>Turbulent diffusion of inertial particle pairs such as in pollen and sandstorms</h3>
          <p>S. M. Usama, N. A. Malik. AMMCS, Waterloo, 2017 · EGU 2017 (poster).</p>
        </article>
        <div class="plot-grid two">
          <figure>
            <img src="/assets/img/work-3ds.jpg" alt="Sparse 3D multiscale grid">
            <figcaption>3D sparse multiscale grid and downstream wake.</figcaption>
          </figure>
          <figure>
            <img src="/assets/img/work-particles.jpg" alt="Inertial particle pairs">
            <figcaption>Inertial particle-pair diffusion in synthetic turbulence.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </div>
</section>
"""

PAPERS = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Bibliography</p>
    <h1>Papers.</h1>
    <p class="lead">Complete public record: journals, proceedings, dissertation, and manuscripts. Ordered newest first.</p>
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
        <h3>Burst buffer accelerated direct numerical simulation of turbulence generated by 3D sparse multiscale grids</h3>
        <p class="authors">S. M. Usama, N. A. Malik, U. Umer, A. Shaikh, Z. Sun</p>
        <p class="venue"><em>Computers &amp; Fluids</em> 308, 106985 · <a href="https://doi.org/10.1016/j.compfluid.2026.106985">10.1016/j.compfluid.2026.106985</a> · data <a href="https://github.com/FlowDat/3DS">FlowDat/3DS</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Journal</span></div>
    </article>
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Scale-separated, physics constrained, deep neural network for turbulent mixing layer simulations</h3>
        <p class="authors">S. M. Usama, N. A. Malik, M. Z. Akhter, U. Umer, Z. Sun</p>
        <p class="venue"><em>Results in Engineering</em> · SPECTRE / <a href="https://github.com/FlowDat/SMLG">SMLG</a> · <a href="https://zenodo.org/records/21234013">Zenodo 21234013</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-review">Under review</span></div>
    </article>
    <article class="pub">
      <div class="year">2026</div>
      <div>
        <h3>Well-posedness diagnostics and staged numerical solution of MHD buoyant flow over a bi-axially stretching surface with Cattaneo–Christov thermal relaxation</h3>
        <p class="authors">S. M. Usama, M. A. Tahir, U. Umer, Z. Sun</p>
        <p class="venue"><em>Scientific Reports</em></p>
      </div>
      <div class="pub-side"><span class="badge badge-review">Under review</span></div>
    </article>
    <article class="pub">
      <div class="year">2024</div>
      <div>
        <h3>Product state-resolved reactive scattering calculations using stair-shaped grids in hyperspherical coordinates for the quantum wave packet method</h3>
        <p class="authors">U. Umer, S. M. Usama, H. Zhao, Z. Sun</p>
        <p class="venue"><em>Theoretical Chemistry Accounts</em> 143, 61 · <a href="https://doi.org/10.1007/s00214-024-03133-w">10.1007/s00214-024-03133-w</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Journal</span></div>
    </article>
    <article class="pub">
      <div class="year">2024</div>
      <div>
        <h3>A time-dependent quantum wavepacket method on stair-shaped grids for reactive scattering using the hyperspherical coordinates</h3>
        <p class="authors">U. Umer, S. K. Usman, S. M. Usama, H. Zhao, Z. Sun</p>
        <p class="venue"><em>Chemical Physics Letters</em> 837, 141060 · <a href="https://doi.org/10.1016/j.cplett.2023.141060">10.1016/j.cplett.2023.141060</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Journal</span></div>
    </article>
    <article class="pub">
      <div class="year">2021</div>
      <div>
        <h3>A comparison of turbulence generated by 3DS sparse grids with different blockage ratios and different co-frame arrangements</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue"><em>Recent Developments in Mathematical, Statistical and Computational Sciences</em> (AMMCS 2019)</p>
      </div>
      <div class="pub-side"><span class="badge">Chapter</span></div>
    </article>
    <article class="pub">
      <div class="year">2019</div>
      <div>
        <h3>Direct numerical simulation of 3D sparse multiscale grid generated turbulence and kinematic simulation of inertial particle pair diffusion</h3>
        <p class="authors">S. M. Usama</p>
        <p class="venue">Ph.D. dissertation, KFUPM · <a href="https://eprints.kfupm.edu.sa/140958/">eprints.kfupm.edu.sa/140958</a> · PQDT-Global, 2019</p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Thesis</span></div>
    </article>
    <article class="pub">
      <div class="year">2019</div>
      <div>
        <h3>A comparison of turbulence generated by 3DS sparse grids with different blockage ratios and different co-frame arrangements</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue">AMMCS International Conference, 2019</p>
      </div>
      <div class="pub-side"><span class="badge">Talk</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Turbulence behind 3D multi-scale sparse grids</h3>
        <p class="authors">S. M. Usama, J. Tellez-Alvarez, J. Kopec, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue"><em>J. Phys.: Conf. Series</em> 1101, 012048 · <a href="https://doi.org/10.1088/1742-6596/1101/1/012048">10.1088/1742-6596/1101/1/012048</a></p>
      </div>
      <div class="pub-side"><span class="badge badge-live">Open access</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Fractal intermittent wakes in a wind tunnel</h3>
        <p class="authors">J. M. Redondo, J. Tellez, J. Kopec, K. Kwiatkowski, P. Lopez, M. Tijera, S. Strihjak, N. Malik, O. B. Mahjoub, S. M. Usama</p>
        <p class="venue"><em>Topical Problems of Fluid Mechanics</em>, 243–250</p>
      </div>
      <div class="pub-side"><span class="badge">Proceedings</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Turbulence characteristics generated by 3D sparse grids</h3>
        <p class="authors">S. M. Usama, J. M. Kopec, J. Tellez, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue">ICEFM, 2018</p>
      </div>
      <div class="pub-side"><span class="badge">Proceedings</span></div>
    </article>
    <article class="pub">
      <div class="year">2018</div>
      <div>
        <h3>Turbulent pair diffusion of inertial particles using kinematic simulations</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue">Manuscript / KS study of locality versus non-locality</p>
      </div>
      <div class="pub-side"><span class="badge">Note</span></div>
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
        <h3>Turbulence generated by 3D sparse multi-scale grid</h3>
        <p class="authors">S. M. Usama, J. M. Kopec, J. Tellez, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue">Conference contribution, 2017</p>
      </div>
      <div class="pub-side"><span class="badge">Talk</span></div>
    </article>
    <article class="pub">
      <div class="year">2017</div>
      <div>
        <h3>Turbulent diffusion of inertial particle pairs such as in pollen and sandstorms</h3>
        <p class="authors">S. M. Usama, N. A. Malik</p>
        <p class="venue">AMMCS, Waterloo, 20–25 August 2017</p>
      </div>
      <div class="pub-side"><span class="badge">Talk</span></div>
    </article>
    <article class="pub">
      <div class="year">2017</div>
      <div>
        <h3>Turbulent inertial particle pair diffusion</h3>
        <p class="authors">S. Usama, N. Malik</p>
        <p class="venue">EGU General Assembly, abstract 12517, 2017</p>
      </div>
      <div class="pub-side"><span class="badge">Poster</span></div>
    </article>
    <article class="pub">
      <div class="year">2017</div>
      <div>
        <h3>Mixing and turbulence generated by 3D sparse multi-scale grid</h3>
        <p class="authors">S. M. Usama, J. Kopeć, J. Tellez-Alvarez, K. Kwiatkowski, J. M. Redondo, N. A. Malik</p>
        <p class="venue">Presentation, 2017</p>
      </div>
      <div class="pub-side"><span class="badge">Talk</span></div>
    </article>
  </div>
</section>
"""

CODES = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Development</p>
    <h1>Codes.</h1>
    <p class="lead">Public repositories under <a href="https://github.com/FlowDat">github.com/FlowDat</a>. MATLAB, C++, Python, OpenFOAM. SPECTRE data on Zenodo.</p>
  </div>
</section>
<section style="padding-bottom:2rem">
  <div class="wrap grid-3">
    <a class="code-card" href="https://github.com/FlowDat/3DS">
      <span class="lang">MATLAB · 2019–2026</span>
      <h3>3DS</h3>
      <p>Sparse 3D multiscale grid geometries and companion results for burst-buffer DNS. 15% blockage cases versus 2D fractal grids.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/SMLG">
      <span class="lang">Python · 2025–2026</span>
      <h3>SMLG / SPECTRE</h3>
      <p>Scale-aware digital twin of turbulence. Analysis of mixing-layer DNS at seven Reynolds numbers. Zenodo 21234013.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/3DSPipe">
      <span class="lang">C++ · OpenFOAM</span>
      <h3>3DSPipe</h3>
      <p>Pipe mixing: STL geometries, system dictionaries, coefficient of variation versus Reynolds number and downstream station.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/Blade_pod">
      <span class="lang">C++</span>
      <h3>Blade_pod</h3>
      <p>POD / machine-learning reduced-order model of wind-turbine blade flow. SST versus ROM.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/Reservoir">
      <span class="lang">C++ · OpenFOAM</span>
      <h3>Reservoir</h3>
      <p>Reservoir simulation tutorials: grid and wells, multiphase control, domain decomposition, parallel I/O.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/schrod">
      <span class="lang">MATLAB</span>
      <h3>schrod</h3>
      <p>1D time-dependent Schrödinger solvers for different potentials, masses, and reaction-inspired domains.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/phaseChangeCondEvapHeat">
      <span class="lang">C++ · 2026</span>
      <h3>phaseChangeCondEvapHeat</h3>
      <p>Phase-change, condensation, evaporation, and heat-transfer cases.</p>
    </a>
    <a class="code-card" href="https://github.com/FlowDat/contina">
      <span class="lang">Python</span>
      <h3>contina</h3>
      <p>Continuum visualisation: mean profiles, wavepackets, coil geometry, mesh studies.</p>
    </a>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <p class="num">3DSPipe</p>
    <h2 style="margin-bottom:1rem">Mixing quality versus Reynolds number.</h2>
    <div class="plot-grid">
      <figure class="paper"><img src="/assets/img/figures/cov-re.png" alt="CoV versus Reynolds number"><figcaption>CoV vs Re at successive z stations.</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/cov.png" alt="Coefficient of variation"><figcaption>Coefficient of variation field.</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/cov23.png" alt="CoV slice"><figcaption>CoV, additional station.</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/cov31.png" alt="CoV slice"><figcaption>CoV, downstream station.</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/pipe-12.png" alt="Pipe mixing snapshot"><figcaption>Pipe mixing snapshot.</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/pipe-14.png" alt="Pipe mixing snapshot"><figcaption>Pipe mixing snapshot.</figcaption></figure>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <p class="num">contina</p>
    <h2 style="margin-bottom:1rem">Mean flow, geometry, wavepackets.</h2>
    <div class="plot-grid">
      <figure class="paper"><img src="/assets/img/figures/umean.png" alt="Mean velocity profile"><figcaption>Mean streamwise velocity U(y).</figcaption></figure>
      <figure><img src="/assets/img/figures/contina-orig.png" alt="Helical coil"><figcaption>Helical coil geometry.</figcaption></figure>
      <figure><img src="/assets/img/figures/wave-packet.gif" alt="Wave packet"><figcaption>Wavepacket evolution.</figcaption></figure>
      <figure><img src="/assets/img/figures/contina-44006.png" alt="Field visualisation"><figcaption>Field visualisation.</figcaption></figure>
      <figure><img src="/assets/img/figures/contina-4211.png" alt="Mesh / field"><figcaption>Mesh / field study.</figcaption></figure>
      <figure><img src="/assets/img/figures/contina-170616.png" alt="Contour"><figcaption>Contour.</figcaption></figure>
    </div>
  </div>
</section>
"""

PLOTS = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Figures</p>
    <h1>Plots.</h1>
    <p class="lead">DNS volumes, SPECTRE diagnostics, pipe-mixing CoV, wavepackets. Sourced from the public repositories.</p>
  </div>
</section>
<section class="section" style="border-top:0;padding-top:0">
  <div class="wrap">
    <p class="num">SPECTRE · SMLG</p>
    <h2 style="margin-bottom:1rem">Mixing-layer emulator versus DNS.</h2>
    <div class="plot-grid">
      <figure><img src="/assets/img/figures/figure01_global_error_benchmark.jpg" alt=""><figcaption>01 Global error vs Re</figcaption></figure>
      <figure><img src="/assets/img/figures/figure02_diagnostic_dashboard_Re2500.jpg" alt=""><figcaption>02 Dashboard Re 2500</figcaption></figure>
      <figure><img src="/assets/img/figures/figure02_diagnostic_dashboard_Re25000.jpg" alt=""><figcaption>02 Dashboard Re 25000</figcaption></figure>
      <figure><img src="/assets/img/figures/figure03_spectral_temporal_grid.jpg" alt=""><figcaption>03 Spectral–temporal grid</figcaption></figure>
      <figure><img src="/assets/img/figures/figure04_local_probe_validation.jpg" alt=""><figcaption>04 Local probe validation</figcaption></figure>
      <figure><img src="/assets/img/figures/figure05_mean_flow_profiles.jpg" alt=""><figcaption>05 Mean flow profiles</figcaption></figure>
      <figure><img src="/assets/img/figures/figure06_turbulent_intensities.jpg" alt=""><figcaption>06 Turbulent intensities</figcaption></figure>
      <figure><img src="/assets/img/figures/figure07_transport_stresses.jpg" alt=""><figcaption>07 Transport and stresses</figcaption></figure>
      <figure><img src="/assets/img/figures/figure08_coherent_structures.jpg" alt=""><figcaption>08 Coherent structures</figcaption></figure>
      <figure><img src="/assets/img/figures/figure09_layer_thickness_evolution.jpg" alt=""><figcaption>09 Layer thickness</figcaption></figure>
      <figure><img src="/assets/img/figures/figure10_spectral_comparison.jpg" alt=""><figcaption>10 Spectral comparison</figcaption></figure>
      <figure><img src="/assets/img/figures/figure11_strouhal_frequency.jpg" alt=""><figcaption>11 Strouhal frequency</figcaption></figure>
      <figure><img src="/assets/img/figures/figure12_validation_metrics.jpg" alt=""><figcaption>12 Validation metrics</figcaption></figure>
      <figure><img src="/assets/img/figures/figure13_mixing_performance.jpg" alt=""><figcaption>13 Mixing performance</figcaption></figure>
      <figure><img src="/assets/img/figures/figure14_detailed_comparison_x6.jpg" alt=""><figcaption>14 Detailed comparison x/δ</figcaption></figure>
      <figure><img src="/assets/img/figures/figure15_coherence_profiles.jpg" alt=""><figcaption>15 Coherence profiles</figcaption></figure>
      <figure><img src="/assets/img/figures/figure16_concentration_pdf.jpg" alt=""><figcaption>16 Concentration PDF</figcaption></figure>
      <figure><img src="/assets/img/figures/figure17_mean_flow_profiles_x5.jpg" alt=""><figcaption>17 Mean flow, station x5</figcaption></figure>
      <figure><img src="/assets/img/figures/figure18_turbulent_intensities_x5.jpg" alt=""><figcaption>18 Intensities, station x5</figcaption></figure>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <p class="num">DNS · mixing · quantum</p>
    <h2 style="margin-bottom:1rem">Volumes and laboratory figures.</h2>
    <div class="plot-grid">
      <figure><img src="/assets/img/figures/turb36.png" alt=""><figcaption>DNS vorticity isosurfaces</figcaption></figure>
      <figure class="paper"><img src="/assets/img/figures/cov-re.png" alt=""><figcaption>Pipe mixing CoV vs Re</figcaption></figure>
      <figure><img src="/assets/img/figures/wave-packet.gif" alt=""><figcaption>Quantum wavepacket</figcaption></figure>
      <figure><img src="/assets/img/work-3ds.jpg" alt=""><figcaption>3DS grid and wake</figcaption></figure>
      <figure><img src="/assets/img/work-spectre.jpg" alt=""><figcaption>Mixing layer / SPECTRE</figcaption></figure>
      <figure><img src="/assets/img/work-quantum.jpg" alt=""><figcaption>Stair-shaped domains</figcaption></figure>
      <figure><img src="/assets/img/work-particles.jpg" alt=""><figcaption>Inertial particle pairs</figcaption></figure>
      <figure><img src="/assets/img/work-wind.jpg" alt=""><figcaption>Blade flow control</figcaption></figure>
      <figure><img src="/assets/img/work-battery.jpg" alt=""><figcaption>Pack thermal field</figcaption></figure>
      <figure><img src="/assets/img/work-reservoir.jpg" alt=""><figcaption>Subsurface saturation</figcaption></figure>
      <figure><img src="/assets/img/work-hydrotwin.jpg" alt=""><figcaption>Interactive CFD twin</figcaption></figure>
      <figure><img src="/assets/img/figures/contina-orig.png" alt=""><figcaption>Helical coil</figcaption></figure>
    </div>
  </div>
</section>
"""

NOTES = r"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Research notes</p>
    <h1>Notes.</h1>
    <p class="lead">Technical write-ups of the computational work — methods, results, and the attached papers.</p>
    <div class="filters" role="tablist">
      <button data-filter="all" class="is-on">All</button>
      <button data-filter="turbulence">Turbulence</button>
      <button data-filter="quantum">Quantum</button>
      <button data-filter="energy">Energy</button>
      <button data-filter="methods">Methods</button>
    </div>
  </div>
</section>
<section style="padding-bottom:5rem">
  <div class="wrap-wide grid-3">
    <a class="card" href="/notes/grid-turbulence.html" data-filter-item="turbulence">
      <div class="thumb"><img src="/assets/img/work-3ds.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">2017–2026</p>
        <h3>Grid-generated turbulence</h3>
        <p>DNS of classical, fractal, and 3D sparse grids. Burst-buffer algorithm. Mixing and decay.</p>
      </div>
    </a>
    <a class="card" href="/notes/spectre.html" data-filter-item="turbulence methods">
      <div class="thumb"><img src="/assets/img/work-spectre.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">2025–2026</p>
        <h3>SPECTRE mixing layers</h3>
        <p>Scale-aware, physics-constrained emulator of turbulent mixing layers, Re 2,500–30,000.</p>
      </div>
    </a>
    <a class="card" href="/notes/quantum.html" data-filter-item="quantum">
      <div class="thumb"><img src="/assets/img/work-quantum.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">2024</p>
        <h3>Stair-shaped scattering grids</h3>
        <p>Time-dependent wavepackets in hyperspherical coordinates. F+HCl, O+O₂, Cl+H₂.</p>
      </div>
    </a>
    <a class="card" href="/notes/particles.html" data-filter-item="turbulence">
      <div class="thumb"><img src="/assets/img/work-particles.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">2017–2019</p>
        <h3>Inertial particle pairs</h3>
        <p>Kinematic simulation of pair diffusion. Stokes number, locality versus non-locality.</p>
      </div>
    </a>
    <a class="card" href="/notes/wind.html" data-filter-item="energy">
      <div class="thumb"><img src="/assets/img/work-wind.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Development</p>
        <h3>Blade flow and ROM</h3>
        <p>Wind-turbine blades, flow-control devices, SST, POD reduced-order models.</p>
      </div>
    </a>
    <a class="card" href="/notes/thermal.html" data-filter-item="energy">
      <div class="thumb"><img src="/assets/img/work-battery.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Development</p>
        <h3>Battery thermal management</h3>
        <p>Multiscale CFD and chemistry for lithium-ion thermal runaway diagnosis.</p>
      </div>
    </a>
    <a class="card" href="/notes/reservoir.html" data-filter-item="energy methods">
      <div class="thumb"><img src="/assets/img/work-reservoir.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">OpenFOAM</p>
        <h3>Reservoir and pipe mixing</h3>
        <p>Multiphase subsurface cases and 3DSPipe CoV–Re campaigns.</p>
      </div>
    </a>
    <a class="card" href="/notes/combustion.html" data-filter-item="energy methods">
      <div class="thumb"><img src="/assets/img/work-3ds.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Methods</p>
        <h3>Combustion CFD</h3>
        <p>Fuel–air mixing, NOx, furnaces, jets, rockets — CFD as the digital laboratory.</p>
      </div>
    </a>
    <a class="card" href="/notes/sst.html" data-filter-item="methods turbulence">
      <div class="thumb"><img src="/assets/img/work-wind.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Methods</p>
        <h3>SST turbulence model</h3>
        <p>Menter 1994 k–ω / k–ε blend, transition and DES variants, engineering use.</p>
      </div>
    </a>
    <a class="card" href="/notes/cfd.html" data-filter-item="methods">
      <div class="thumb"><img src="/assets/img/work-hydrotwin.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Methods</p>
        <h3>CFD core techniques</h3>
        <p>Navier–Stokes, RANS/LES, FVM, AMR, HPC, FSI, data assimilation.</p>
      </div>
    </a>
    <a class="card" href="/notes/materials.html" data-filter-item="methods quantum">
      <div class="thumb"><img src="/assets/img/work-quantum.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Methods</p>
        <h3>Generative materials</h3>
        <p>Diffusion models for inorganic crystals; MatterGen; carbon-capture design space.</p>
      </div>
    </a>
    <a class="card" href="/notes/hydrotwin.html" data-filter-item="methods">
      <div class="thumb"><img src="/assets/img/work-hydrotwin.jpg" alt=""></div>
      <div class="card-body">
        <p class="kicker">Development</p>
        <h3>HydroTwin Studio</h3>
        <p>Interactive desktop layer over CFD solvers. In development.</p>
      </div>
    </a>
  </div>
</section>
"""


def case(kicker, title, lead, img, alt, side, copy, back="/notes.html"):
    return f"""
<section class="case-hero">
  <div class="wrap">
    <a class="back" href="{back}">← Notes</a>
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


N_GRID = case(
    "Turbulence · HPC · 2017–2026",
    "DNS of grid-generated turbulence",
    "Classical, fractal, and 3D sparse grids. A burst-buffer algorithm that makes the Navier–Stokes comparison affordable.",
    "/assets/img/work-3ds.jpg",
    "Sparse 3D grid and turbulent wake",
    """
    <div><dt>Journal</dt><dd><em>Computers &amp; Fluids</em> 308 (2026) 106985</dd></div>
    <div><dt>DOI</dt><dd><a href="https://doi.org/10.1016/j.compfluid.2026.106985">10.1016/j.compfluid.2026.106985</a></dd></div>
    <div><dt>Earlier</dt><dd><em>J. Phys.: Conf. Series</em> 1101, 012048 (2018)</dd></div>
    <div><dt>Code</dt><dd><a href="https://github.com/FlowDat/3DS">FlowDat/3DS</a></dd></div>
    """,
    r"""
    <p>Grid-generated turbulence turns a uniform stream into a controllable cascade. Classical square grids do it at one scale. Flat fractal grids inject several scales at once, at the cost of high blockage. The <strong>3D sparse grid (3DS)</strong> puts each scale on its own co-frame, spaced along the tunnel, so effective blockage can drop well below a 2D fractal of similar intensity (Malik, US Patent 9,599,269 B2).</p>
    <p>Direct numerical simulation of the full grid, the developing wakes, and the downstream decay is I/O-bound. The <strong>burst-buffer accelerated DNS algorithm (BBDSA)</strong> parks those bursts on fast intermediate storage. The 2026 <em>Computers &amp; Fluids</em> study reports a fivefold cut in wall time and an eightfold gain in parallel efficiency, with no loss of accuracy.</p>
    <figure class="figure">
      <img src="/assets/img/figures/turb36.png" alt="Isosurfaces of vorticity">
      <figcaption class="caption">Vorticity volume from DNS — the class of field BBDSA is built to write.</figcaption>
    </figure>
    <h2>Comparison at Re = 4000</h2>
    <p>Uniform inflow in a laboratory-scale conduit. Two-dimensional classical grids, two-dimensional fractal grids, and 3DSG. A 3DSG at 24% blockage produced turbulence intensities and Reynolds stresses comparable to classical and fractal grids with substantially higher blockage: the same free-stream turbulence for less drag.</p>
    <p>Fractal grids generate intermittent multi-scale wakes and slower decay through continuous energy injection. Classical grids decay more predictably at a single dominant scale. Sparse 3D grids sit between them: sustained multi-scale activity with improved homogeneity, which is the mixing argument for combustion and chemical reactors.</p>
    <p>The 2018 open-access DNS (<em>J. Phys.: Conf. Series</em> 1101, 012048) mapped the three-frame parameter space — blockage, effective mesh size, inter-frame spacing. Wind-tunnel fractal wakes were reported the same year in <em>Topical Problems of Fluid Mechanics</em>.</p>
    """,
)

N_SPEC = case(
    "Scientific machine learning · 2025–2026",
    "SPECTRE — mixing-layer emulator",
    "A scale-separated, physics-constrained network trained on DNS mixing layers from Re 2,500 to 30,000.",
    "/assets/img/work-spectre.jpg",
    "Neural overlay on a mixing layer",
    """
    <div><dt>Status</dt><dd>Under review, <em>Results in Engineering</em>, 2026</dd></div>
    <div><dt>Code</dt><dd><a href="https://github.com/FlowDat/SMLG">FlowDat/SMLG</a></dd></div>
    <div><dt>Data</dt><dd><a href="https://zenodo.org/records/21234013">Zenodo 21234013</a></dd></div>
    """,
    r"""
    <p>Mixing layers are simple enough to DNS and hard enough to matter: two streams, a shear, a scalar, a growing thickness. A network that only fits one Reynolds number has learned a picture, not a flow.</p>
    <p><strong>SPECTRE</strong> is trained on DNS at seven Reynolds numbers — 2,500, 5,000, 10,000, 15,000, 20,000, 25,000, 30,000. Stored fields: streamwise and wall-normal velocity, pressure, scalar concentration, mean, temporal ROM coefficients, reconstruction. The public analysis stack plots spectra, stresses, coherent structures, and mixing metrics against the original DNS.</p>
    <div class="plot-grid two">
      <figure class="figure" style="margin:0"><img src="/assets/img/figures/figure05_mean_flow_profiles.jpg" alt=""><figcaption class="caption">Mean flow profiles.</figcaption></figure>
      <figure class="figure" style="margin:0"><img src="/assets/img/figures/figure08_coherent_structures.jpg" alt=""><figcaption class="caption">Coherent structures.</figcaption></figure>
    </div>
    <p>The manuscript <em>Scale-separated, physics constrained, deep neural network for turbulent mixing layer simulations</em> is under review. Copy the Zenodo dump into <code>data/</code> and the SMLG scripts regenerate the figures.</p>
    """,
)

N_Q = case(
    "Quantum molecular dynamics · 2024",
    "Stair-shaped grids for reactive scattering",
    "Hyperspherical wavepackets that do not store points the reaction never visits, including long-lived resonances.",
    "/assets/img/work-quantum.jpg",
    "Wavepacket on stair-shaped domains",
    """
    <div><dt>Papers</dt><dd><em>Chem. Phys. Lett.</em> 837, 141060 (2024)<br><em>Theor. Chem. Acc.</em> 143, 61 (2024)</dd></div>
    <div><dt>DOI</dt><dd><a href="https://doi.org/10.1016/j.cplett.2023.141060">10.1016/j.cplett.2023.141060</a><br><a href="https://doi.org/10.1007/s00214-024-03133-w">10.1007/s00214-024-03133-w</a></dd></div>
    <div><dt>Solvers</dt><dd><a href="https://github.com/FlowDat/schrod">FlowDat/schrod</a></dd></div>
    """,
    r"""
    <p>Three atoms meet; a bond breaks; another forms. In hyperspherical coordinates the whole arrangement space lives on one map. As the hyper-radius grows, the angular grid must densify. Long-range potentials make a uniform mesh prohibitive.</p>
    <p>The hyper-radius is split into <strong>stair-shaped domains</strong>, each with its own angular resolution. Regions where the energy is too high for the reaction are not stored. The wavepacket still sees continuous physics.</p>
    <figure class="figure" style="background:#000">
      <img src="/assets/img/figures/wave-packet.gif" alt="Wave packet">
      <figcaption class="caption">Time-dependent wavepacket from the Schrödinger solvers.</figcaption>
    </figure>
    <p>F + HCl: about 18% fewer points, results matching established methods. O + O₂: nearly 30%. Cl + H₂: more than 33%. The <em>Theoretical Chemistry Accounts</em> paper takes the same construction to product state-resolved probabilities, including long-lived resonances that stretch over long-range grids.</p>
    """,
)

N_P = case(
    "Turbulent dispersion · 2017–2019",
    "Inertial particle-pair diffusion",
    "How massive particles, not tracers, separate in turbulence — pollen, sand, industrial aerosols.",
    "/assets/img/work-particles.jpg",
    "Inertial particles in a turbulent flow",
    """
    <div><dt>Record</dt><dd>Dissertation, 2019 · AMMCS 2017 · EGU 2017</dd></div>
    <div><dt>Method</dt><dd>Kinematic simulation (KS)</dd></div>
    """,
    r"""
    <p>Tracers follow the fluid. Inertial particles do not. Stokes number decides whether they ride eddies or cut through them, and pair dispersion changes accordingly. Richardson’s 1926 locality picture is the textbook; a non-local theory of pair diffusion is the alternative under test.</p>
    <p><strong>Kinematic simulation</strong> builds synthetic turbulence cheap enough for millions of pairs and rich enough in scales to distinguish local from non-local spreading. Low-St particles behave like dyes. High-St particles filter small eddies and remember ballistic stretches.</p>
    """,
)

N_W = case(
    "Wind energy · reduced-order modelling",
    "Blade flow control and POD",
    "Blade-resolved CFD, passive and active devices, SST closures, and a POD/ROM stack of the near-blade field.",
    "/assets/img/work-wind.jpg",
    "Wind turbine blade with streamlines",
    """
    <div><dt>Code</dt><dd><a href="https://github.com/FlowDat/Blade_pod">FlowDat/Blade_pod</a></dd></div>
    <div><dt>Methods</dt><dd>CFD · POD · ML-ROM · SST</dd></div>
    """,
    r"""
    <p>Rotor diameter has grown faster than the materials that have to live with it. Flow-control devices — vortex generators, trailing-edge flaps, active blowing — exist to keep the boundary layer attached, to move transition, and to cut unsteady loads.</p>
    <p>RANS, typically SST k–ω and its transition variants, covers design sweeps. Proper orthogonal decomposition compresses the near-blade field into a reduced-order model. <strong>Blade_pod</strong> is that ROM experiment.</p>
    """,
)

N_T = case(
    "Energy storage · safety",
    "Multiscale battery thermal management",
    "Lithium-ion packs fail thermally at the cell, the module, and the chemistry at once. The diagnosis has to as well.",
    "/assets/img/work-battery.jpg",
    "Battery pack with thermal field",
    """
    <div><dt>Methods</dt><dd>CFD heat transfer · computational chemistry · multiscale entropy</dd></div>
    """,
    r"""
    <p>Battery thermal management is not only a cooling problem. Thermal runaway is a chemical cascade that CFD alone cannot see and that a 0D equivalent-circuit model will not locate in a pack. The useful picture is multiscale: CFD for coolant and cell-to-cell coupling; computational chemistry for the reactions that start the runaway; data-driven diagnostics (modified multiscale entropy on temperature traces) for the pattern that says the pack is leaving the safe manifold.</p>
    """,
)

N_R = case(
    "Subsurface flow · mixing",
    "Reservoir simulation and pipe mixing",
    "OpenFOAM cases for multiphase subsurface flow, and a pipe-mixing campaign of CoV versus Reynolds number.",
    "/assets/img/work-reservoir.jpg",
    "Subsurface reservoir saturations",
    """
    <div><dt>Codes</dt><dd><a href="https://github.com/FlowDat/Reservoir">Reservoir</a> · <a href="https://github.com/FlowDat/3DSPipe">3DSPipe</a></dd></div>
    """,
    r"""
    <p>Reservoir simulation is Darcy-scale transport, wells as internal boundary conditions, saturations that must be conservative. The Reservoir repository holds tutorial cases: single-phase setup, multiphase and well control, then domain decomposition and parallel I/O.</p>
    <figure class="figure paper">
      <img src="/assets/img/figures/cov-re.png" alt="CoV versus Reynolds number">
      <figcaption class="caption">Mixing quality (CoV) versus Reynolds number at successive downstream stations, 3DSPipe.</figcaption>
    </figure>
    """,
)

N_HT = case(
    "Development",
    "HydroTwin Studio",
    "The physics of CFD is hard. The workflow is harder. A desktop layer that keeps the solver and hides the obstacle course.",
    "/assets/img/work-hydrotwin.jpg",
    "Digital twin of a fluid experiment",
    """
    <div><dt>Status</dt><dd>In development</dd></div>
    <div><dt>Related</dt><dd><a href="/notes/spectre.html">SPECTRE</a> · OpenFOAM cases</dd></div>
    """,
    r"""
    <p>OpenFOAM dictionaries, meshes, and log files are the usual bottleneck. HydroTwin Studio is a desktop environment for interactive CFD that still talks to real solvers underneath. The scientific backbone is the same as this archive — 3DS grids, mixing layers, SPECTRE as a fast twin of DNS, reservoir and blade cases.</p>
    """,
)

N_COMB = case(
    "Methods",
    "CFD for combustion",
    "Fuel, air, and fire as a computable field: engines, furnaces, jets, rockets, and domestic burners.",
    "/assets/img/work-3ds.jpg",
    "Turbulent combustion visualisation",
    """
    <div><dt>Source</dt><dd>Research note, Flowdat</dd></div>
    """,
    r"""
    <p>Computational fluid dynamics lets a combustion system be watched without lighting it: injection, mixing, ignition, heat release, pollutants. The same conservation laws as any other flow, coupled to chemical kinetics.</p>
    <p>Applications on the record: fuel-injection mixing and NOx in engines; industrial furnaces and boilers; jet engines and gas turbines (stability, power, noise); biomass and coal plant burners; rocket chambers (pressure spikes); household heaters. CFD here is a digital laboratory — cheaper than a rig, and the only way to see inside some of them.</p>
    """,
)

N_SST = case(
    "Methods · turbulence closures",
    "Shear-stress transport (SST)",
    "Menter 1994: k–ω near the wall, k–ε in free shear, blended. Still the default engineering RANS model for a reason.",
    "/assets/img/work-wind.jpg",
    "Boundary-layer and free-shear blend",
    """
    <div><dt>Origin</dt><dd>Menter, 1994</dd></div>
    <div><dt>Use here</dt><dd>Blade RANS, industrial mixing, wind</dd></div>
    """,
    r"""
    <p>The SST model blends Wilcox k–ω (accurate in the viscous sublayer, sensitive to free-stream ω) with k–ε (better in free shear, weaker at the wall). Extra terms keep the eddy viscosity from over-predicting in adverse pressure gradients. That combination is why it is used on wings, cars, wind-turbine blades, stirred tanks, and compressible flight.</p>
    <p>Variants in production use: improved wall treatment, SST transition, compressible SST, SST-DES and other hybrid RANS–LES forms. Blade_pod compares a KOSST closure with a POD reduced-order model of the same blade field.</p>
    """,
)

N_CFD = case(
    "Methods",
    "CFD: core theories and techniques",
    "The stack behind the simulations in this archive — from Navier–Stokes to data assimilation.",
    "/assets/img/work-hydrotwin.jpg",
    "Computational fluid dynamics workflow",
    """
    <div><dt>Companion</dt><dd><a href="https://cfdbasics.carrd.co/">cfdbasics.carrd.co</a></dd></div>
    """,
    r"""
    <p>The governing system is continuity and Navier–Stokes, optionally energy and scalars. Turbulence is treated by RANS, LES, or DNS. Discrete forms: finite volume, finite difference, finite element. Boundaries: walls, inlets, outlets, wall functions. Multiphase: VOF, level set. Mesh: structured, unstructured, hybrid, AMR. Solvers: multigrid, MPI, GPU. Further couplings: heat transfer, phase change, FSI, CFD–DEM, SPH, chemical kinetics, moving meshes (ALE), high-order schemes, mass-conserving algorithms, stability fixes, data assimilation and learning.</p>
    <p>That list is the vocabulary of the codes in this archive — OpenFOAM cases, DNS of 3DS grids, SPECTRE as a learned surrogate, stair-shaped quantum grids as the molecular analogue of not paying for unused points.</p>
    """,
)

N_MAT = case(
    "Methods · materials",
    "Generative models for inorganic crystals",
    "Diffusion models that propose stable, unique, novel structures instead of screening a finite database.",
    "/assets/img/work-quantum.jpg",
    "Generated crystal structures",
    """
    <div><dt>Context</dt><dd>MatterGen (Microsoft Research, Nature) · QMD notes</dd></div>
    """,
    r"""
    <p>Materials discovery is usually a search over known crystals. Generative diffusion models invert that: start from noise, denoise into a chemically valid lattice, optionally conditioned on bulk modulus, magnetism, or adsorption. MatterGen, trained on hundreds of thousands of known inorganics, has produced S.U.N. (stable, unique, novel) candidates and at least one experimentally realised bulk-modulus target.</p>
    <p>The design space of interest in these notes is carbon-capture frameworks (MOFs, zeolites), energy-storage solids, and corrosion-resistant alloys — the same molecular-dynamics toolchain (VASP, Quantum ESPRESSO, LAMMPS, Gaussian) that sits next to the stair-grid scattering work.</p>
    """,
)

LOST = r"""
<section class="lost">
  <div>
    <p class="kicker">404</p>
    <h1>This streamline left the domain.</h1>
    <p class="lead" style="margin-inline:auto">No record at this path. Try the archive, the papers, or the plots.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-solid" href="/">Archive</a>
      <a class="btn btn-ghost" href="/papers.html">Papers</a>
    </div>
  </div>
</section>
"""

REDIRECT_ABOUT = """
<section class="lost">
  <div>
    <p class="kicker">Moved</p>
    <h1>See the archive.</h1>
    <p class="lead" style="margin-inline:auto">Papers, codes, and figures live in the archive.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-solid" href="/">Archive</a>
      <a class="btn btn-ghost" href="/papers.html">Papers</a>
    </div>
  </div>
</section>
"""

page("/index.html", "Flowdat — research archive", "Chronological archive of computational research: turbulence DNS, quantum scattering, SPECTRE, codes, and figures. 2017–2026.", HOME, "home", JSONLD)
page("/papers.html", "Papers — Flowdat", "Complete bibliography: journals, proceedings, dissertation, manuscripts.", PAPERS, "papers")
page("/codes.html", "Codes — Flowdat", "Public repositories: 3DS, SPECTRE/SMLG, OpenFOAM, Schrödinger, blade ROM.", CODES, "codes")
page("/plots.html", "Plots — Flowdat", "DNS, SPECTRE diagnostics, pipe-mixing CoV, wavepackets, and laboratory figures.", PLOTS, "plots")
page("/notes.html", "Notes — Flowdat", "Technical notes on grid turbulence, SPECTRE, quantum scattering, mixing, and CFD methods.", NOTES, "notes")
page("/notes/grid-turbulence.html", "Grid-generated turbulence — Flowdat", "DNS of classical, fractal, and 3D sparse grids. Burst-buffer algorithm.", N_GRID, "notes")
page("/notes/spectre.html", "SPECTRE — Flowdat", "Scale-aware deep emulator of turbulent mixing layers.", N_SPEC, "notes")
page("/notes/quantum.html", "Stair-shaped grids — Flowdat", "Quantum wavepacket reactive scattering on stair-shaped hyperspherical grids.", N_Q, "notes")
page("/notes/particles.html", "Inertial particle pairs — Flowdat", "Kinematic simulation of inertial particle-pair diffusion.", N_P, "notes")
page("/notes/wind.html", "Blade flow and ROM — Flowdat", "Wind-turbine CFD, flow control, POD reduced-order models.", N_W, "notes")
page("/notes/thermal.html", "Battery thermal management — Flowdat", "Multiscale CFD and chemistry for lithium-ion thermal runaway.", N_T, "notes")
page("/notes/reservoir.html", "Reservoir and pipe mixing — Flowdat", "OpenFOAM reservoir cases and 3DSPipe mixing.", N_R, "notes")
page("/notes/hydrotwin.html", "HydroTwin Studio — Flowdat", "Desktop environment for interactive CFD.", N_HT, "notes")
page("/notes/combustion.html", "Combustion CFD — Flowdat", "CFD of engines, furnaces, jets, and rockets.", N_COMB, "notes")
page("/notes/sst.html", "SST turbulence model — Flowdat", "Menter SST k–ω / k–ε blend and variants.", N_SST, "notes")
page("/notes/cfd.html", "CFD techniques — Flowdat", "Core theories and techniques of computational fluid dynamics.", N_CFD, "notes")
page("/notes/materials.html", "Generative materials — Flowdat", "Diffusion models for inorganic crystal design.", N_MAT, "notes")
page("/404.html", "Page not found — Flowdat", "No record at this path.", LOST, "")
page("/about.html", "Flowdat archive", "Research archive of papers, codes, and figures.", REDIRECT_ABOUT, "")
page("/publications.html", "Papers — Flowdat", "Complete bibliography: journals, proceedings, dissertation, manuscripts.", PAPERS, "papers")
page("/work.html", "Notes — Flowdat", "Technical notes on grid turbulence, SPECTRE, quantum scattering, mixing, and CFD methods.", NOTES, "notes")
page("/work/3ds.html", "Grid-generated turbulence — Flowdat", "DNS of classical, fractal, and 3D sparse grids. Burst-buffer algorithm.", N_GRID, "notes")
page("/work/spectre.html", "SPECTRE — Flowdat", "Scale-aware deep emulator of turbulent mixing layers.", N_SPEC, "notes")
page("/work/quantum.html", "Stair-shaped grids — Flowdat", "Quantum wavepacket reactive scattering on stair-shaped hyperspherical grids.", N_Q, "notes")
page("/work/particles.html", "Inertial particle pairs — Flowdat", "Kinematic simulation of inertial particle-pair diffusion.", N_P, "notes")
page("/work/wind.html", "Blade flow and ROM — Flowdat", "Wind-turbine CFD, flow control, POD reduced-order models.", N_W, "notes")
page("/work/battery.html", "Battery thermal management — Flowdat", "Multiscale CFD and chemistry for lithium-ion thermal runaway.", N_T, "notes")
page("/work/reservoir.html", "Reservoir and pipe mixing — Flowdat", "OpenFOAM reservoir cases and 3DSPipe mixing.", N_R, "notes")
page("/work/hydrotwin.html", "HydroTwin Studio — Flowdat", "Desktop environment for interactive CFD.", N_HT, "notes")

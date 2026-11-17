(() => {
  const header = document.getElementById("header");
  const menuBtn = document.querySelector(".menu-btn");
  const nav = document.getElementById("menu");

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (menuBtn && nav) {
    menuBtn.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.textContent = open ? "Close" : "Menu";
    });
  }

  document.querySelectorAll("[data-page]").forEach((el) => {
    const page = document.body.dataset.page;
    if (page && el.dataset.page === page) el.classList.add("is-active");
  });

  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  document.querySelectorAll("[data-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.filter;
      document.querySelectorAll("[data-filter]").forEach((b) => b.classList.toggle("is-on", b === btn));
      document.querySelectorAll("[data-filter-item]").forEach((item) => {
        const tags = item.dataset.filterItem.split(/\s+/);
        item.classList.toggle("is-hidden", key !== "all" && !tags.includes(key));
      });
    });
  });

  const canvas = document.getElementById("flow");
  if (!canvas) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;

  const ctx = canvas.getContext("2d", { alpha: true });
  const hero = canvas.parentElement;
  let w = 0, h = 0, dpr = 1, t = 0;
  const N = 140;
  const particles = Array.from({ length: N }, () => spawn());

  function spawn() {
    return {
      x: Math.random(),
      y: Math.random(),
      s: 0.4 + Math.random() * 1.2,
      life: 40 + Math.random() * 140,
      hue: Math.random() < 0.18 ? "copper" : "teal",
    };
  }

  function field(x, y, time) {
    const px = x * 6.2;
    const py = y * 4.4;
    const a = Math.sin(px * 1.1 + time * 0.00018) + Math.cos(py * 0.9 - time * 0.00014);
    const b = Math.sin((px + py) * 0.65 + time * 0.00011);
    const u = Math.cos(py * 1.05 + a) * 0.55 + Math.sin(px * 0.4 + b) * 0.2;
    const v = Math.sin(px * 0.95 - a) * 0.5 + 0.08;
    return [u, v];
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = hero.clientWidth;
    h = hero.clientHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function step(now) {
    t = now;
    ctx.fillStyle = "rgba(8,9,12,0.12)";
    ctx.fillRect(0, 0, w, h);
    for (const p of particles) {
      const [u, v] = field(p.x, p.y, t);
      const x0 = p.x * w;
      const y0 = p.y * h;
      p.x += (u * p.s) * 0.0018;
      p.y += (v * p.s) * 0.0018;
      p.life -= 1;
      if (p.x < -0.05 || p.x > 1.05 || p.y < -0.05 || p.y > 1.05 || p.life < 0) {
        Object.assign(p, spawn());
        if (Math.random() < 0.5) p.x = Math.random();
        else p.y = 0;
        continue;
      }
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(p.x * w, p.y * h);
      ctx.strokeStyle = p.hue === "copper"
        ? "rgba(208,138,90,0.55)"
        : "rgba(94,224,200,0.45)";
      ctx.lineWidth = p.s * 0.9;
      ctx.stroke();
    }
    requestAnimationFrame(step);
  }

  resize();
  window.addEventListener("resize", resize);
  ctx.fillStyle = "#08090c";
  ctx.fillRect(0, 0, w, h);
  requestAnimationFrame(step);
})();

/* ===================================================
   Fahrschule G&R — Main JS
   =================================================== */

(function () {
  'use strict';

  // ── Dark / Light Mode Toggle ─────────────────────
  var THEME_KEY = 'gundr-theme';

  function getPreferredTheme() {
    var stored = localStorage.getItem(THEME_KEY);
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);

    document.querySelectorAll('.theme-toggle').forEach(function (btn) {
      var iconSun  = btn.querySelector('.icon-sun');
      var iconMoon = btn.querySelector('.icon-moon');
      if (iconSun && iconMoon) {
        iconSun.style.display  = theme === 'dark'  ? 'block' : 'none';
        iconMoon.style.display = theme === 'light' ? 'block' : 'none';
      }
    });
  }

  var currentTheme = getPreferredTheme();
  applyTheme(currentTheme);

  document.querySelectorAll('.theme-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
      localStorage.setItem(THEME_KEY, currentTheme);
      applyTheme(currentTheme);
    });
  });

  // ── Hero Carousel ────────────────────────────────
  var slides   = Array.from(document.querySelectorAll('.hero__slide'));
  var dots     = Array.from(document.querySelectorAll('.hero__dot'));
  var current  = 0;
  var autoplay = null;

  function goToSlide(index) {
    if (!slides.length) return;
    slides[current].classList.remove('is-active');
    dots[current] && dots[current].classList.remove('is-active');
    current = (index + slides.length) % slides.length;
    slides[current].classList.add('is-active');
    dots[current] && dots[current].classList.add('is-active');
  }

  function startAutoplay() {
    stopAutoplay();
    autoplay = setInterval(function () {
      goToSlide(current + 1);
    }, 7000);
  }

  function stopAutoplay() {
    if (autoplay) { clearInterval(autoplay); autoplay = null; }
  }

  if (slides.length > 0) {
    goToSlide(0);
    startAutoplay();

    dots.forEach(function (dot, i) {
      dot.addEventListener('click', function () {
        stopAutoplay();
        goToSlide(i);
        startAutoplay();
      });
    });

    var heroEl = document.querySelector('.hero');
    if (heroEl) {
      heroEl.addEventListener('mouseenter', stopAutoplay);
      heroEl.addEventListener('mouseleave', startAutoplay);
    }
  }

  // ── Fleet Tabs ───────────────────────────────────
  document.querySelectorAll('.fleet-tab').forEach(function (tab) {
    tab.addEventListener('click', function () {
      var target = tab.getAttribute('data-target');
      document.querySelectorAll('.fleet-tab').forEach(function (t) {
        t.classList.remove('is-active');
      });
      document.querySelectorAll('.fleet-panel').forEach(function (p) {
        p.classList.remove('is-active');
      });
      tab.classList.add('is-active');
      var panel = document.getElementById(target);
      if (panel) panel.classList.add('is-active');
    });
  });

  // ── Toast helper ─────────────────────────────────
  function showToast(title, msg) {
    var toast = document.getElementById('toast');
    if (!toast) return;
    var tTitle = toast.querySelector('.toast__title');
    var tText  = toast.querySelector('.toast__text');
    if (tTitle) tTitle.textContent = title;
    if (tText)  tText.textContent  = msg;
    toast.classList.add('is-visible');
    setTimeout(function () {
      toast.classList.remove('is-visible');
    }, 6000);
  }

  // ── Contact / Beratung Form ──────────────────────
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      showToast(
        'Nachricht erhalten',
        'Diese Nachricht hätte an Sie gesendet werden können. Da dies ein Showcase-Design ist, erfolgt die echte E-Mail-Anbindung erst bei Kauf oder Übernahme der Website.'
      );
      contactForm.reset();
    });
  }

  // ── Anmeldung Form ───────────────────────────────
  var anmeldungForm = document.getElementById('anmeldung-form');
  if (anmeldungForm) {
    anmeldungForm.addEventListener('submit', function (e) {
      e.preventDefault();
      showToast(
        'Anmeldung erhalten',
        'Diese Anmeldung hätte an die Fahrschule G&R übermittelt werden können. Da dies ein Showcase-Design ist, erfolgt die echte Anbindung erst bei Übernahme der Website.'
      );
      anmeldungForm.reset();
    });
  }

})();

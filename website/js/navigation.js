/* ===================================================
   Fahrschule G&R — Navigation JS
   =================================================== */

(function () {
  'use strict';

  const nav       = document.getElementById('main-nav');
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  const overlay   = document.getElementById('nav-overlay');

  // ── Sticky / transparent nav on scroll ──────────
  function handleScroll() {
    if (window.scrollY > 60) {
      nav && nav.classList.add('is-scrolled');
    } else {
      nav && nav.classList.remove('is-scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // ── Mobile menu toggle ───────────────────────────
  function openMenu() {
    hamburger && hamburger.classList.add('is-open');
    mobileNav && mobileNav.classList.add('is-open');
    overlay   && overlay.classList.add('is-visible');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    hamburger && hamburger.classList.remove('is-open');
    mobileNav && mobileNav.classList.remove('is-open');
    overlay   && overlay.classList.remove('is-visible');
    document.body.style.overflow = '';
  }

  hamburger && hamburger.addEventListener('click', function () {
    if (mobileNav && mobileNav.classList.contains('is-open')) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  overlay && overlay.addEventListener('click', closeMenu);

  // Close on mobile link click
  document.querySelectorAll('.mobile-nav__link, .mobile-nav__cta').forEach(function (el) {
    el.addEventListener('click', closeMenu);
  });

  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  // ── Active nav link highlight ────────────────────
  var currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__link, .mobile-nav__link').forEach(function (el) {
    var href = el.getAttribute('href') || '';
    if (href && href.includes(currentPath) && currentPath !== '') {
      el.classList.add('is-active');
    }
  });

})();

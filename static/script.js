document.addEventListener('DOMContentLoaded', function () {

  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.sidenav__link'));
  var sections = navLinks
    .map(function (link) {
      var id = link.getAttribute('data-section');
      return document.getElementById(id);
    })
    .filter(Boolean);

  
  navLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var targetId = link.getAttribute('data-section');
      var target = document.getElementById(targetId);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      closeMobileNav();
    });
  });

  
  function setActiveLink() {
    var scrollPos = window.scrollY + window.innerHeight * 0.35;
    var current = sections[0];

    sections.forEach(function (section) {
      if (section.offsetTop <= scrollPos) {
        current = section;
      }
    });

    navLinks.forEach(function (link) {
      link.classList.remove('is-active');
      if (link.getAttribute('data-section') === current.id) {
        link.classList.add('is-active');
      }
    });
  }

  var scrollTicking = false;
  window.addEventListener('scroll', function () {
    if (!scrollTicking) {
      window.requestAnimationFrame(function () {
        setActiveLink();
        scrollTicking = false;
      });
      scrollTicking = true;
    }
  });

  setActiveLink();

  var revealTargets = document.querySelectorAll(
    '.section__head, .about__grid, .card-grid, .contact__grid'
  );

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );

    revealTargets.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    revealTargets.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  
  var sidenav = document.getElementById('sidenav');
  var navToggle = document.getElementById('navToggle');
  var navScrim = document.getElementById('navScrim');

  function openMobileNav() {
    sidenav.classList.add('is-open');
    navScrim.classList.add('is-visible');
  }

  function closeMobileNav() {
    sidenav.classList.remove('is-open');
    navScrim.classList.remove('is-visible');
  }

  if (navToggle) {
    navToggle.addEventListener('click', function () {
      if (sidenav.classList.contains('is-open')) {
        closeMobileNav();
      } else {
        openMobileNav();
      }
    });
  }

  if (navScrim) {
    navScrim.addEventListener('click', closeMobileNav);
  }

  
  let yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

});

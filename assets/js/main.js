/* ===================================================
   Shubham Kumar Jha — Portfolio | main.js v3
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // ─── 1. NAVBAR: scroll state ──────────────────────
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        updateActiveNav();
    }, { passive: true });


    // ─── 2. ACTIVE NAV HIGHLIGHTING ──────────────────
    const sections  = document.querySelectorAll('section[id]');
    const navLinks  = document.querySelectorAll('.nav-links .nav-link');

    function updateActiveNav() {
        let current = '';
        sections.forEach(sec => {
            if (window.scrollY >= sec.offsetTop - 140) {
                current = sec.getAttribute('id');
            }
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${current}`) link.classList.add('active');
        });
    }


    // ─── 3. MOBILE HAMBURGER MENU ────────────────────
    const hamburger     = document.getElementById('hamburger');
    const navLinksEl    = document.getElementById('navLinks');
    const hamburgerIcon = document.getElementById('hamburger-icon');

    function closeMenu() {
        navLinksEl.classList.remove('open');
        hamburgerIcon.className = 'fas fa-bars';
    }

    hamburger.addEventListener('click', () => {
        const isOpen = navLinksEl.classList.toggle('open');
        hamburgerIcon.className = isOpen ? 'fas fa-times' : 'fas fa-bars';
    });

    navLinks.forEach(link => link.addEventListener('click', closeMenu));


    // ─── 4. HERO TYPING EFFECT ───────────────────────
    const typedEl = document.getElementById('typed-text');
    if (typedEl) {
        const typedRoles = ['Aspiring Machine Learning Engineer', 'Data Scientist'];
        let roleIdx = 0;
        let charIdx = 0;
        let isDeleting = false;

        function typeRole() {
            const currentRole = typedRoles[roleIdx];
            
            if (!isDeleting) {
                typedEl.textContent = currentRole.slice(0, ++charIdx);
                if (charIdx === currentRole.length) {
                    isDeleting = true;
                    setTimeout(typeRole, 2500);
                    return;
                }
            } else {
                typedEl.textContent = currentRole.slice(0, --charIdx);
                if (charIdx === 0) {
                    isDeleting = false;
                    roleIdx = (roleIdx + 1) % typedRoles.length;
                    setTimeout(typeRole, 400);
                    return;
                }
            }
            
            const speed = isDeleting ? (Math.random() * 10 + 25) : (Math.random() * 20 + 40);
            setTimeout(typeRole, speed);
        }

        setTimeout(typeRole, 1500);
    }


    // ─── 5. SCROLL REVEAL ────────────────────────────
    const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => revealObserver.observe(el));


    // ─── 6. STAGGERED CHILDREN ANIMATION ─────────────
    // For .stagger containers, give each direct child a delay
    document.querySelectorAll('.stagger').forEach(parent => {
        Array.from(parent.children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.08}s`;
        });
    });


    // ─── 7. COUNTER ANIMATION ────────────────────────
    const counters = document.querySelectorAll('.counter[data-target]');
    const r2El     = document.getElementById('r2-stat');

    function animateCounter(el) {
        const target   = +el.dataset.target;
        const suffix   = el.dataset.suffix || '';
        const duration = 1800;
        const fps      = 60;
        const steps    = Math.round(duration / (1000 / fps));
        let   step     = 0;

        const timer = setInterval(() => {
            step++;
            const progress = step / steps;
            const eased    = 1 - Math.pow(1 - progress, 3); // ease-out cubic
            const current  = Math.round(target * eased);
            el.textContent = current + suffix;
            if (step >= steps) {
                el.textContent = target + suffix;
                clearInterval(timer);
            }
        }, 1000 / fps);
    }

    function animateR2() {
        const target   = 0.67;
        const duration = 2000;
        const fps      = 60;
        const steps    = Math.round(duration / (1000 / fps));
        let   step     = 0;

        const timer = setInterval(() => {
            step++;
            const progress = step / steps;
            const eased    = 1 - Math.pow(1 - progress, 3);
            r2El.textContent = (target * eased).toFixed(2);
            if (step >= steps) {
                r2El.textContent = target.toFixed(2);
                clearInterval(timer);
            }
        }, 1000 / fps);
    }

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                if (el.classList.contains('counter')) animateCounter(el);
                if (el.id === 'r2-stat')              animateR2();
                counterObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(c => counterObserver.observe(c));
    if (r2El) counterObserver.observe(r2El);


    // ─── 8. SKILL TAGS STAGGER POP-IN ────────────────
    const tagObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const tags = entry.target.querySelectorAll('.tag');
                tags.forEach((tag, i) => {
                    setTimeout(() => {
                        tag.style.transition = `opacity 0.3s ease ${i * 0.05}s, transform 0.3s ease ${i * 0.05}s`;
                        tag.classList.add('visible');
                    }, i * 50);
                });
                tagObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.skill-card').forEach(card => tagObserver.observe(card));


    // ─── 9. MODAL SYSTEM ─────────────────────────────
    const modalBg    = document.getElementById('modalBg');
    const modalBoxes = document.querySelectorAll('.modal-box');

    function openModal(id) {
        modalBoxes.forEach(m => m.style.display = 'none');
        const target = document.getElementById(id);
        if (target) {
            target.style.display = 'block';
            // Force reflow before adding class for transition
            modalBg.offsetHeight;
            modalBg.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeModal() {
        modalBg.classList.remove('open');
        document.body.style.overflow = '';
        setTimeout(() => {
            modalBoxes.forEach(m => m.style.display = 'none');
        }, 300);
    }

    // Open on project card click
    document.querySelectorAll('.project-card[data-modal]').forEach(card => {
        card.addEventListener('click', () => openModal(card.dataset.modal));
    });

    // Close buttons
    document.querySelectorAll('[data-close]').forEach(btn => {
        btn.addEventListener('click', closeModal);
    });

    // Close on backdrop click
    modalBg.addEventListener('click', (e) => {
        if (e.target === modalBg) closeModal();
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalBg.classList.contains('open')) closeModal();
    });


    // ─── 10. SMOOTH NAV LINK SCROLL ──────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});

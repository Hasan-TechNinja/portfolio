/**
 * Fullstack Portfolio Interactive Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Drawer Toggle
    const mobileToggle = document.getElementById('mobile-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    if (mobileToggle && mobileMenu) {
        mobileToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (mobileMenu.classList.contains('active')) {
                icon.className = 'fa-solid fa-xmark';
            } else {
                icon.className = 'fa-solid fa-bars';
            }
        });

        mobileNavLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                mobileToggle.querySelector('i').className = 'fa-solid fa-bars';
            });
        });
    }

    // 2. Scroll Spy & Active Nav Link Highlight
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let currentSection = '';
        const scrollPosition = window.scrollY + 200;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });

    // 3. Project Category Filter Tabs
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all filter buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');

                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });
        });
    });

    // 4. AJAX Contact Form Submission
    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('submit-btn');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Loading State
            const originalBtnHTML = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Sending...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
            formStatus.className = 'form-status';
            formStatus.style.display = 'none';

            const formData = new FormData(contactForm);

            try {
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    formStatus.className = 'form-status success';
                    formStatus.textContent = result.message;
                    formStatus.style.display = 'block';
                    contactForm.reset();
                } else {
                    formStatus.className = 'form-status error';
                    formStatus.textContent = result.message || 'Error sending message. Please try again.';
                    formStatus.style.display = 'block';
                }
            } catch (error) {
                console.error('Contact Form Error:', error);
                formStatus.className = 'form-status error';
                formStatus.textContent = 'A network error occurred. Please try again later.';
                formStatus.style.display = 'block';
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHTML;
            }
        });
    }

    // 5. Project Modal
    const projectModal = document.getElementById('projectModal');
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    
    if (projectModal && modalCloseBtn) {
        const modalTitle = document.getElementById('modalTitle');
        const modalDesc = document.getElementById('modalDesc');
        const modalCategory = document.getElementById('modalCategory');
        const modalImage = document.getElementById('modalImage');
        const modalTech = document.getElementById('modalTech');
        const modalActions = document.getElementById('modalActions');
        
        const openModalBtns = document.querySelectorAll('.view-details-btn');
        
        openModalBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const card = e.target.closest('.project-card');
                if (!card) return;
                
                const pTitle = card.querySelector('.pd-title').innerHTML;
                const pDesc = card.querySelector('.pd-desc').innerHTML;
                const pCat = card.querySelector('.pd-category').innerHTML;
                const pImg = card.querySelector('.pd-image').innerHTML;
                const pLive = card.querySelector('.pd-live').innerHTML;
                const pGit = card.querySelector('.pd-github').innerHTML;
                const pTech = card.querySelector('.pd-tech').innerHTML;
                
                modalTitle.innerHTML = pTitle;
                modalDesc.innerHTML = pDesc;
                modalCategory.innerHTML = pCat;
                modalImage.src = pImg;
                
                // Build Tech Tags
                modalTech.innerHTML = '';
                if (pTech.trim()) {
                    const tags = pTech.trim().split(/\s+/);
                    tags.forEach(t => {
                        const span = document.createElement('span');
                        span.className = 'tag-pill';
                        span.textContent = t;
                        modalTech.appendChild(span);
                    });
                }
                
                // Build Actions
                modalActions.innerHTML = '';
                if (pLive.trim()) {
                    const aLive = document.createElement('a');
                    aLive.href = pLive;
                    aLive.target = '_blank';
                    aLive.className = 'btn btn-primary';
                    aLive.innerHTML = 'Live Demo <i class="fa-solid fa-arrow-up-right-from-square"></i>';
                    modalActions.appendChild(aLive);
                }
                if (pGit.trim()) {
                    const aGit = document.createElement('a');
                    aGit.href = pGit;
                    aGit.target = '_blank';
                    aGit.className = 'btn btn-outline';
                    aGit.innerHTML = '<i class="fa-brands fa-github"></i> Source Code';
                    modalActions.appendChild(aGit);
                }
                
                // Show modal
                document.body.style.overflow = 'hidden'; // Prevent background scroll
                projectModal.classList.add('active');
            });
        });
        
        const closeModal = () => {
            projectModal.classList.remove('active');
            document.body.style.overflow = '';
        };
        
        modalCloseBtn.addEventListener('click', closeModal);
        projectModal.addEventListener('click', (e) => {
            if (e.target === projectModal) {
                closeModal();
            }
        });
    }
});

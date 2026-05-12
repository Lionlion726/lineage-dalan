// ══ 導覽列自動標記當前頁 ══
function initNav() {
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.topnav-link').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === path);
  });
}

// ══ 浮動側欄 Modal ══
function initFloatSidebar() {
  document.querySelectorAll('.float-btn[data-modal]').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = document.getElementById(btn.dataset.modal);
      if (modal) modal.classList.add('open');
    });
  });

  document.querySelectorAll('.float-modal').forEach(modal => {
    modal.addEventListener('click', e => {
      if (e.target === modal) modal.classList.remove('open');
    });
    modal.querySelector('.modal-close')?.addEventListener('click', () => {
      modal.classList.remove('open');
    });
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.float-modal.open').forEach(m => m.classList.remove('open'));
    }
  });
}

// ══ Hero 視差滾動 ══
function initParallax() {
  const heroBg = document.querySelector('.hero-bg');
  if (!heroBg) return;
  window.addEventListener('scroll', () => {
    heroBg.style.transform = `translateY(${window.scrollY * 0.28}px)`;
  }, { passive: true });
}

// ══ 啟動 ══
document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initFloatSidebar();
  initParallax();
});

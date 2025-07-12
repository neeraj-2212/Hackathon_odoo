// Animate lines on scroll
const lines = document.querySelectorAll('.line');

function revealLines() {
  lines.forEach((line, index) => {
    const top = line.getBoundingClientRect().top;
    if (top < window.innerHeight - 100) {
      setTimeout(() => line.classList.add('visible'), index * 200);
    }
  });
}

window.addEventListener('scroll', revealLines);
window.addEventListener('load', revealLines);

// Scroll to categories section
function scrollToCategories() {
  const section = document.getElementById('categories');
  section.scrollIntoView({ behavior: 'smooth' });
}

/////////////////
// MODALS SKILLS //
/////////////////
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");
  const modalContent = document.querySelector(".modal-content");

  const skillInfo = {
    html: {
      title: "HTML (Nivel Alto)",
      text: "Tengo un dominio avanzado de HTML, creando estructuras semánticas limpias y adaptadas a proyectos web complejos.",
      level: "high"
    },
    css: {
      title: "CSS (Nivel Alto)",
      text: "Me especializo en estilos modernos, responsive design, y efectos visuales avanzados con animaciones y gradientes.",
      level: "high"
    },
    jira: {
      title: "Jira (Nivel Alto)",
      text: "Amplia experiencia gestionando tareas y flujos ágiles en entornos colaborativos de desarrollo usando Jira.",
      level: "high"
    },
    js: {
      title: "JavaScript (Nivel Medio)",
      text: "Experiencia construyendo funcionalidades dinámicas y manipulando el DOM, pero aún estoy profundizando en frameworks modernos.",
      level: "medium"
    },
    python: {
      title: "Python (Nivel Medio)",
      text: "Conocimientos sólidos de Python para automatización, scripting, y desarrollo de pequeñas aplicaciones.",
      level: "medium"
    },
    github: {
      title: "GitHub (Nivel Medio)",
      text: "Uso habitual de GitHub para control de versiones, ramas, pull requests y colaboración en equipo.",
      level: "medium"
    },
    php: {
      title: "PHP (Nivel Bajo)",
      text: "Conocimientos básicos, principalmente para mantenimiento y ajustes menores en proyectos existentes.",
      level: "low"
    },
    mysql: {
      title: "MySQL (Nivel Bajo)",
      text: "Capacidad para ejecutar consultas simples y comprender estructuras de bases de datos relacionales.",
      level: "low"
    },
    powerplatform: {
      title: "Power Platform (Nivel Bajo)",
      text: "Familiarizado con la creación básica de aplicaciones en Power Apps, flujos simples en Power Automate y uso inicial de Dataverse.",
      level: "low"
    }
  };

  window.openModal = function(skill) {
    const info = skillInfo[skill];
    modalTitle.textContent = info.title;
    modalBody.textContent = info.text;

    // Reset clases previas
    modalContent.classList.remove("high", "medium", "low");

    // Asignar color según nivel
    modalContent.classList.add(info.level);

    modal.style.display = "flex";
  };

  window.closeModal = function() {
    modal.style.display = "none";
  };

  // Cierra si se hace clic fuera del modal
  window.onclick = function(event) {
    if (event.target === modal) {
      closeModal();
    }
  };
});

/////////////////////////
// ANIMACIÓN VALORACIONES //
/////////////////////////
function updateCarouselButtons() {
  const track = document.getElementById('carouselTrack');
  const btnLeft = document.querySelector('.carousel-btn.left');
  const btnRight = document.querySelector('.carousel-btn.right');

  // Mostrar u ocultar flechas según posición de scroll
  btnLeft.style.display = track.scrollLeft <= 0 ? 'none' : 'block';

  const maxScrollLeft = track.scrollWidth - track.clientWidth;
  btnRight.style.display = track.scrollLeft >= maxScrollLeft - 1 ? 'none' : 'block';
}

// Adaptar al hacer scroll
document.getElementById('carouselTrack').addEventListener('scroll', updateCarouselButtons);

// Adaptar al redimensionar
window.addEventListener('resize', updateCarouselButtons);

// Adaptar después de hacer scroll con botones
function scrollCarousel(direction) {
  const track = document.getElementById('carouselTrack');
  const scrollAmount = 320;

  track.scrollBy({
    left: scrollAmount * direction,
    behavior: 'smooth'
  });

  // Esperar animación y luego actualizar botones
  setTimeout(updateCarouselButtons, 400); // Ajusta según duración del scroll
}

// Ejecutar una vez al cargar
window.addEventListener('DOMContentLoaded', updateCarouselButtons);


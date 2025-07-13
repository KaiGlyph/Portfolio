// Función para toggle del menú hamburguesa
function toggleMenu() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.navmenu');
    
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
}

// Cerrar menú al hacer clic en un enlace (opcional, para mejor UX)
document.querySelectorAll('.navmenu a').forEach(link => {
    link.addEventListener('click', () => {
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.navmenu');
        
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Cerrar menú al hacer clic fuera de él (opcional)
document.addEventListener('click', (e) => {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.navmenu');
    
    if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }
});

// Manejar redimensionamiento de ventana
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.navmenu');
        
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }
});

// Funciones para los modales de skills
function openModal(skill) {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    const modalContent = document.querySelector('.modal-content');
    
    const skillData = {
        html: {
            title: 'HTML',
            description: 'Tengo un dominio avanzado de HTML, creando estructuras semánticas limpias y adaptadas a proyectos web complejos.',
            level: 'high'
        },
        css: {
            title: 'CSS',
            description: 'Me especializo en estilos modernos, responsive design, y efectos visuales avanzados con animaciones y gradientes.',
            level: 'high'
        },
        jira: {
            title: 'Jira',
            description: 'Gran Manejo gestionando tareas y flujos ágiles en entornos colaborativos de desarrollo usando Jira.',
            level: 'high'
        },
        js: {
            title: 'JavaScript',
            description: 'Experiencia construyendo funcionalidades dinámicas y manipulando el DOM, pero aún estoy profundizando en frameworks modernos.',
            level: 'medium'
        },
        python: {
            title: 'Python',
            description: 'Uso habitual de GitHub para control de versiones, ramas, pull requests y colaboración en equipo.',
            level: 'medium'
        },
        github: {
            title: 'GitHub',
            description: 'Plataforma de control de versiones. Manejo de repositorios, branches, pull requests y colaboración en proyectos.',
            level: 'medium'
        },
        php: {
            title: 'PHP',
            description: 'Conocimientos básicos, principalmente para mantenimiento y ajustes menores en proyectos existentes.',
            level: 'low'
        },
        mysql: {
            title: 'MySQL',
            description: 'Capacidad para ejecutar consultas simples y comprender estructuras de bases de datos relacionales.',
            level: 'low'
        },
        powerplatform: {
            title: 'Power Platform',
            description: 'Familiarizado con la creación básica de aplicaciones en Power Apps, flujos simples en Power Automate y uso inicial de Dataverse.',
            level: 'low'
        }
    };
    
    const data = skillData[skill];
    modalTitle.textContent = data.title;
    modalBody.textContent = data.description;
    
    // Remover clases de nivel anteriores
    modalContent.classList.remove('high', 'medium', 'low');
    // Agregar clase de nivel actual
    modalContent.classList.add(data.level);
    
    modal.style.display = 'flex';
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
}

// Cerrar modal al hacer clic fuera de él
window.addEventListener('click', (e) => {
    const modal = document.getElementById('modal');
    if (e.target === modal) {
        closeModal();
    }
});

// Función para el carousel de valoraciones
function scrollCarousel(direction) {
    const track = document.getElementById('carouselTrack');
    const scrollAmount = 400; 
    
    if (direction === 1) {
        track.scrollLeft += scrollAmount;
    } else {
        track.scrollLeft -= scrollAmount;
    }
}

// Auto-scroll del carousel (opcional)
let autoScrollInterval;

function startAutoScroll() {
    autoScrollInterval = setInterval(() => {
        const track = document.getElementById('carouselTrack');
        const maxScroll = track.scrollWidth - track.clientWidth;
        
        if (track.scrollLeft >= maxScroll) {
            track.scrollLeft = 0;
        } else {
            track.scrollLeft += 380;
        }
    }, 7000);
}

function stopAutoScroll() {
    clearInterval(autoScrollInterval);
}

// Iniciar auto-scroll cuando la página carga
document.addEventListener('DOMContentLoaded', () => {
    startAutoScroll();
    
    // Pausar auto-scroll cuando el usuario interactúa con el carousel
    const carouselContainer = document.querySelector('.carousel-container');
    carouselContainer.addEventListener('mouseenter', stopAutoScroll);
    carouselContainer.addEventListener('mouseleave', startAutoScroll);
});

// Animación de hover para la imagen del header
document.addEventListener('DOMContentLoaded', () => {
    const headerImg = document.querySelector('header img');
    if (headerImg) {
        headerImg.addEventListener('mouseenter', () => {
            headerImg.style.transform = 'scale(1.05) rotate(2deg)';
        });
        
        headerImg.addEventListener('mouseleave', () => {
            headerImg.style.transform = 'scale(1) rotate(0deg)';
        });
    }
});
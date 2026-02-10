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
        react: {
            title: 'React',
            description: 'Conocimientos sólidos en la creación de componentes reutilizables, gestión de estado y hooks en aplicaciones React.',
            level: 'medium'
        },
        typescript: {
            title: 'TypeScript',
            description: 'Familiaridad con la tipificación estática y la integración de TypeScript en proyectos JavaScript para mejorar la calidad del código.',
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
        mysql: {
            title: 'MySQL',
            description: 'Capacidad para ejecutar consultas simples y comprender estructuras de bases de datos relacionales.',
            level: 'medium'
        },
        powerplatform: {
            title: 'Power Platform',
            description: 'Familiarizado con la creación básica de aplicaciones en Power Apps, flujos simples en Power Automate y uso inicial de Dataverse.',
            level: 'medium'
        },
        php: {
            title: 'PHP',
            description: 'Conocimientos básicos, principalmente para mantenimiento y ajustes menores en proyectos existentes.',
            level: 'low'
        },
        outsystems: {
            title: 'OutSystems',
            description: 'Conocimientos básicos en desarrollo low-code, enfocado en la creación rápida de aplicaciones empresariales simples.',
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

// Filtro de proyectos
function filtrarProyectos(filterType) {
    const filterButtons = document.querySelectorAll('.filtro-btn');
    const tarjetasProyecto = document.querySelectorAll('.tarjetaproyecto');
    
    // Remover clase activa de todos los botones
    filterButtons.forEach(btn => btn.classList.remove('activo'));
    
    // Añadir clase activa al botón seleccionado
    event.target.classList.add('activo');
    
    tarjetasProyecto.forEach(tarjeta => {
        const lenguajes = tarjeta.querySelectorAll('.lenguajes .chip');
        const lenguajesArray = Array.from(lenguajes).map(chip => chip.textContent.trim().toLowerCase());
        
        let mostrar = false;
        
        switch(filterType) {
            case 'all':
                mostrar = true;
                break;
                
            case 'powerplatform':
                // Verificar si tiene Power Apps o Power Automate
                mostrar = lenguajesArray.some(lenguaje => 
                    lenguaje.includes('power apps') || 
                    lenguaje.includes('power automate')
                );
                break;
                
            case 'htmlcssjs':
                // Verificar si tiene HTML, CSS y JS juntos
                const tieneHTML = lenguajesArray.includes('html');
                const tieneCSS = lenguajesArray.includes('css');
                const tieneJS = lenguajesArray.includes('js');
                
                mostrar = tieneHTML && tieneCSS && tieneJS;
                break;
                
            case 'python':
                // Verificar si tiene Python
                mostrar = lenguajesArray.includes('python');
                break;
                
            case 'php':
                // Verificar si tiene PHP
                mostrar = lenguajesArray.includes('php');
                break;
                
            case 'reactts':
                // Verificar si tiene React Y TypeScript juntos
                const tieneReact = lenguajesArray.includes('react');
                const tieneTypeScript = lenguajesArray.includes('typescript') || lenguajesArray.includes('type script');
                
                mostrar = tieneReact && tieneTypeScript;
                break;
        }
        
        if (mostrar) {
            tarjeta.style.display = 'block';
            tarjeta.style.opacity = '0';
            setTimeout(() => {
                tarjeta.style.opacity = '1';
                tarjeta.style.transform = 'translateY(0)';
            }, 10);
        } else {
            tarjeta.style.display = 'none';
        }
    });
}

// Iniciar auto-scroll cuando la página carga y configurar filtros
document.addEventListener('DOMContentLoaded', () => {
    // Auto-scroll del carousel
    startAutoScroll();
    
    // Pausar auto-scroll cuando el usuario interactúa con el carousel
    const carouselContainer = document.querySelector('.carousel-container');
    carouselContainer.addEventListener('mouseenter', stopAutoScroll);
    carouselContainer.addEventListener('mouseleave', startAutoScroll);
    
    // Configurar filtros de proyectos
    const filterButtons = document.querySelectorAll('.filtro-btn');
    
    // Event listeners para los botones de filtro
    filterButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const filterType = event.target.getAttribute('data-filter');
            filtrarProyectos(filterType);
        });
    });
    
    // Inicializar con todos los proyectos visibles
    const tarjetasProyecto = document.querySelectorAll('.tarjetaproyecto');
    setTimeout(() => {
        tarjetasProyecto.forEach(tarjeta => {
            tarjeta.style.opacity = '1';
            tarjeta.style.transform = 'translateY(0)';
        });
    }, 100);
});
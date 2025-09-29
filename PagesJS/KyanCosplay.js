// Lightbox simple
const lightbox = document.getElementById('lightbox');
const lightboxImg = lightbox.querySelector('img');

document.querySelectorAll('.imagen-item img').forEach(img => {
    img.addEventListener('click', () => {
        lightbox.style.display = 'flex';
        lightboxImg.src = img.src;
    });
});

lightbox.addEventListener('click', () => {
    lightbox.style.display = 'none';
    lightboxImg.src = '';
});


function openPDFViewer(pdfUrl) {
    const overlay = document.getElementById('pdf-viewer-overlay');
    const iframe = document.getElementById('pdf-viewer-frame');
    iframe.src = pdfUrl;
    overlay.style.display = 'flex';
}

function closePDFViewer() {
    const overlay = document.getElementById('pdf-viewer-overlay');
    const iframe = document.getElementById('pdf-viewer-frame');
    iframe.src = ''; // limpia la URL
    overlay.style.display = 'none';
}

// Evitar que clics dentro del iframe cierren el overlay
document.getElementById('pdf-viewer-frame').addEventListener('click', function(event){
    event.stopPropagation();
});

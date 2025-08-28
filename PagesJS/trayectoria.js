// --- Menú hamburguesa existente ---
function toggleMenu() {
  const navMenu = document.querySelector(".navmenu");
  navMenu.classList.toggle("active");
}

// --- Modal PDFs / Imágenes ---
function openMedia(url, type) {
  const modal = document.getElementById("pdfModal");
  const iframe = document.getElementById("pdfFrame");
  const img = document.getElementById("imgFrame");

  // Ocultamos ambos primero
  iframe.style.display = "none";
  img.style.display = "none";

  if (type === "pdf") {
    iframe.src = url;
    iframe.style.display = "block";
  } else if (type === "image") {
    img.src = url;
    img.style.display = "block";
  }

  modal.style.display = "block";
}

function closePDF() {
  const modal = document.getElementById("pdfModal");
  const iframe = document.getElementById("pdfFrame");
  const img = document.getElementById("imgFrame");

  modal.style.display = "none";
  iframe.src = "";
  img.src = "";
}

// Cerrar modal al hacer clic fuera
window.onclick = function(event) {
  const modal = document.getElementById("pdfModal");
  if (event.target === modal) {
    closePDF();
  }
};

const modal = document.getElementById("comingSoonModal");
const closeBtn = document.querySelector(".close-modal");

document.querySelectorAll("a").forEach((link) => {
  if (!link.classList.contains("close-modal")) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      openModal();
    });
  }
});

function openModal() {
  modal.style.display = "block";
  modal.classList.remove("fade-out");
}

function closeModal() {
  modal.classList.add("fade-out");
  setTimeout(() => {
    modal.style.display = "none";
    modal.classList.remove("fade-out");
  }, 300);
}

closeBtn.onclick = closeModal;

window.onclick = function (event) {
  if (event.target == modal) {
    closeModal();
  }
};

// Mobile menu toggle
const menuToggle = document.querySelector(".menu-toggle");
const ctaButtons = document.querySelector(".cta-buttons");

menuToggle.addEventListener("click", () => {
  ctaButtons.classList.toggle("active");
});

// Close menu when clicking outside
document.addEventListener("click", (e) => {
  if (!e.target.closest(".navbar")) {
    ctaButtons.classList.remove("active");
  }
});

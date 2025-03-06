/**
 * Swordindex - JavaScript Functionality
 * Handles modal functionality, mobile menu, and other interactive elements
 */

// Mobile menu functionality
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("mobile-menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", function () {
      if (mobileMenu.classList.contains("hidden")) {
        mobileMenu.classList.remove("hidden");
      } else {
        mobileMenu.classList.add("hidden");
      }
    });

    // Close menu when clicking on a link
    const menuLinks = mobileMenu.querySelectorAll("a");
    menuLinks.forEach((link) => {
      link.addEventListener("click", function () {
        mobileMenu.classList.add("hidden");
      });
    });

    // Close menu when clicking outside
    document.addEventListener("click", function (event) {
      if (
        !event.target.closest("#mobile-menu") &&
        !event.target.closest("#mobile-menu-toggle") &&
        !mobileMenu.classList.contains("hidden")
      ) {
        mobileMenu.classList.add("hidden");
      }
    });
  }

  // Add smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      if (this.getAttribute("href") === "#") return;

      e.preventDefault();
      const targetId = this.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: "smooth",
        });
      }
    });
  });

  // Close modal when clicking outside of content
  const modal = document.getElementById("privacyModal");
  if (modal) {
    modal.addEventListener("click", function (event) {
      if (event.target === modal) {
        closeModal();
      }
    });
  }

  // Carousel Functionality
  initCarousel();
});

// HTMX form handling
document.addEventListener("htmx:afterRequest", function (event) {
  // This is a mock response since we don't have a real backend
  if (event.detail.target && event.detail.target.id === "form-response") {
    const formData = new FormData(event.detail.elt);
    const formValues = {};

    for (const [key, value] of formData.entries()) {
      formValues[key] = value;
    }

    // Validate form data
    if (!formValues.comp || !formValues.mail || !formValues.cont) {
      event.detail.target.className =
        "mt-4 p-4 bg-red-900/30 border border-red-500 rounded-lg text-center";
      event.detail.target.innerHTML = "모든 필드를 채워주세요.";
      return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formValues.mail)) {
      event.detail.target.className =
        "mt-4 p-4 bg-red-900/30 border border-red-500 rounded-lg text-center";
      event.detail.target.innerHTML = "유효한 이메일 주소를 입력해주세요.";
      return;
    }

    // Success response
    event.detail.target.className =
      "mt-4 p-4 bg-primary/10 border border-primary rounded-lg text-center";
    event.detail.target.innerHTML =
      "문의가 성공적으로 제출되었습니다. 곧 연락드리겠습니다.";

    // Reset form
    event.detail.elt.reset();
  }
});

// Function to initialize carousel
function initCarousel() {
  // Get carousel elements
  const carousel = document.getElementById("carousel");
  const carouselInner = document.getElementById("carousel-inner");
  const prevBtn = document.getElementById("prev-btn");
  const nextBtn = document.getElementById("next-btn");
  const indicators = document.querySelectorAll(".slide-indicator");

  // Check if carousel elements exist
  if (!carousel || !carouselInner) {
    console.log("Primary carousel elements not found");
    return;
  }

  console.log("Carousel found:", carousel);
  console.log("Carousel inner found:", carouselInner);

  let currentIndex = 0;
  const slideCount = carouselInner.children.length;

  console.log("Carousel initialized with", slideCount, "slides");

  // Initialize carousel
  updateCarousel();

  // Next slide button
  if (nextBtn) {
    console.log("Next button found");
    nextBtn.addEventListener("click", function () {
      console.log("Next button clicked");
      currentIndex = (currentIndex + 1) % slideCount;
      updateCarousel();
    });
  }

  // Previous slide button
  if (prevBtn) {
    console.log("Prev button found");
    prevBtn.addEventListener("click", function () {
      console.log("Prev button clicked");
      currentIndex = (currentIndex - 1 + slideCount) % slideCount;
      updateCarousel();
    });
  }

  // Indicator buttons
  if (indicators.length > 0) {
    console.log("Indicators found:", indicators.length);
    indicators.forEach((indicator, idx) => {
      indicator.addEventListener("click", function () {
        console.log("Indicator clicked:", idx);
        currentIndex = parseInt(this.dataset.index || idx);
        updateCarousel();
      });
    });
  }

  // Auto slide every 5 seconds
  let interval = setInterval(() => {
    currentIndex = (currentIndex + 1) % slideCount;
    updateCarousel();
  }, 5000);

  // Pause auto slide on hover
  carousel.addEventListener("mouseenter", () => {
    clearInterval(interval);
  });

  // Resume auto slide when mouse leaves
  carousel.addEventListener("mouseleave", () => {
    interval = setInterval(() => {
      currentIndex = (currentIndex + 1) % slideCount;
      updateCarousel();
    }, 5000);
  });

  // Function to update carousel position and indicators
  function updateCarousel() {
    console.log("Updating carousel to index:", currentIndex);

    // Update slide position
    carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;

    // Update indicators
    if (indicators.length > 0) {
      indicators.forEach((indicator, index) => {
        if (index === currentIndex) {
          indicator.classList.add("bg-white");
          indicator.classList.remove("bg-white/50");
        } else {
          indicator.classList.remove("bg-white");
          indicator.classList.add("bg-white/50");
        }
      });
    }
  }
}

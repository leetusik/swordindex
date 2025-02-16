const modal = document.getElementById("comingSoonModal");
const closeBtn = document.querySelector(".close-modal");

document.querySelectorAll(".nav-links a, .cta-buttons a").forEach((link) => {
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

// Email form handling
const waitlistForm = document.getElementById("waitlistForm");
const thankYouModal = document.getElementById("thankYouModal");

// Add this at the top of the file with other constants
const messageContainer = document.createElement("div");
messageContainer.className = "message-container";
document.body.appendChild(messageContainer);

function showMessage(message, type = "error") {
  const messageElement = document.createElement("div");
  messageElement.className = `message ${type}`;
  messageElement.innerHTML = `
        ${message}
        <span class="message-close">×</span>
    `;

  messageContainer.appendChild(messageElement);

  // Remove message after 5 seconds
  setTimeout(() => {
    messageElement.remove();
  }, 5000);

  // Allow manual close
  messageElement.querySelector(".message-close").onclick = () => {
    messageElement.remove();
  };
}

waitlistForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const email = document.getElementById("emailInput").value;

  if (validateEmail(email)) {
    try {
      const response = await fetch("/emails/collect/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: `email=${encodeURIComponent(email)}`,
      });

      if (response.ok) {
        openThankYouModal();
        waitlistForm.reset();
      } else {
        showMessage(
          "This email is already registered. Please try a different one."
        );
      }
    } catch (error) {
      showMessage(
        "There was an error submitting your email. Please try again later."
      );
    }
  } else {
    showMessage("Please enter a valid email address.");
  }
});

// Helper function to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function validateEmail(email) {
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(email);
}

function openThankYouModal() {
  thankYouModal.style.display = "block";
  thankYouModal.classList.remove("fade-out");
}

function closeThankYouModal() {
  thankYouModal.classList.add("fade-out");
  setTimeout(() => {
    thankYouModal.style.display = "none";
    thankYouModal.classList.remove("fade-out");
  }, 300);
}

// Update window click handler to include both modals
window.onclick = function (event) {
  if (event.target == modal) {
    closeModal();
  }
  if (event.target == thankYouModal) {
    closeThankYouModal();
  }
};

// Add close button handler for thank you modal
document.querySelector("#thankYouModal .close-modal").onclick =
  closeThankYouModal;

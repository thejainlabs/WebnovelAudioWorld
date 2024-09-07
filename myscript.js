// Search Script - index.html
document.getElementById("novelSearch").addEventListener("keyup", function() {
          let input = this.value.toLowerCase();
          
          let cards = document.querySelectorAll(".card");
          

          cards.forEach(function(card) {
            let novelName = card.querySelector(".novel-name").textContent.toLowerCase();
            if (novelName.includes(input)) {
              card.parentElement.style.display = ""; //Show the card
            } else {
              card.parentElement.style.display = "none"; // hide the card
            }
          });
        });

// Search Script - Table of Content Page
document.getElementById("novelSearch").addEventListener("keyup", function() {
      let input = this.value.toLowerCase();
      let cards = document.querySelectorAll(".novel-item");
      cards.forEach(function(card) {
        let novelName = card.querySelector(".novel-title").textContent.toLowerCase();
        if (novelName.includes(input)) {
              card.style.display = ""; // Show the card
            } else {
              card.style.display = "none"; // Hide the card
            }
          });
    });

// Search Script - Chapter list page

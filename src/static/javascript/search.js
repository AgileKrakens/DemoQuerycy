document.addEventListener("DOMContentLoaded", () => {
    const filterBox = document.querySelector(".filter-box");
    const cards = document.querySelectorAll(".card");

    filterBox.addEventListener("input", (event) => {
        const searchText = event.target.value.toLowerCase();
        
        cards.forEach(card => {
            const name = card.querySelector(".name").textContent.toLowerCase();
            if (name.includes(searchText)) {
                card.style.display = "block"; // Exibe o card
            } else {
                card.style.display = "none";  // Oculta o card
            }
        });
    });
});
 
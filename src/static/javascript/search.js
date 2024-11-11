document.addEventListener("DOMContentLoaded", () => {
    const filterBox = document.querySelector(".filter-box");
    const cards = document.querySelectorAll(".card");
    const noResultsMessage = document.querySelector(".no-results");

    filterBox.addEventListener("input", (event) => {
        const searchText = event.target.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
        let hasResults = false;

        cards.forEach(card => {
            const name = card.querySelector(".name").textContent.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            const descricao = card.querySelector(".descricao").textContent.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            if (name.includes(searchText) || descricao.includes(searchText)) {
                card.style.display = "block"; // Exibe o card
                hasResults = true;
            } else {
                card.style.display = "none";  // Oculta o card
            }
        });

        noResultsMessage.style.display = hasResults ? "none" : "block";
    });
});
 
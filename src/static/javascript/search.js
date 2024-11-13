document.addEventListener("DOMContentLoaded", () => {
    const filterBox = document.querySelector(".filter-box");
    const cards = document.querySelectorAll(".card");
    const noResultsMessage = document.querySelector(".no-results");
    const resultados = document.querySelector(".resultados");

    filterBox.addEventListener("input", (event) => {
        const searchText = event.target.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        // Se a barra de pesquisa estiver vazia, remova a classe 'filtered' e mostre todos os cards
        if (searchText.trim() === "") {
            resultados.classList.remove("filtered");
            cards.forEach(card => {
                card.style.display = "inline"; // Exibe todos os cards
            });
            noResultsMessage.style.display = "none"; // Oculta a mensagem de 'sem resultados'
            return; // Sai do evento, pois não há mais nada a fazer
        }

        let hasResults = false;

        cards.forEach(card => {
            const name = card.querySelector(".name").textContent.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            const descricao = card.querySelector(".descricao").textContent.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            if (name.includes(searchText) || descricao.includes(searchText)) {
                card.style.display = "inline"; // Exibe o card
                hasResults = true;
            } else {
                card.style.display = "none"; // Oculta o card
            }
        });

        // Se há resultados, adicione a classe 'filtered' ao container; caso contrário, remova
        if (hasResults) {
            resultados.classList.add("filtered");
        } else {
            resultados.classList.remove("filtered");
        }

        noResultsMessage.style.display = hasResults ? "none" : "block";
    });
});

function filterCards() {
    const searchInput = document.getElementById('searchBar').value.toLowerCase();
    const cards = document.querySelectorAll('.politician-card');
    let found = false;

    cards.forEach(card => {
        const politicianName = card.querySelector('.card-title').textContent.toLowerCase();
        if (politicianName.includes(searchInput)) {
            card.style.display = ''; // Show card
            found = true; // At least one card is found
        } else {
            card.style.display = 'none'; // Hide card
        }
    });

    // Show or hide the "Nenhum político encontrado" message
    const noPoliticiansMessage = document.getElementById('noPoliticiansMessage');
    if (found) {
        noPoliticiansMessage.style.display = 'none'; // Hide message
    } else {
        noPoliticiansMessage.style.display = 'flex'; // Show message
    }
}
document.addEventListener('DOMContentLoaded', function() {
    
//show more/less button
    const cards = document.querySelectorAll('.favorite-mini-card');
    const show_more = document.querySelector('#show-more-button');
    
    let initialCount = 8;
    let currentlyShown = initialCount;

    cards.forEach((card, index) => {
        if (index >= currentlyShown) {
            card.classList.add('hidden-card');
        }
    });

    show_more.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (this.classList.contains('showing-all')) {

            currentlyShown = initialCount;
            
            cards.forEach((card, index) => {
                if (index >= currentlyShown) {
                    card.classList.add('hidden-card');
                }
            });
            
            this.innerHTML = 'Show More';
            this.classList.remove('showing-all');

        } else {
            
            for (let i = currentlyShown; i < currentlyShown + 8; i++) {
                if (cards[i]) {
                    cards[i].classList.remove('hidden-card');
                }
            }
            
            currentlyShown += 8;

            if (currentlyShown >= cards.length) {
                this.innerHTML = 'Show Less';
                this.classList.add('showing-all'); 
            }
        }
    });
});
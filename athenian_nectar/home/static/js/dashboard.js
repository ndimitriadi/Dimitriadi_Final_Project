document.addEventListener('DOMContentLoaded', function() {
    
    function show_more_button(grid_selector, button_selector, counter) {
        
        const grid = document.querySelector(grid_selector);
        const button = document.querySelector(button_selector);

        const cards = grid.querySelectorAll('.favorite-mini-card');
        let shown_cards = counter;

        cards.forEach((card, index) => {
            if (index >= shown_cards) {
                card.classList.add('hidden-card');
            }
        });

        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            if (this.classList.contains('showing-all')) {
                shown_cards = counter;
                
                cards.forEach((card, index) => {
                    if (index >= shown_cards) {
                        card.classList.add('hidden-card');
                    }
                });
                
                this.innerHTML = 'Show More';
                this.classList.remove('showing-all');

            } else {
                for (let i = shown_cards; i < shown_cards + counter; i++) {
                    if (cards[i]) {
                        cards[i].classList.remove('hidden-card');
                    }
                }
                
                shown_cards += counter;

                if (shown_cards >= cards.length) {
                    this.innerHTML = 'Show Less';
                    this.classList.add('showing-all'); 
                }
            }
        });
    }
    show_more_button('#favorites-grid', '#favorites-show-more-button', 8);
    show_more_button('#ratings-grid', '#ratings-show-more-button', 8);
});
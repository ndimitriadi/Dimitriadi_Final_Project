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

document.addEventListener('DOMContentLoaded', function() {
        const order_button = document.querySelector('#orders-toggle-button');
        const extra_order = document.querySelectorAll('.extra-order');
        
        if (order_button && extra_order.length > 0) {
            
            extra_order.forEach(order => order.style.display = 'none');
            order_button.innerHTML = 'Show More';
            order_button.setAttribute('data-expanded', 'false');

            order_button.addEventListener('click', function(e) {
                e.preventDefault();
                
                const is_open = order_button.getAttribute('data-expanded') === 'true';

                if (is_open) {
                    //close
                    extra_order.forEach(order => order.style.display = 'none');
                    order_button.innerHTML = 'Show More';
                    order_button.setAttribute('data-expanded', 'false'); 
                } else {
                    extra_order.forEach(order => order.style.display = 'block');
                    order_button.innerHTML = 'Show Less';
                    order_button.setAttribute('data-expanded', 'true'); 
                }
            });
        }
    });
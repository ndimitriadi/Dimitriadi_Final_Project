document.addEventListener('DOMContentLoaded', function() {
    
    const stars = document.querySelectorAll('.star-icon');
    const hidden_rating = document.querySelector('#hidden_rating'); 
    const review_form = document.querySelector('#ajax-review-form');
    const star_error = document.querySelector('#star-error'); 
    let current_rating = 0;

    // Hover effects
    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            highlightStars(this.getAttribute('data-value'));
        });
        
        star.addEventListener('mouseout', function() {
            highlightStars(current_rating);
        });
        
        star.addEventListener('click', function() {
            current_rating = this.getAttribute('data-value');
            if(hidden_rating) hidden_rating.value = current_rating; 
            highlightStars(current_rating);
            
            if(star_error) star_error.style.display = 'none'; 
        });
    });

    function highlightStars(val) {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= val) {
                star.classList.remove('bi-star');
                star.classList.add('bi-star-fill', 'active');
            } else {
                star.classList.remove('bi-star-fill', 'active');
                star.classList.add('bi-star');
            }
        });
    }

    //no starts selected
    if (review_form) {
        review_form.addEventListener('submit', function(e) {
            if (!hidden_rating.value || hidden_rating.value === "0") {
                e.preventDefault();
                if (star_error) {
                    star_error.style.display = 'inline-block';
                }
            }
        });
    }
});
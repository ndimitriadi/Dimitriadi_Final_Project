// WEATHER API
async function athens_weather() {
    // Athens coordinates
    const latitude = 37.9838;
    const longitude = 23.7275;
    
    // Open-Meteo URL - making the request
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,weather_code`;

    const weather_description = document.querySelector('#weather-description');
    const weather_temperature = document.querySelector('#weather-temperature');
    const weather_icon = document.querySelector('#weather-icon');

    try {
        const response = await fetch(url);
        const data = await response.json();
        
        //temperature and weather code
        const temp = Math.round(data.current.temperature_2m);
        const code = data.current.weather_code;

        let condition = "Clear";
        let iconClass = "bi-sun";

        if (code === 0) { 
            condition = "Clear Sky"; 
            iconClass = "bi-sun"; 
        }
        else if (code >= 1 && code <= 3) { 
            condition = "Cloudy"; 
            iconClass = "bi-clouds"; 
        }
        else if (code >= 45 && code <= 48) { 
            condition = "Foggy"; 
            iconClass = "bi-cloud-haze"; 
        }
        else if (code >= 51 && code <= 67) { 
            condition = "Rainy"; 
            iconClass = "bi-cloud-rain"; 
        }
        else if (code >= 71 && code <= 77) { 
            condition = "Snowy"; 
            iconClass = "bi-snow"; 
        }
        else if (code >= 95 && code <= 99) { 
            condition = "Thunderstorms"; 
            iconClass = "bi-cloud-lightning-rain"; 
        }

        weather_temperature.textContent = temp + '°C';
        weather_description.textContent = condition;
        weather_icon.className = `bi ${iconClass}`;

    } catch (error) {
        console.error("Error fetching weather:", error);
        weather_description.textContent = "Weather unavailable";
        weather_icon.className = "bi bi-cloud-slash";
    }
}

document.addEventListener("DOMContentLoaded", athens_weather);


// SEARCH BUTTON
document.addEventListener('DOMContentLoaded', () => {
    const blog_search = document.querySelector('#blog-search');
    const blog_card = document.querySelectorAll('.blog-card');
    const no_results_message = document.querySelector('#no-results-message'); 

    blog_search.addEventListener('input', (e) => {
        const search_input = e.target.value.toLowerCase();
        
        let reults_counter = 0; 

        blog_card.forEach(card => {
           const titleElement = card.querySelector('h3');
                const title = titleElement ? titleElement.innerText.toLowerCase() : "";
                
                // This single element holds BOTH your Category and Subcategory text!
                const categoryElement = card.querySelector('.blog-category');
                const categories = categoryElement ? categoryElement.innerText.toLowerCase() : "";
            

            if (title.includes(search_input) || categories.includes(search_input)) {
                card.style.display = 'flex'; 
                reults_counter++; 
            } else {
                card.style.display = 'none'; 
            }
        });

        if (no_results_message) {
            if (reults_counter === 0) {
                no_results_message.style.display = 'block'; 
            } else {
                no_results_message.style.display = 'none'; 
            }
        }
    });
});

//FILTERING
document.addEventListener('DOMContentLoaded', () => {

    const blog_search = document.querySelector('#blog-search');
    const category_filter = document.querySelector('#category-filter');
    const subcategory_filter = document.querySelector('#subcategory-filter');
    const duration_filter = document.querySelector('#duration-filter');
    const duration_value_display = document.querySelector('#duration-value'); 
    const price_filter = document.querySelector('#price-filter');
    const price_value_display = document.querySelector('#price-value');
    const blog_cards = document.querySelectorAll('.blog-card');
    const no_results_message = document.querySelector('#no-results-message'); 

    function applyFilters() {
        //getting user inputs
        const searchText = blog_search.value.toLowerCase();
        const catFilter = category_filter.value.toLowerCase();
        const subFilter = subcategory_filter.value.toLowerCase();
        const maxDur = parseFloat(duration_filter.value);
        const maxPrice = parseFloat(price_filter.value);

        let results_counter = 0; 

        blog_cards.forEach(card => {
            //reading data from each card
            const titleElement = card.querySelector('h3');
            const cardTitle = titleElement.innerText.toLowerCase();
            const cardCat = card.getAttribute('data-category');
            const cardSub = card.getAttribute('data-subcategory');
            const cardDur = parseFloat(card.getAttribute('data-duration'));
            const cardPrice = parseFloat(card.getAttribute('data-price'));

            //checks if cards passes filters
            const passesText = cardTitle.includes(searchText);
            const passesCat = (catFilter === "") || (cardCat === catFilter);
            const passesSub = (subFilter === "") || (cardSub === subFilter);
            const passesDur = cardDur <= maxDur;
            const passesPrice = cardPrice <= maxPrice;

            //show or hide the card
            if (passesText && passesCat && passesSub && passesDur && passesPrice) {
                card.style.display = 'flex'; 
                results_counter++; 
            } else {
                card.style.display = 'none'; 
            }
        });

        if (no_results_message) {
            if (results_counter === 0) {
                no_results_message.style.display = 'block';
            } else {
                no_results_message.style.display = 'none';
            }
        }
    }

    const inputs = [blog_search, category_filter, subcategory_filter];
    inputs.forEach(input => {
        if (input.tagName === 'SELECT') {
            input.addEventListener('change', applyFilters);
        } else {
            input.addEventListener('input', applyFilters);
        }
    });

    //reseting subcategory
    if (category_filter && subcategory_filter) {
        category_filter.addEventListener('change', () => {
            const selectedCategory = category_filter.value.toLowerCase();
            const subOptions = subcategory_filter.querySelectorAll('option');

            subcategory_filter.value = "";

            subOptions.forEach(option => {
                if (option.value === "") {
                    option.style.display = 'block';
                    return;
                }
                const parentCategory = option.getAttribute('data-parent');
                if (selectedCategory === "" || parentCategory === selectedCategory) {
                    option.style.display = 'block';
                } else {
                    option.style.display = 'none';
                }
            });
            applyFilters(); 
        });
    }

    //price slider
    price_filter.addEventListener('input', (e) => {
        if (price_value_display) {
            price_value_display.textContent = e.target.value; 
        }
        applyFilters();
    });
    
    //duration slider
    duration_filter.addEventListener('input', (e) => {
        if (duration_value_display) {
            duration_value_display.textContent = e.target.value; 
        }
        applyFilters();
    });

});


//SAVE BUTTON
document.addEventListener('DOMContentLoaded', function() {
    
    const save_button = document.querySelectorAll('.save-button');

    save_button.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); 
            
            const authorized = this.getAttribute('data-auth') === 'true';
            
            //if not logged in
            if (!authorized) {
                window.location.href = '/users/login/'; 
                return;
            }

            //if logged in
            const itemId = this.getAttribute('data-id');
            const icon = this.querySelector('i');

            //making a POST request to save the favorite
            fetch(`/users/favorite/${itemId}/`, {
                method: 'POST',
                headers: { //tells the server how to handle the request
                    'X-CSRFToken': getCookie('csrftoken'), //security
                }
            })
            .then(response => response.json())
            .then(data => {
                //icon change 
                if (data.is_favorited) {
                    icon.classList.remove('bi-bookmark');
                    icon.classList.add('bi-bookmark-fill');
                    
                } else {
                    icon.classList.remove('bi-bookmark-fill');
                    icon.classList.add('bi-bookmark');
                }
            });
        });
    });

    // Helper function to grab Django's CSRF token for the fetch request
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
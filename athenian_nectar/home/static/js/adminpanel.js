//no negative numbers
const numberInputs = document.querySelectorAll('#tasks_form input[type="number"]');
numberInputs.forEach(input => {
    input.setAttribute('min', '0');
    
    //ratings max is 5
    if (input.name === 'rating') input.setAttribute('max', '5');

    //the user cant type -
    input.addEventListener('input', function() {
        if (this.value < 0) this.value = 0; 
    });
});

//subcategories corresponding to categories 
const categories = document.querySelector('#tasks_form [name="category"]');
const subcategories = document.querySelector('#tasks_form [name="subcategory"]');
const all_subcategories = Array.from(subcategories.options);

const map_element = document.querySelector('#dynamic-category-map');
let category_map;
if (map_element) {
  category_map = JSON.parse(map_element.textContent);
} else {
  category_map = {};
}

categories.addEventListener('change', function() {
    const selected_category = this.options[this.selectedIndex].text;
    const allowed_subcategories = category_map[selected_category] || [];

    subcategories.innerHTML = '';

    all_subcategories.forEach(option => {
        const clean_option = option.cloneNode(true);
        if (clean_option.text.includes(" - ")) {
            clean_option.text = clean_option.text.split(" - ").pop();
        }

        if (option.value === "" || allowed_subcategories.includes(option.value)) {
            subcategories.appendChild(clean_option);
        }
    });
});
    

//experiences table
document.addEventListener('DOMContentLoaded', function() {
    
    const table = document.querySelector('#experience_table');
    const form = document.querySelector('#tasks_form');
    const form_title = document.querySelector('#form_title'); 
    const save_button = document.querySelector('#save_button');  
    const hidden_id = document.querySelector('#hidden_experience_id');
    const cancel_button = document.querySelector('#cancel_task_button');
    const image = document.querySelector('input[type="file"]');

    //edit button
    table.addEventListener('click', function(e) {
        const edit_button = e.target.closest('.edit-btn');
        const row = edit_button.closest('.table-row');
        const title = row.getAttribute('data-title') || "";
        const category = row.getAttribute('data-category') || "";
        const subcategory = row.getAttribute('data-subcategory') || "";
        const price = row.getAttribute('data-price') || "";
        const descriptionDiv = row.querySelector('.hidden-description');
        const descriptionText = descriptionDiv ? descriptionDiv.textContent : "";

        document.querySelector('#tasks_form [name="title"]').value = title;
        document.querySelector('#tasks_form [name="category"]').value = category;
        document.querySelector('#tasks_form [name="subcategory"]').value = subcategory;
        document.querySelector('#tasks_form [name="price"]').value = parseFloat(price || 0).toFixed(2);
        document.querySelector('#tasks_form [name="description"]').value = descriptionText;
        document.querySelector('#tasks_form [name="duration"]').value = row.getAttribute('data-duration') || "";
        document.querySelector('#tasks_form [name="rating"]').value = row.getAttribute('data-rating') || "5.0";
        document.querySelector('#tasks_form [name="total_reviews"]').value = row.getAttribute('data-total_reviews') || "0";
        
        if (image) image.removeAttribute('required');
        
        if (hidden_id) hidden_id.value = row.getAttribute('data-id');

        if (form_title) form_title.innerHTML = `Edit Experience`;
        if (save_button) save_button.innerText = "Update";
        
        window.scrollTo({ top: 0, behavior: 'smooth' });;
    });

    //cancel button
    if (cancel_button) {
        cancel_button.addEventListener('click', function(e) {
            e.preventDefault();
            
            form.reset(); 
            if (hidden_id) hidden_id.value = ""; 
            
            if (image) image.setAttribute('required', 'required');
            
            if (form_title) form_title.innerText = "Add Experience";
            if (save_button) save_button.innerText = "Save";
        });
    }
});


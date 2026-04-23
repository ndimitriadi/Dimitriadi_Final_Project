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

document.addEventListener('DOMContentLoaded', function() {
//experiences page
    const exp_table = document.querySelector('#experience_table');
    const exp_form = document.querySelector('#tasks_form');

    if (exp_table && exp_form) {
        
        //smart subcategories
        const categories = document.querySelector('#tasks_form [name="category"]');
        const subcategories = document.querySelector('#tasks_form [name="subcategory"]');
        
        if (categories && subcategories) {
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
        }

        //edit/cancel
        const form_title = document.querySelector('#form_title'); 
        const save_button = document.querySelector('#save_button');  
        const hidden_id = document.querySelector('#hidden_experience_id');
        const cancel_button = document.querySelector('#cancel_task_button');
        const image = document.querySelector('input[type="file"]');

        exp_table.addEventListener('click', function(e) {
            const edit_button = e.target.closest('.edit-btn');
            const row = edit_button.closest('.table-row');
            
            const title = row.getAttribute('data-title') || "";
            const category = row.getAttribute('data-category') || "";
            const subcategory = row.getAttribute('data-subcategory') || "";
            const price = row.getAttribute('data-price') || "";
            const descriptionDiv = row.querySelector('.hidden-description');
            const descriptionText = descriptionDiv ? descriptionDiv.textContent : "";

            document.querySelector('#tasks_form [name="title"]').value = title;
            
            const catInput = document.querySelector('#tasks_form [name="category"]');
            if (catInput) {
                catInput.value = category;
                catInput.dispatchEvent(new Event('change'));
            }

            document.querySelector('#tasks_form [name="subcategory"]').value = subcategory;
            document.querySelector('#tasks_form [name="price"]').value = parseFloat(price || 0).toFixed(2);
            document.querySelector('#tasks_form [name="description"]').value = descriptionText;
            document.querySelector('#tasks_form [name="duration"]').value = row.getAttribute('data-duration') || "";
            
            if (image) image.removeAttribute('required');
            if (hidden_id) hidden_id.value = row.getAttribute('data-id');
            if (form_title) form_title.innerHTML = `Edit Experience`;
            if (save_button) save_button.innerText = "Update";
            
            console.log("CLICK WORKS");
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        cancel_button.addEventListener('click', function(e) {
            e.preventDefault();
            exp_form.reset(); 
            if (hidden_id) hidden_id.value = ""; 
            if (image) image.setAttribute('required', 'required');
            if (form_title) form_title.innerText = "Add Experience";
            if (save_button) save_button.innerText = "Save";
        });

    }


    //category page
    const cat_table = document.querySelector('#category_table');
    const cat_form = document.querySelector('#category_form');

    if (cat_table && cat_form) {
        
        const category_form_title = document.querySelector('#form_title'); 
        const category_save_button = document.querySelector('#save_button');  
        const category_id = document.querySelector('#hidden_category_id');
        const category_cancel_button = document.querySelector('#cancel_category_button');

        //edit/cancel
        cat_table.addEventListener('click', function(e) {
            const category_edit_button = e.target.closest('.edit-btn');
            const row = category_edit_button.closest('.table-row');
            
            const name = row.getAttribute('data-name') || "";
            document.querySelector('#category_form [name="name"]').value = name;

            if (category_id) category_id.value = row.getAttribute('data-id');
            if (category_form_title) category_form_title.innerHTML = `Edit Category`;
            if (category_save_button) category_save_button.innerText = "Update";
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });


        category_cancel_button.addEventListener('click', function(e) {
            e.preventDefault();
            cat_form.reset(); 
            if (category_id) category_id.value = ""; 
            if (category_form_title) category_form_title.innerText = "Add Category";
            if (category_save_button) category_save_button.innerText = "Save";
        });
    }

//subcategory page
    const subcat_table = document.querySelector('#subcategory_table');
    const subcat_form = document.querySelector('#subcategory_form');

    if (subcat_table && subcat_form) {
        
        const subcategory_form_title = document.querySelector('#form_title'); 
        const subcategory_save_button = document.querySelector('#save_button');  
        const subcategory_id = document.querySelector('#hidden_subcategory_id');
        const subcategory_cancel_button = document.querySelector('#cancel_subcategory_button');

        subcat_table.addEventListener('click', function(e) {
            const subcategory_edit_button = e.target.closest('.edit-btn');
            const row = subcategory_edit_button.closest('.table-row');
            
            const name = row.getAttribute('data-name') || "";
            document.querySelector('#subcategory_form [name="name"]').value = name;

            const category_id = row.getAttribute('data-category') || "";
            document.querySelector('#subcategory_form [name="category"]').value = category_id;

            if (subcategory_id) subcategory_id.value = row.getAttribute('data-id');
            if (subcategory_form_title) subcategory_form_title.innerHTML = `Edit Subcategory`;
            if (subcategory_save_button) subcategory_save_button.innerText = "Update";
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

    
        subcategory_cancel_button.addEventListener('click', function(e) {
            e.preventDefault();
            subcat_form.reset(); 
            if (subcategory_id) subcategory_id.value = ""; 
            if (subcategory_form_title) subcategory_form_title.innerText = "Add Subcategory";
            if (subcategory_save_button) subcategory_save_button.innerText = "Save";
        });
    
    }

//testimonials page
    const test_table = document.querySelector('#testimonial_table');
    const test_form = document.querySelector('#testimonial_form');

    if (test_table && test_form) {
        
        const t_form_title = document.querySelector('#form_title'); 
        const t_save_button = document.querySelector('#save_button');  
        const t_id = document.querySelector('#hidden_testimonial_id');
        const t_cancel_button = document.querySelector('#cancel_testimonial_button');

        test_table.addEventListener('click', function(e) {
            const t_edit_button = e.target.closest('.edit-btn');

            const row = t_edit_button.closest('.table-row');
            
            const name = row.getAttribute('data-name') || "";
            const role = row.getAttribute('data-role') || "";
            const stars = row.getAttribute('data-stars') || "";
            
            const quoteDiv = row.querySelector('.hidden-quote');
            const quoteText = quoteDiv ? quoteDiv.textContent : "";

            document.querySelector('#testimonial_form [name="name"]').value = name;
            document.querySelector('#testimonial_form [name="role"]').value = role;
            document.querySelector('#testimonial_form [name="quote"]').value = quoteText;
            document.querySelector('#testimonial_form [name="stars"]').value = stars;

            if (t_id) t_id.value = row.getAttribute('data-id');
            if (t_form_title) t_form_title.innerHTML = `Edit Testimonial`;
            if (t_save_button) t_save_button.innerText = "Update";
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        t_cancel_button.addEventListener('click', function(e) {
            e.preventDefault();
            test_form.reset(); 
            if (t_id) t_id.value = ""; 
            if (t_form_title) t_form_title.innerText = "Add Testimonial";
            if (t_save_button) t_save_button.innerText = "Save";
        });
    }


//users page
    const user_table = document.querySelector('#user_table');
    const user_form = document.querySelector('#user_form');

    if (user_table && user_form) {
        
        const user_form_title = document.querySelector('#form_title'); 
        const user_save_button = document.querySelector('#save_button');  
        const user_id = document.querySelector('#hidden_user_id');
        const user_cancel_button = document.querySelector('#cancel_user_button');

        const old_password = document.querySelector('#user_form [name="old_password"]');
        let old_password_row = null;
        if (old_password) {
        old_password_row = old_password.closest('.form-rows');
        }
        
        if (user_id && user_id.value !== "") {
            old_password_row.style.display = ''; 
            if (user_form_title) user_form_title.innerHTML = `Edit User`;
            if (user_save_button) user_save_button.innerText = "Update User";
        } else {
            old_password_row.style.display = 'none'; 
        }
        
        user_table.addEventListener('click', function(e) {
            
            const user_edit_button = e.target.closest('.edit-btn');
            const row = user_edit_button.closest('.table-row');
            
            const username = row.getAttribute('data-username') || "";
            const email = row.getAttribute('data-email') || "";
            const status = row.getAttribute('data-status') || "user";

            document.querySelector('#user_form [name="username"]').value = username;
            document.querySelector('#user_form [name="email"]').value = email;
            document.querySelector('#user_form [name="status"]').value = status;
            
            const new_password = document.querySelector('#user_form [name="password"]');
            if (old_password) old_password.value = "";
            if (new_password) new_password.value = "";

            //show previous password field
            if (old_password_row) {
                old_password_row.style.display = ''; 
            }

            //this id tells us which user we need to update
            if (user_id) user_id.value = row.getAttribute('data-id');
            
            if (user_form_title) user_form_title.innerHTML = `Edit User`;
            if (user_save_button) user_save_button.innerText = "Update User";
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        if (user_cancel_button) {
            user_cancel_button.addEventListener('click', function(e) {
                e.preventDefault();
                
                //clear form
                const all_inputs = user_form.querySelectorAll('input:not([type="hidden"]), select');
                all_inputs.forEach(input => input.value = '');
                
                //clearing user id
                if (user_id) user_id.value = ""; 
                
                //removes error messages
                const errors = user_form.querySelectorAll('.errors');
                errors.forEach(err => err.remove());
                
                //hide previous password field
                if (old_password_row) {
                    old_password_row.style.display = 'none';
                }

                if (user_form_title) user_form_title.innerText = "Add New User";
                if (user_save_button) user_save_button.innerText = "Save";
            });
        }
    }
});
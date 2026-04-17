//show/hide add form
document.addEventListener('DOMContentLoaded', function() {
    
    const add_button = document.querySelector("#add_button");
    const cancel_task_button = document.querySelector("#cancel_task_button");
    const tasks_form_container = document.querySelector("#tasks_form_container");
    const tasks_form = document.querySelector("#tasks_form"); 

    add_button.addEventListener("click", (e) => {
        tasks_form_container.classList.toggle("show-form");
    });


    cancel_task_button.addEventListener("click", (e) => {
        e.preventDefault();
        tasks_form.reset(); 

        tasks_form_container.classList.remove("show-form");
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('experience_table');
    if (!table) return;

    table.addEventListener('click', function(e) {
        // Find if a button was clicked
        const btn = e.target.closest('.inline-btn');
        if (!btn) return;

        // Find the specific row that the button belongs to
        const row = btn.closest('.interactive-row');

        // --- EDIT BUTTON CLICKED ---
        if (btn.classList.contains('edit-btn')) {
            // Hide normal text, show inputs
            row.querySelectorAll('.view-mode').forEach(el => el.style.display = 'none');
            row.querySelectorAll('.edit-mode').forEach(el => {
                el.style.display = el.classList.contains('input-group') ? 'flex' : 'block';
            });
            // Swap buttons
            row.querySelector('.view-actions').style.display = 'none';
            row.querySelector('.edit-actions').style.display = 'flex';
        }

        // --- CANCEL EDIT BUTTON CLICKED ---
        else if (btn.classList.contains('cancel-edit-btn')) {
            // Hide inputs, show normal text
            row.querySelectorAll('.edit-mode').forEach(el => el.style.display = 'none');
            row.querySelectorAll('.view-mode').forEach(el => el.style.display = 'block');
            // Swap buttons back
            row.querySelector('.edit-actions').style.display = 'none';
            row.querySelector('.view-actions').style.display = 'flex';
        }

        // --- DELETE BUTTON CLICKED ---
        else if (btn.classList.contains('delete-btn')) {
            // Swap to Yes/No buttons
            row.querySelector('.view-actions').style.display = 'none';
            row.querySelector('.delete-actions').style.display = 'flex';
            row.style.backgroundColor = '#fff5f5'; // Subtle red tint
        }

        // --- CANCEL DELETE (NO) CLICKED ---
        else if (btn.classList.contains('cancel-delete-btn')) {
            // Swap back to normal actions
            row.querySelector('.delete-actions').style.display = 'none';
            row.querySelector('.view-actions').style.display = 'flex';
            row.style.backgroundColor = ''; // Remove red tint
        }

        // --- CONFIRM SAVE / CONFIRM DELETE ---
        else if (btn.classList.contains('save-btn')) {
            alert('This is where you trigger the AJAX call to Django to save the edits!');
            // After successful save, you would update the view-mode text and switch back to view mode.
        }
        else if (btn.classList.contains('confirm-delete-btn')) {
            alert('This is where you trigger the AJAX call to Django to delete the item!');
            // After successful delete, you would remove the row: row.remove();
        }
    });
});
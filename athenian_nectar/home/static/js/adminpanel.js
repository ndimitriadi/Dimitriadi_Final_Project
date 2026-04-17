


document.addEventListener('DOMContentLoaded', function() {
    
    const add_button = document.querySelector("#add_button");
    const cancel_task_button = document.querySelector("#cancel_task_button");
    const tasks_form_container = document.querySelector("#tasks_form_container");
    const tasks_form = document.querySelector("#tasks_form"); 

    add_button.addEventListener("click", (e) => {
        tasks_form_container.classList.toggle("show-form");
    });


    cancel_task_button.addEventListener("click", (e) => {
        tasks_form.reset(); 
        tasks_form_container.classList.remove("show-form");
    });
});
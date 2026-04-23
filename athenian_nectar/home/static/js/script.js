//-------------- HIGHLIGHT ACTIVE LINK --------------------------------------
function highlight_active_link(){
    const current_window_location = window.location.href; 
    const all_nav_links = document.querySelectorAll('.nav-links a, .mobile-dropdown a');
    
    all_nav_links.forEach(link => {
        if (link.href === current_window_location) {
            link.classList.add('active'); 
        }
    });
}

//----------------------- HAMBURGER MENU -----------------------------------
function hamburger_menu(){
    const hamburger_button = document.querySelector('.hamburger-button');
    const mobile_dropdown = document.querySelector('.mobile-dropdown');

    hamburger_button.addEventListener('click', () => {
        mobile_dropdown.classList.toggle('active');
        hamburger_button.classList.toggle('open');
        
        //animation
        const spans = hamburger_button.querySelectorAll('span');
        if (hamburger_button.classList.contains('open')) {
            spans[0].style.transform = "rotate(45deg) translate(5px, 5px)";
            spans[1].style.opacity = "0";
            spans[2].style.transform = "rotate(-45deg) translate(4px, -4px)";
        } else {
            spans[0].style.transform = "none";
            spans[1].style.opacity = "1";
            spans[2].style.transform = "none";
        }
        })
}

/*--------------- BACK TO TOP BUTTON-----------------------------*/
document.addEventListener('DOMContentLoaded', () => {

    highlight_active_link();
    hamburger_menu();

    const back_to_top = document.querySelector('#back-to-top');
    if (back_to_top) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 800) {
                back_to_top.classList.add('show');
            } else {
                back_to_top.classList.remove('show');
            }
        });

        back_to_top.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: 'smooth'
            });
        });
    }
});
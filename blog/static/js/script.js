document.addEventListener('DOMContentLoaded', function() {
    const body = document.querySelector('body');
    const sidebar = document.querySelector('.sidebar');
    const sidebarLinks = document.querySelectorAll('.sidebar a');

    body.addEventListener('click', function(event) {
        if (!event.target.closest('.sidebar')) {
            sidebar.classList.remove('close');
        }
    });

    sidebarLinks.forEach(link => {
        link.addEventListener('mouseover', function() {
            if (sidebar.classList.contains('close')) {
                const title = this.getAttribute('data-temp-title');
                if (title) {
                    this.setAttribute('title', title);
                    this.removeAttribute('data-temp-title');
                }
            } else {
                const title = this.getAttribute('title');
                if (title) {
                    this.setAttribute('data-temp-title', title);
                    this.removeAttribute('title');
                }
            }
        });
    });

    const modeSwitch = document.querySelector('.toggle-switch');
    const modeText = document.querySelector('.mode-text');

    modeSwitch.addEventListener('click', () => {
        body.classList.toggle('dark');
        if (body.classList.contains('dark')) {
            modeText.innerText = 'Light mode';
        } else {
            modeText.innerText = 'Dark mode';
        }
    });

    const toggle = document.querySelector('.toggle');
    toggle.addEventListener('click', () => {
        sidebar.classList.toggle('close');
    });

    
});

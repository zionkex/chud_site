document.addEventListener('DOMContentLoaded', function () {
    const body = document.querySelector('body');
    const sidebar = document.querySelector('.sidebar');
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    const modeSwitch = document.querySelector('.toggle-switch');
    const modeText = document.querySelector('.mode-text');
    const toggle = document.querySelector('.toggle');

    // Function to save theme mode and sidebar state to localStorage
    const saveState = () => {
        localStorage.setItem('themeMode', body.classList.contains('dark') ? 'dark' : 'light');
        localStorage.setItem('sidebarState', sidebar.classList.contains('close') ? 'closed' : 'open');
    };

    // Function to load theme mode and sidebar state from localStorage
    const loadState = () => {
        const themeMode = localStorage.getItem('themeMode');
        const sidebarState = localStorage.getItem('sidebarState');

        if (themeMode === 'dark') {
            body.classList.add('dark');
            modeText.innerText = 'Light mode';
        }

        if (sidebarState === 'closed') {
            sidebar.classList.add('close');
        }
    };

    // Load initial state on page load
    loadState();

    // Event listener for body click to close sidebar
    body.addEventListener('click', function (event) {
        if (!event.target.closest('.sidebar')) {
            sidebar.classList.remove('close');
            saveState();
        }
    });

    // Event listener for sidebar link mouseover to handle titles
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

    // Event listener for mode switch click
    modeSwitch.addEventListener('click', () => {
        body.classList.toggle('dark');
        if (body.classList.contains('dark')) {
            modeText.innerText = 'Light mode';
        } else {
            modeText.innerText = 'Dark mode';
        }
        saveState();
    });

    // Event listener for toggle click to open/close sidebar
    toggle.addEventListener('click', () => {
        sidebar.classList.toggle('close');
        saveState();
    });
});

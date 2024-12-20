let darkmode = localStorage.getItem('darkmode');

// Get both desktop and mobile theme switches
const themeSwitchDesktop = document.getElementById('theme-switch');
const themeSwitchMobile = document.getElementById('theme-switch-mobile');

// Get both desktop and mobile theme icons
const themeIconDesktop = document.getElementById('theme-class-switch');
const themeIconMobile = document.getElementById('theme-class-switch-mobile');

// Enable dark mode
const enableDarkmode = () => {
    document.body.classList.add('darkmode');
    localStorage.setItem('darkmode', 'active');

    // Update icons for both desktop and mobile
    if (themeIconDesktop) {
        themeIconDesktop.classList.remove('fa-sun');
        themeIconDesktop.classList.add('fa-moon');
    }
    if (themeIconMobile) {
        themeIconMobile.classList.remove('fa-sun');
        themeIconMobile.classList.add('fa-moon');
    }
};

// Disable dark mode
const disableDarkmode = () => {
    document.body.classList.remove('darkmode');
    localStorage.setItem('darkmode', null);

    // Update icons for both desktop and mobile
    if (themeIconDesktop) {
        themeIconDesktop.classList.remove('fa-moon');
        themeIconDesktop.classList.add('fa-sun');
    }
    if (themeIconMobile) {
        themeIconMobile.classList.remove('fa-moon');
        themeIconMobile.classList.add('fa-sun');
    }
};

// Check localStorage for dark mode preference and apply it
if (darkmode === "active") {
    enableDarkmode();
}

// Add event listeners for both desktop and mobile switches
if (themeSwitchDesktop) {
    themeSwitchDesktop.addEventListener("click", () => {
        darkmode = localStorage.getItem('darkmode');
        if (darkmode !== "active") {
            enableDarkmode();
        } else {
            disableDarkmode();
        }
    });
}

if (themeSwitchMobile) {
    themeSwitchMobile.addEventListener("click", () => {
        darkmode = localStorage.getItem('darkmode');
        if (darkmode !== "active") {
            enableDarkmode();
        } else {
            disableDarkmode();
        }
    });
}

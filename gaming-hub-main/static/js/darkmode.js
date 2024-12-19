let darkmode = localStorage.getItem('darkmode')
const themeSwitch = document.getElementById('theme-switch')
const themeIcon = document.getElementById('theme-class-switch')

const enableDarkmode = () => {
  document.body.classList.add('darkmode')
  localStorage.setItem('darkmode', 'active')

  themeIcon.classList.remove('fa-sun');
  themeIcon.classList.add('fa-moon');
}

const disableDarkmode = () => {
    document.body.classList.remove('darkmode')
    localStorage.setItem('darkmode', null)

    themeIcon.classList.remove('fa-moon');
    themeIcon.classList.add('fa-sun');
}

if (darkmode === "active") {
    enableDarkmode()
}

themeSwitch.addEventListener("click", () => {
  darkmode = localStorage.getItem('darkmode')
  if (darkmode !== "active") {
    enableDarkmode()
  }
  else {
    disableDarkmode()
  }
})

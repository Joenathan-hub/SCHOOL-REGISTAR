const loginPage = document.getElementById("loginPage");
const dashboard = document.getElementById("dashboard");
const userRole = document.getElementById("userRole");

const navLinks = document.querySelectorAll(".nav-links li");
const pages = document.querySelectorAll(".page");

/* LOGIN */
function login() {
    const role = document.getElementById("role").value;
    loginPage.classList.add("hidden");
    dashboard.classList.remove("hidden");
    userRole.textContent = "Role: " + role.toUpperCase();
}

/* NAVIGATION */
navLinks.forEach(link => {
    link.addEventListener("click", () => {
        navLinks.forEach(l => l.classList.remove("active"));
        pages.forEach(p => p.classList.remove("active-page"));

        link.classList.add("active");
        document.getElementById(link.dataset.page).classList.add("active-page");
    });
});

/* THEME TOGGLE */
function toggleTheme() {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
}

/* Animazione per "scroll to section" del bottone btn primary dell'hero banner */
/* che scorrerà fino alla sezione successiva "introduction" */
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".btn-primary").addEventListener("click", function() {
        document.querySelector(".introduction").scrollIntoView({ behavior: "smooth" });
    });
});
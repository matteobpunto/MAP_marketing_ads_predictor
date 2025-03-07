/*SCRIPT PER ANIMAZIONI*/

/* Animazione di entrata fade in per testo sezione "introduction" */
document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Aggiunge la classe per far partire l'animazione
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Stoppa l'osservazione dopo la prima animazione
            }
        });
    }, { threshold: 0.5 }); // L'animazione parte quando il 50% del paragrafo è visibile

    // Osserviamo il paragrafo
    observer.observe(document.querySelector("#intro-map"));
});

/* Animazione di entrata fade in per testo sezione "marketing-section" */
document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Aggiunge la classe per far partire l'animazione
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Stoppa l'osservazione dopo la prima animazione
            }
        });
    }, { threshold: 0.5 }); // L'animazione parte quando il 50% del paragrafo è visibile

    // Osserviamo il paragrafo
    observer.observe(document.querySelector(".text-container"));
});

/* Animazione di entrata fade in per immagini "marketing-section" */
document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Aggiunge la classe per far partire l'animazione
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Stoppa l'osservazione dopo la prima animazione
            }
        });
    }, { threshold: 0.5 }); // L'animazione parte quando il 50% della sezione è visibile

    // Osserviamo la classe .marketing-options
    observer.observe(document.querySelector(".marketing-options"));
});

/* Animazione per "scroll to section" del bottone btn primary dell'hero banner */
/* che scorrerà fino alla sezione successiva "introduction" */
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".btn-primary").addEventListener("click", function() {
        document.querySelector(".introduction").scrollIntoView({ behavior: "smooth" });
    });
});















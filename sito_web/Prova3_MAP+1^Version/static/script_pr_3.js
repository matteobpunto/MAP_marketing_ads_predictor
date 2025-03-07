
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












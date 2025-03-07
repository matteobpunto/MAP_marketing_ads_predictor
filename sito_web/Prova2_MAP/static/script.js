
document.addEventListener("DOMContentLoaded", () => {
    const imageContainer = document.querySelector(".image-container");
    const lens = document.querySelector(".lens");
    const blurredImage = document.querySelector(".blurred-image");

    imageContainer.addEventListener("mousemove", (e) => {
        const rect = imageContainer.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        lens.style.left = ${x - 40}px;
        lens.style.top = ${y - 40}px;
        lens.style.display = "block";

        // Rimuove il blur solo attorno alla lente
        blurredImage.style.filter = blur(0px);
        blurredImage.style.clipPath = circle(40px at ${x}px ${y}px);
    });

    imageContainer.addEventListener("mouseleave", () => {
        lens.style.display = "none";
        blurredImage.style.clipPath = "none"; // Ripristina il blur totale
    });
});












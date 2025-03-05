
document.querySelector(".image-container").addEventListener("mousemove", (e) => {
    const { left, top } = e.target.getBoundingClientRect();
    e.target.style.setProperty("--x", `${e.clientX - left}px`);
    e.target.style.setProperty("--y", `${e.clientY - top}px`);
});

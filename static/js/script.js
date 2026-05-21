document.querySelectorAll(".card").forEach(card => {
    card.onmouseenter = () => card.style.transform = "scale(1.05)";
    card.onmouseleave = () => card.style.transform = "scale(1)";
});

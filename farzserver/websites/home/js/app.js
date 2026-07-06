console.log("FARZNET JS loaded successfully 🚀");

document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector("h1");
    if (title) {
        title.addEventListener("click", () => {
            title.style.color = "red";
            alert("FARZNET is running your JS!");
        });
    }
});
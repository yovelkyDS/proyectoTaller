
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const nombre = document.getElementById("username").value;
    if (nombre.trim() !== "") {
        document.getElementById("userDisplay").textContent = nombre;
        document.getElementById("loginScreen").classList.add("hidden");
        document.getElementById("chatScreen").classList.remove("hidden");
    }
});
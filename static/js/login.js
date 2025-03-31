document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Evita que la página se recargue
    const nombre = document.getElementById("username").value.trim(); // Captura el nombre

    if (nombre) {
        console.log("Nombre ingresado:", nombre); // Ver en la consola
        document.getElementById("userDisplay").textContent = nombre; // Mostrar en la interfaz
        document.getElementById("loginScreen").classList.add("hidden"); // Ocultar login
        document.getElementById("chatScreen").classList.remove("hidden"); // Mostrar chat
    }
});
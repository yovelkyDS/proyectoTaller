document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const chatInput = document.getElementById('chatInput');
    const chatBody = document.getElementById('chatBody');

    chatForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Evita la recarga de la página al enviar el formulario
        const message = chatInput.value.trim();
        if (message === '') return;

        // Limpiar el campo de entrada
        chatInput.value = '';

        // Mostrar mensaje del usuario en el chat
        const userMessage = document.createElement('div');
        userMessage.classList.add('chat-message', 'user');
        userMessage.innerHTML = `${message}`;
        chatBody.appendChild(userMessage);
        chatBody.scrollTop = chatBody.scrollHeight;

        // Spinner de carga
        const loadingMessage = document.createElement('div');
        loadingMessage.classList.add('chat-message', 'bot');
        loadingMessage.innerHTML = `<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span> ...`;
        chatBody.appendChild(loadingMessage);

        try {
            // Enviar mensaje al servidor
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            const data = await response.json();

            // Remueve el spinner antes de procesar la respuesta
            chatBody.removeChild(loadingMessage);

            if (data.error) {
                // Mostrar mensaje de error si existe el campo "error" en la respuesta
                const errorMessage = document.createElement('div');
                errorMessage.classList.add('d-flex', 'flex-column', 'align-items-start', 'error', 'text-danger');
                icon = `<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><path fill="currentColor" d="M11.001 10h2v5h-2zM11 16h2v2h-2z"/><path fill="currentColor" d="M13.768 4.2C13.42 3.545 12.742 3.138 12 3.138s-1.42.407-1.768 1.063L2.894 18.064a1.99 1.99 0 0 0 .054 1.968A1.98 1.98 0 0 0 4.661 21h14.678c.708 0 1.349-.362 1.714-.968a1.99 1.99 0 0 0 .054-1.968zM4.661 19L12 5.137L19.344 19z"/></svg>`
                errorMessage.innerHTML = `<p class='d-flex gap-2 align-items-center'>${icon}${data.error}</p>`;
                chatBody.appendChild(errorMessage);
            } else {
                // Mensaje del chatbot
                const botMessage = document.createElement('div');
                botMessage.classList.add('chat-message', 'bot');
            
                // SVG del chatbot
                const botIcon = `
                    <svg class="IconChat" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 48 48"><ellipse cx="24" cy="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" rx="9.636" ry="20.5"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="M28.818 15.655c9.805 5.66 15.597 13.986 12.936 18.595s-12.767 3.756-22.572-1.905S3.586 18.36 6.247 13.75c1.064-1.843 3.318-2.812 6.267-2.95c4.427-.208 10.42 1.457 16.304 4.855"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" d="M28.818 32.345c-9.805 5.661-19.91 6.514-22.571 1.905s3.13-12.934 12.935-18.595c5.662-3.27 11.424-4.935 15.795-4.871c3.198.046 5.652 1.018 6.777 2.966c2.66 4.609-3.13 12.934-12.936 18.595M20.43 21.251h7.14M19.314 24h9.372m-6.745 2.749h4.118"/></svg>`;

                // Mensaje del chatbot convertido a HTML con Markdown
                const botMessageText = document.createElement('div');
                botMessageText.classList.add('d-flex', 'flex-column', 'align-items-start');  // Añade clases según tu diseño
                botMessageText.innerHTML = '';  // Inserta el HTML generado con markdown

                // Inserta el SVG y el mensaje dentro del contenedor
                botMessage.innerHTML = botIcon;
                botMessage.appendChild(botMessageText);
                chatBody.appendChild(botMessage);

                // Función de efecto typing
                function textTypingHTML(htmlString, element, speed, callback) {
                    let currentIndex = 0;

                    function typingEffect() {
                        element.innerHTML = htmlString.slice(0, currentIndex + 1);
                        chatBody.scrollTop = chatBody.scrollHeight;

                        if (currentIndex < htmlString.length - 1) {
                            currentIndex++;
                            setTimeout(typingEffect, speed);
                        } else if (callback) {
                            callback();
                        }
                    }

                    typingEffect();
                }

                // Ejecuta el efecto typing en el mensaje del bot con el HTML formateado
                textTypingHTML(data.text, botMessageText, 10, () => {
                    if (data.graph) {
                        const imageElement = document.createElement('img');
                        imageElement.src = data.graph;
                        imageElement.alt = 'Gráfico generado';
                        imageElement.style.maxWidth = '90%';
                        imageElement.style.margin = '0 auto';
                        botMessageText.appendChild(imageElement);
                        chatBody.scrollTop = chatBody.scrollHeight;
                    }
                }); // Puedes ajustar la velocidad con el tercer parámetro

            }
            // Asegúrate de hacer scroll al final
            chatBody.scrollTop = chatBody.scrollHeight;

        } catch (error) {
            chatBody.removeChild(loadingMessage);
            const errorMessage = document.createElement('div');
            errorMessage.classList.add('chat-message', 'bot', 'text-danger');
            errorMessage.innerHTML = '<strong>Error:</strong> No se pudo conectar con el servidor. Inténtalo más tarde.';
            chatBody.appendChild(errorMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
            console.error("Error en el fetch:", error);
        }
    });
});
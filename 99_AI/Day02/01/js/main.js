document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatBox = document.getElementById('chat-box');

    if (chatForm) {
        chatForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = chatInput.value.trim();

            if (message) {
                appendMessage(message, 'user');
                chatInput.value = '';
                showLoadingIndicator();

                // Simulate API call
                setTimeout(() => {
                    removeLoadingIndicator();
                    // As per PRD, return a fixed response if no API key is present.
                    const botResponse = 'API Key가 없습니다.';
                    appendMessage(botResponse, 'bot');
                }, 1000);
            }
        });
    }

    function appendMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message', sender === 'user' ? 'user-message' : 'bot-message');
        messageElement.textContent = message;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
    }

    function showLoadingIndicator() {
        const loadingElement = document.createElement('div');
        loadingElement.classList.add('chat-message', 'bot-message', 'loading-indicator');
        loadingElement.innerHTML = '<span>.</span><span>.</span><span>.</span>';
        chatBox.appendChild(loadingElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function removeLoadingIndicator() {
        const loadingElement = chatBox.querySelector('.loading-indicator');
        if (loadingElement) {
            chatBox.removeChild(loadingElement);
        }
    }
});

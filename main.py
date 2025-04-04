#26032025 Yovelky Delgado // Andres Valerio
import os
from flask import Flask, request, jsonify, render_template
from historyFiles import chat, openConversation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chats():
    data = request.get_json()
    user_message = data.get('message', '')
    try:
        res = chat(user_message)
        return jsonify({'text': res})
    except Exception as e:
        print(f"Error interno: {e}")
        # Devuelve un mensaje de error
        return jsonify({'error': 'Ocurrió un error interno. Por favor, inténtalo más tarde.'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    historial = openConversation("yovelky")
    return jsonify(historial)

@app.route('/api/clear_history', methods=['DELETE'])
def clear_history():
    file_name = "yovelky_conversation.txt"
    if os.path.exists(file_name):
        open(file_name, "w").close()
    return jsonify({"message": "Historial eliminado"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5510, debug=True)
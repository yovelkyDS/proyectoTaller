#26032025 Yovelky Delgado // Andres Valerio
from flask import Flask, request, jsonify, render_template
import markdown
from historyFiles import chat 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def process_response(response):
    if '| --- |' in response:  # Detección simple de tablas
        response_html = markdown.markdown(response, extensions=['tables'])
    else:
        response_html = markdown.markdown(response)
    return response_html

@app.route('/chat', methods=['POST'])
def chats():
    data = request.get_json()
    user_message = data.get('message', '')
    try:
        res = chat(user_message)
        print(" - - - - -- - - - - - - - -- - - - -- - - -")
        print(res)
        res_text_html = process_response(res)  # Solo la parte de texto
        return jsonify({'text': res_text_html})
    except Exception as e:
        print(f"Error interno: {e}")
        # Devuelve un mensaje de error
        return jsonify({'error': 'Ocurrió un error interno. Por favor, inténtalo más tarde.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5510, debug=True)
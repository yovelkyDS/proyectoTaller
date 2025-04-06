#26032025 Yovelky Delgado // Andres Valerio
from API import chat_con_php 
import ast, os

def openConversation(name:str)->bool:
    nameF = f"{name}_conversation.txt"
    with open(nameF, "a+") as file:
        file.seek(0)
        content = file.readlines()
        if content:
            return (content)
        else:
            return ([])
        
def register(msg:str, name:str,) -> str:
        """Funcion que registra la conversacion del chatbot con el usuario
        Args:
            msg (str): mensaje del usuario

        Returns:
            str: respuesta dada por el chatbot
        """
        fileN = f"{name}_conversation.txt"
        with open(fileN, "a", encoding="utf-8") as f:
            f.write(f"{msg}\n")

def chat(message:str, nombre:str)-> str:
    """Trae la informacion que proporciona el usuario, registra y devuelve la respuesta del chatbot

    Args:
        message (str): mensaje del usuario

    Returns:
        str: respuesta del chatbot
    """
    answer = chat_con_php(message)
    conversacion = []
    conversacion.append(["Usuario:", message, "Chatbot", answer])
    register(conversacion, nombre)
    return answer

def lookForWord(wordKey:str, nombre:str)->list:
    """Busca en el historial de conversaciones de un usuario utilizando una palabra clave

    Args:
        wordKey (str): palabra a buscar
        nombre (str): archivo a buscar

    Returns:
        list: Lista de conversaciones en las que se encontraron resultados
    """
    archivo = f"{nombre}_conversation.txt"
    if not os.path.exists(archivo):
        print("El usuario no tiene conversaciones guardadas.")
        return

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        try:
            historial = ast.literal_eval(contenido)
        except Exception as e:
            print("Error al leer el archivo:", e)
            return

    palabra_clave = wordKey.lower()
    resultados = []

    for i, conversacion in enumerate(historial, 1):
        for j in range(1, len(conversacion), 2):  # recorremos solo los mensajes
            mensaje = conversacion[j].lower()
            if palabra_clave in mensaje:
                resultados.append((i, conversacion[j]))
                break  # solo una coincidencia por conversación
    return (resultados)

def abstractConversation(conversacion:list)->str:
    abstract = chat_con_php(f"Haz un resumen de maximo 50 palabras de la siguiente conversacion: {conversacion}")
    return abstract
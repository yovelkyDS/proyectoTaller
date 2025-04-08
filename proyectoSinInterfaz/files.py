#26032025 Yovelky Delgado // Andres Valerio
from API import chat_con_php 
import os, json


def openConversation(name:str)->list:
    nameF = f"{name.lower()}_conversation.txt"
    historial = []
    if os.path.exists(nameF):
        with open(nameF, "r", encoding="utf-8") as f:
            try:
                historial = json.load(f)
                return historial
            except Exception as e:
                print(f"Error al leer el archivo: {e}")
                return []
    return []

def register(msg:list, name:str,) -> str:
        """Funcion que registra la conversacion del chatbot con el usuario
        Args:
            msg (str): mensaje del usuario

        Returns:
            str: respuesta dada por el chatbot
        """
        fileN = f"{name}_conversation.txt"
        historial = openConversation(name)
        historial.append(msg)
        with open(fileN, "w", encoding="utf-8") as f:
            json.dump(historial, f)

def chat(message:str)-> str:
    """Trae la informacion que proporciona el usuario, registra y devuelve la respuesta del chatbot

    Args:
        message (str): mensaje del usuario

    Returns:
        str: respuesta del chatbot
    """
    answer = chat_con_php(message)
    conversacion = ["Usuario:", message, "Chatbot", answer]
    return answer, conversacion

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
        return []
        
    palabraClave = wordKey.lower()
    resultados = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            historial = json.load(f)
            for i, conversacion in enumerate(historial, 1):
                for mensaje in conversacion:
                    if isinstance(mensaje, str) and palabraClave in mensaje.lower():
                        resultados.append((i, conversacion))
                        break
    except Exception as e:
        print(f"Error leyendo conversación {i}: {e}")
    return (resultados)

def abstractConversation(conversacion:list)->str:
    abstract = chat_con_php(f"Haz un resumen de maximo 50 palabras de la siguiente conversacion: {conversacion}")
    return abstract

def contextConversation(c:list):
    answer = chat_con_php(f"Deseo continuar una conversacion basado en este contexto: {c}")
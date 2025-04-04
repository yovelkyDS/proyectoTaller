#26032025 Yovelky Delgado // Andres Valerio
from API import chat_con_php

def openConversation(nombre:str)->list:
    nameF = f"{nombre}_conversation.txt"
    with open(nameF, "a+") as file:
        file.seek(0)
        content = file.readlines()
        if content:
            return (content)
        else:
            return ([])

try: 
    def login():
        pass
    def register(msg:str, name:str,) -> str:
        """Funcion que registra la conversacion del chatbot con el usuario


        Args:
            msg (str): mensaje del usuario

        Returns:
            str: respuesta dada por el chatbot
        """
        #name = login()
        fileN = f"{name}_conversation.txt"
        with open(fileN, "a", encoding="utf-8") as f:
            f.write(f"{msg}\n")
except:
    print("Error!")

def chat(message:str)-> str:
    """Trae la informacion que proporciona el usuario, registra y devuelve la respuesta del chatbot

    Args:
        message (str): mensaje del usuario

    Returns:
        str: respuesta del chatbot
    """
    historial = openConversation("yovelky")
    answer = chat_con_php(message)
    conversacion = []
    conversacion.append(["Usuario:", message, "Chatbot", answer])
    register(conversacion, "yovelky")
    return answer
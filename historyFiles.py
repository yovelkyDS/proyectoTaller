#26032025 Yovelky Delgado // Andres Valerio
from API import chat_con_php

def openConversation(nombre:str)->list:
    nameF = f"{nombre}.txt"
    with open(nameF, "a+") as file:
        file.seek(0)
        content = file.read()
        if content:
            return content
        else:
            return "No hay conversacion previa"

try: 
    def login():
        pass
    def answers(msg:str) -> str:
        """Funcion que registra la conversacion del chatbot con el usuario


        Args:
            msg (str): mensaje del usuario

        Returns:
            str: respuesta dada por el chatbot
        """
        name = login()
        answer = chat_con_php(msg)
        fileN = f"{name}.txt"
        with open(fileN, "a") as f:
            f.write()

except:
    print("Error!")
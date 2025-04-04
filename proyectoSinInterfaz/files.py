from API import chat_con_php 
from cli import login

def openConversation()->bool:
    nameF = f"{login()}_conversation.txt"
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
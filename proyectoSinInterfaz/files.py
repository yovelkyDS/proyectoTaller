from API import chat_con_php 

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
import shutil
from files import openConversation, chat

def centerText(txt:str)->str:
    terminal = shutil.get_terminal_size()
    textoC = txt.center(terminal.columns)
    return textoC

def login()->str:
    print(centerText("ChatBot"))
    nombre = str(input("Digite su nombre de usuario: "))
    return nombre

def chatMsg(n:str):
    print(centerText("ChatBot"))
    question = str(input("¡Hola! En que puedo ayudarte?\nTu: "))
    answer = chat(question, n)
    print(f"Respuesta: {answer}")

if __name__ == "__main__":
    name = login()
    history = openConversation(name)
    while True:
        chatMsg(name)
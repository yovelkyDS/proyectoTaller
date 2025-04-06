import shutil
from files import openConversation, chat, lookForWord, abstractConversation

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
    if question != "Salir":
        answer = chat(question, n)
        print(f"Respuesta: {answer}")
    else:
        breakpoint

def buscarPalabra(n:str):
    palabraClave = str(input("Digite la palabra a buscar: "))
    results = lookForWord(palabraClave, n)
    if results:
        print(f"\nConversaciones que contienen la palabra '{palabraClave}':")
        for num, ejemplo in results:
            print(f" - Conversación {num}: ...{ejemplo[:50]}...")
        yesOrNo = input("\n¿Desea ver el resumen de alguna conversación?\n1. Sí\n2. No\n-> ").strip()
        if yesOrNo == "1":
            conversationNum = int(input("Digite el número de la conversación que quiere resumir\n-> ").strip())
            for num, ejm in results:
                if num == conversationNum:
                    resumen = abstractConversation(ejm)
                    break
            print(f"Resumen de la conversacion:\n{resumen}")
        else:
            breakpoint()
    else:
        print("No se encontraron coincidencias.")

def menu():
    name = login()
    history = openConversation(name)
    while True:
        print("Bienvenido al chatbot\nOpciones\n\n1.Nueva Conversacion")
        print("2.Ver historial de conversaciones\n3.Buscar por palabra")
        print("4.Salir")
        opcion = str(input("Seleccione una opcion:"))
        match opcion:
            case "1":
                while True:
                    chatMsg(name)
            case "2":
                pass
            case "3":
                while True:
                    buscarPalabra(name)
            case "4":
                pass
if __name__ == "__main__":
    menu()
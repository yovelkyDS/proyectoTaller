import shutil, textwrap
from files import openConversation, chat, lookForWord, abstractConversation, register
import sys

def centerText(txt:str)->str:
    terminal = shutil.get_terminal_size()
    textoC = txt.center(terminal.columns)
    return textoC

AZUL = '\033[94m'
RESET = '\033[0m'
def imprimirMensaje(msg: str, orientacion: str = 'derecha', porcentaje: int = 80) -> None:
    terminal_size = shutil.get_terminal_size()
    anchoLinea = int(terminal_size.columns * porcentaje / 100)

    # Envuelve el texto dentro del ancho de la burbuja
    texto_formateado = textwrap.fill(msg, width=anchoLinea)
    lineas = texto_formateado.split('\n')
    ancho_burbuja = max(len(linea) for linea in lineas)

    # Crear bordes
    borde_superior = '┌' + '─' * (ancho_burbuja + 2) + '┐'
    borde_inferior = '└' + '─' * (ancho_burbuja + 2) + '┘'

    if orientacion == 'derecha':
        justificar = str.rjust
        padding = 0
        color = AZUL  # azul para usuario
    else:
        justificar = str.ljust
        padding = terminal_size.columns - (ancho_burbuja + 4)
        color = ''  # sin color para chatbot
        

    # Imprimir burbuja
    print(' ' * padding + justificar(color + borde_superior + RESET, ancho_burbuja + 4))
    for linea in lineas:
        contenido = f"│ {linea.ljust(ancho_burbuja)} │"
        print(' ' * padding + justificar(color + contenido + RESET, ancho_burbuja + 4))
    print(' ' * padding + justificar(color + borde_inferior + RESET, ancho_burbuja + 4))

def login()->str:
    print(centerText("ChatBot"))
    nombre = input("Digite su nombre de usuario: ")
    return nombre

def chatMsg(n:str):
    conversation = []
    print(centerText("ChatBot"))
    imprimirMensaje("¡Hola! En que puedo ayudarte?", 'izquierda')
    while True:
        question = str(input(f"{n}: "))
        if question.lower() == "salir":
            register(conversation, n)
            print ("Saliendo del chatbot...")
            return ("salir")
        answer, update = chat(question)
        conversation.extend(update)
        sys.stdout.write('\033[F\033[K')
        sys.stdout.flush()
        imprimirMensaje(question, 'derecha')
        imprimirMensaje(answer, 'izquierda')  

def buscarPalabra(n:str):
    palabraClave = str(input("Digite la palabra a buscar: "))
    results = lookForWord(palabraClave, n)
    print(results)
    if results:
        print(f"\nConversaciones que contienen la palabra '{palabraClave}':")
        for num, ejemplo in results:
            print(f" - Conversación {num}: ...{ejemplo[:50]}...")
        yesOrNo = input("\n¿Desea ver el resumen de alguna conversación?\n1. Sí\n2. No\n-> ").strip()
        if yesOrNo == "1":
            conversationNum = int(input("Digite el número de la conversación que quiere resumir\n-> ").strip())
            resumen = None
            for num, ejm in results:
                if num == conversationNum:
                    resumen = abstractConversation(ejm)
                    break
            if resumen:
                print(f"Resumen de la conversacion:\n{resumen}")
            else:
                print("No se encontró una conversación con ese número.")
        else:
            return("salir")
    else:
        print("No se encontraron coincidencias.")

def resumirConversacion(num:int, historial:list):
    cont = 1
    for e in historial:
        if cont == num:
            abstract = abstractConversation(e)
            imprimirMensaje(abstract, 'derecha', 90)
            break
        else:
            cont += 1

def cargarHistorial(h:list):
    h.reverse()
    conta=1
    for c in h:
        resumen = abstractConversation(c)
        print(f"{conta}. {resumen[:50]}...")
        conta+=1
    print("Digite:\n1.Si desea ver el resumen de alguna conversacion\n2.Si desea continuar con alguna conversacion\n3.Si desea regresar al menu principal")
    option = input("- ")
    match option:
        case "1":
            numC = int(input("Digite el numero de la conversacion que desea ver: "))
            resumirConversacion(numC, h)
        case "2":
            pass
        case "3":
            pass

def menu():
    name = login()
    history = openConversation(name)
    print(history)
    while True:
        print("Bienvenido al chatbot\nOpciones\n\n1.Nueva Conversacion")
        print("2.Ver historial de conversaciones\n3.Buscar por palabra")
        print("4.Salir")
        opcion = str(input("Seleccione una opcion:"))
        match opcion:
            case "1":
                while True:
                    s = chatMsg(name)
                    if s == "salir":
                        break
            case "2":
                cargarHistorial(history)
            case "3":
                while True:
                    s = buscarPalabra(name)
                    if s == "salir":
                        break
            case "4":
                print("¡Gracias por usar nuestro programa!")
                exit()

if __name__ == "__main__":
    menu()
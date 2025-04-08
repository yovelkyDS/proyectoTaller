import shutil, textwrap
from files import openConversation, chat, lookForWord, abstractConversation, register, contextConversation
import sys, os
import colores as c

def centerText(txt:str)->str:
    """Funcion para mejorar la estetica del programa 

    Args:
        txt (str): texto a colocar

    Returns:
        str: devuelve el texto orientado en el centro de la terminal
    """
    terminal = shutil.get_terminal_size()
    textoC = txt.center(terminal.columns)
    return textoC

def imprimirMensaje(msg: str, orientacion: str = 'derecha', porcentaje: int = 80) -> None:
    """funcion para darle formato a los emnsajes entre el usuario y el chatbot

    Args:
        msg (str): mensaje del chatbot o del usuario
        orientacion (str, optional): se orienta segun de quien sea el mensaje. Defaults to 'derecha'.
        porcentaje (int, optional): porcentaje de la pantalla en el cual se mostrara el mensaje. Defaults to 80.
    """
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
        color = c.AZUL  # azul para usuario
    else:
        justificar = str.ljust
        padding = terminal_size.columns - (ancho_burbuja + 4)
        color = ''  # sin color para chatbot
        

    # Imprimir burbuja
    print(' ' * padding + justificar(color + borde_superior + c.RESET, ancho_burbuja + 4))
    for linea in lineas:
        contenido = f"│ {linea.ljust(ancho_burbuja)} │"
        print(' ' * padding + justificar(color + contenido + c.RESET, ancho_burbuja + 4))
    print(' ' * padding + justificar(color + borde_inferior + c.RESET, ancho_burbuja + 4))

def login()->str:
    """mensaje para que el usuario ingrese su nombre

    Returns:
        str: dato ingresado por el usuario
    """
    print(centerText("ChatBot"))
    nombre = input("Escriba su nombre, incluyendo la primer letra de su apellido: ")
    return nombre

def chatMsg(n:str, conversation: list = [])-> None:
    """permite al usuario establecer una conversacion con el chatbot 

    Args:
        n (str): nombre para buscar el archivo en el cual se guardara la conversacion

    Returns:
        _type_: no posee un retorno 
    """
    print(centerText("ChatBot"))
    imprimirMensaje("¡Hola! En que puedo ayudarte?", 'izquierda')
    while True:
        question = str(input(f"{n}: "))
        if question.lower() == "salir":
            register(conversation, n)
            print ("\nRegresando al menu...")
            return ("salir")
        answer, update = chat(question)
        conversation.extend(update)
        sys.stdout.write('\033[F\033[K')
        sys.stdout.flush()
        imprimirMensaje(question, 'derecha')
        imprimirMensaje(answer, 'izquierda')  

def buscarPalabra(n:str)-> None:
    """permite buscar mediante una palabra en la lista de conversaciones guardadas en el archivo 

    Args:
        n (str): nombre del usuario propietario del archivo 
    """
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

def resumirConversacion(num:int, historial:list)-> None:
    """Genera un resumen de una conversacion especifica que el usuario desee 

    Args:
        num (int): numero de conversacion que se desea resumir 
        historial (list): historial de conversaciones entre el chatbot y el usuario
    """
    cont = 1
    for e in historial:
        if cont == num:
            abstract = abstractConversation(e)
            imprimirMensaje(abstract, 'derecha', 90)
            break
        else:
            cont += 1

def continuarConversacion(nume:int, h:list, n:str)-> None:
    """permite al usuario continuar con una conversacion guardada 

    Args:
        nume (int): numero de conversacion
        h (list): historial de la conversacion 
        n (str): nombre del usuario 
    """
    cont = 1
    for e in h:
        if cont == nume:
            contextConversation(e)
            chatMsg(n, e)
            break
        cont += 1

def cargarHistorial(h:list, nombre:str)-> None:
    """Muestra el historial guardado de conversaciones entre el usuario y el chatbot, y permite al usuario continuar con una conversacion o ver el resumen de la misma 

    Args:
        h (list): historial de conversaciones guardadas
        nombre (str): nombre del usuario
    """
    h.reverse()
    conta=1
    for c in h:
        resumen = abstractConversation(c)
        print(f"{conta}. {resumen[:50]}...")
        conta+=1
    print("\n\nDigite:\n1.Si desea ver el resumen de alguna conversacion\n2.Si desea continuar con alguna conversacion\n3.Si desea regresar al menu principal")
    option = input("- ")
    match option:
        case "1":
            numC = int(input("Digite el numero de la conversacion que desea ver: "))
            resumirConversacion(numC, h)
        case "2":
            numC = int(input("Digite el numero de la conversacion con la que desea continuar: "))
            continuarConversacion(numC, h, nombre)
        case "3":
            return("salir")

def menu():
    """menu principal del sistema, le muestra al usuario las principales funciones que posee el sistema y le permite ingresar a los submenus de las mismas o bien,
    salir del sistema 
    """
    name = login()
    history = openConversation(name)
    while True:
        print(centerText(f"{c.AZUL}Bienvenido al chatbot\n{c.RESET}"))
        print(f"{c.AZUL}\nOpciones\n{c.RESET}")
        print("1.Nueva Conversacion\n2.Ver historial de conversaciones\n3.Buscar por palabra")
        print("4.Salir")
        opcion = str(input("Seleccione una opcion:"))
        match opcion:
            case "1":
                while True:
                    s = chatMsg(name)
                    if s == "salir":
                        break
            case "2":
                while True:
                    history = openConversation(name)
                    s = cargarHistorial(history, name)
                    if s == "salir":
                        break
            case "3":
                while True:
                    s = buscarPalabra(name)
                    if s == "salir":
                        break
            case "4":
                print("\n¡Gracias por usar nuestro programa!")
                exit()

if __name__ == "__main__":
    menu()
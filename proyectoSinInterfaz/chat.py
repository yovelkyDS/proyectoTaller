import time
import shutil
import colores as c


def imprimirMensaje(msg: str, rol: str = 'bot' or 'usuario' or 'sistema', orientación: str = 'derecha', porcentaje: int = 80) -> None:
    lineas = []
    terminal_size = shutil.get_terminal_size()
    anchoLinea = int(terminal_size.columns * porcentaje / 100)

    # Determinar alineación y estilo por rol
    if rol.lower() == 'usuario':
        orientación = 'derecha'
        color = c.CIAN
        nombre = f"Usuario:{nombre} "
    elif rol.lower() == 'sistema':
        orientación = 'centro'
        color = c.AZUL
        nombre = "Sistema:"
    else:
        orientación = 'izquierda'
        color = c.AMARILLO
        nombre = "Bot:"

    # Mostrar quién habla
    if orientación == 'centro':
        print(color + nombre.center(terminal_size.columns) + c.RESET)
    elif orientación == 'derecha':
        print(color + nombre.rjust(terminal_size.columns) + c.RESET)
    else:
        print(color + nombre.ljust(terminal_size.columns) + c.RESET)

    # Dividir mensaje por palabras
    palabras = msg.split()
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual + ' ' + palabra) <= anchoLinea:
            linea_actual += (' ' if linea_actual else '') + palabra
        else:
            if orientación == 'derecha':
                lineas.append(linea_actual.rjust(terminal_size.columns))
            elif orientación == 'centro':
                lineas.append(linea_actual.center(terminal_size.columns))
            else:
                lineas.append(linea_actual.ljust(terminal_size.columns))
            linea_actual = palabra

    # Última línea
    if linea_actual:
        if orientación == 'derecha':
            lineas.append(linea_actual.rjust(terminal_size.columns))
        elif orientación == 'centro':
            lineas.append(linea_actual.center(terminal_size.columns))
        else:
            lineas.append(linea_actual.ljust(terminal_size.columns))

    # Imprimir líneas con color
    for linea in lineas:        
        print(color + linea + c.RESET)
        
mensaje="En la era digital, el conocimiento está al alcance de un clic. La educación, el trabajo y el entretenimiento han cambiado radicalmente gracias a la tecnología. Internet permite la conexión instantánea entre personas de distintas partes del mundo, rompiendo barreras geográficas y culturales. La inteligencia artificial y la automatización están revolucionando industrias, aumentando la eficiencia y optimizando recursos. La clave es adaptarse y aprovechar estas herramientas para el crecimiento personal y profesional."
print(c.CIAN)
imprimirMensaje(porcentaje=60, orientación='izquierda',msg=mensaje)
print(c.AMARILLO)
imprimirMensaje(porcentaje=80, orientación='derecha',msg=mensaje)
print(c.RESET)


print("Ejemplo de alineamiento de texto... espero 10 segundos", )
time.sleep(10)

def centarTexto(s:str)->str:
    terminal_size = shutil.get_terminal_size()
    return s.center(terminal_size.columns)


def validarUsuario(usuario:str,clave:str,lista_usuarios:list)->bool:
    for e in lista_usuarios:
        if e[0]==usuario and e[1]==clave:
            return(True)
    return(False)
 
def menu():
    print(c.CLEAR) #Limpia la terminal
    titulo=centarTexto("Mi asistente virtual")
    print(f"{c.MAGENTA}{titulo}{c.RESET}")
    print (f"\t{c.FONDO_AZUL}1){c.RESET} Ingresar con tu cuenta de usuario")
    print (f"\t{c.FONDO_AZUL}2){c.RESET} Salir del sistema\n")
    respuesta=input ("Digite la opción de su preferencia: ")

    if respuesta=="1":
        usuario=input ("Digite el nombre de usuario: ")
        clave=input ("Digite la clave: ")
        if validarUsuario(usuario,clave,usuarios):
            pass
        else:
            print(c.CLEAR)
            print (f"{c.FONDO_ROJO}{centarTexto("")}{c.RESET}")
            print (f"{c.FONDO_ROJO}{centarTexto("Usuario incorrecto")}{c.RESET}")
            print (f"{c.FONDO_ROJO}{centarTexto("")}{c.RESET}")
            time.sleep(3)

    elif respuesta=="2":
        print(c.CLEAR)
        print (f"{c.FONDO_AZUL}{centarTexto("")}{c.RESET}")
        print (f"{c.FONDO_AZUL}{centarTexto("Muchas gracias por utilizar nuestro sistema")}{c.RESET}")
        print (f"{c.FONDO_AZUL}{centarTexto("")}{c.RESET}")
        time.sleep(3)
        return False
    else:
        print(c.CLEAR)
        print (f"{c.FONDO_ROJO}{centarTexto("")}{c.RESET}")
        print (f"{c.FONDO_ROJO}{centarTexto("Opción incorrecta")}{c.RESET}")
        print (f"{c.FONDO_ROJO}{centarTexto("")}{c.RESET}")
        time.sleep(3)

while True:
    if not menu():
        break


while True:
    terminal_size = shutil.get_terminal_size()
    print('\033c',f"La \033[31mterminal\033[30m tiene {terminal_size.lines} líneas y {terminal_size.columns} columnas.")
    time.sleep(1)


def centarTexto(s:str)->str:
    terminal_size = shutil.get_terminal_size()
    return s.center(terminal_size.columns)


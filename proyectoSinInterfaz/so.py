import time

#reloj del sistema
print (time.ctime())
time.sleep(1)


#manejo del teclado y mouse
import pyautogui

pyautogui.press('enter')
pyautogui.typewrite('Hola mundo!\n')

# Mueve el mouse a la posición (x=100, y=100) en la pantalla
pyautogui.moveTo(100, 100)

# Hace clic en el botón izquierdo del mouse
pyautogui.click()

#pyautogui.click(x=100, y=100, clicks=2)

#archivos

with open("mi_archivo.txt", "w") as f:
    f.write("Hola mundo")

#Procesos
import subprocess

# Ejecuta el comando "clear" en sistemas Unix/Linux para limpiar la pantalla de la consola
subprocess.call("clear", shell=True)

import os

print("La identificación de proceso de este script es:", os.getpid())


import psutil

# Obtener una lista de todos los procesos en ejecución
lista_de_procesos = psutil.process_iter()

# Imprimir la identificación de proceso de cada proceso en la lista
for proceso in lista_de_procesos:
    print("ID del proceso:", proceso.pid, proceso.name())

# Buscar el proceso por su ID de proceso (PID)
pid_a_matar = 1234  # reemplaza con el PID del proceso que deseas matar
proceso_a_matar = None

for proceso in lista_de_procesos:
    if proceso.pid == pid_a_matar:
        proceso_a_matar = proceso
        break

# Matar el proceso si se encontró
if proceso_a_matar:
    proceso_a_matar.kill()
    print("El proceso con PID", pid_a_matar, "ha sido terminado.")
else:
    print("No se encontró ningún proceso con PID", pid_a_matar)


import pyudev

import pyudev

def listar_dispositivos_perifericos():
    context = pyudev.Context()
    dispositivos_perifericos = context.list_devices(subsystem='input')
    
    for dispositivo in dispositivos_perifericos:
        print("Dispositivo: ", dispositivo.device_node)

listar_dispositivos_perifericos()


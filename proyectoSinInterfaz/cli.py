import shutil
from files import openConversation, register

def login()->str:
    terminal = shutil.get_terminal_size()
    print("ChatBot".center(terminal.columns))
    nombre = str(input("Digite su nombre de usuario: "))
    return nombre

def chatMsg()->str:
    



if __name__ == "__main__":
    name = login()
    while True:
        pass
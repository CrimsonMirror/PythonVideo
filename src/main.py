import os 


def main():

    print("PythonVideo version 0.0.0-0ubuntu0.18.04.1 Copyright (c) 2019 CrimsonMirror")

    print(
        "1) Editar un Video\n"
        "2) Ayuda\n"
        "3) Salir\n"
    )
    option()


def help_():
    print("PythonVideo")


def option():
    
    opcion = 0
    try:
        opcion = int(input("Escoja una opción :"))
    except Exception as e:
        print("Error {}".format(e))
        print("Ingrese un valor valido!\n")
        option()
    if opcion not in [1,2,3]:
        print("Ingrese un valor valido!\n")
        option()
    option_edit_video() if opcion is 1 else help_() if opcion is 2 else print('Exit')



def option_edit_video():
    
    path = input("Escriba Direccion Path :")
    if os.path.exists(path):
        print('Nani')
    else:
        print('No nani')

    # print("Ingrese un path valido!\n") if os.path.exists(path) is True else print("Existe!")


main()
import os,re
from tool.color import colorCollection


class PythonVideo():

    def main(self):

        print("PythonVideo version 0.0.0-0ubuntu0.18.04.1 Copyright (c) 2019 CrimsonMirror")

        print(
            "1) Editar un Video\n"
            "2) Ayuda\n"
            "3) Salir\n"
        )
        self.option()


    def help_(self):
        print("PythonVideo")


    def option(self): 
        try:
            opcion = int(input("Escoja una opción :"))
            if opcion not in [1,2,3]:
                print("Ingrese un valor valido!\n")
                self.option()
            else:
                self.search_path() if opcion is 1 else self.help_() if opcion is 2 else print('Exit')
        except Exception as e:
            print("Error {}".format(e))
            print("Ingrese un valor valido!\n")
            return self.option()

    def search_path(self):
        x = 0

        video_list = {}

        regex = '.+.m4v|.+.mp4|.+.mkv'

        path = input("Escriba Direccion Path :")
        if os.path.exists(path):
            path_list = os.listdir(path)
            print("Lista de Archivos :")
            for i in path_list:
                x = x+1
                if re.match(regex,i) is not None:
                    video_list[x] = i
                    print(colorCollection.CYELLOW2+'{}) {}'.format(x,i))
                else:
                    print(colorCollection.END+'{}) {} Archivo No Compatible'.format(x,i))
            self.list_videos(video_list) if video_list != {} else print('No hay archivos para modificar')
            
        else:
            print('Ingrese un path valido!\n')
            self.search_path()

    def list_videos(self,*args):
        old_video_list = args[0]
        print(
            "\n"
            "Seleccione los videos que desea modificar\n"
            "Ejemplo : 2 4 5\n"
            "Si desea modificar todos los videos presione la tecla 'a'\n"
            )
        opcion = input('>> ')
        if opcion is 'a':
            print('Enviar todos los videos')
        else:
            try:
                lista = list(map(int,opcion.split()))
                print(lista)
            except Exception as e:
                print('Error {}'.format(e))
                self.list_videos(old_video_list)
        # newDict = { key:value for (key,value) in dictionary.items() if key in lista  }


videoPython = PythonVideo()

videoPython.main()
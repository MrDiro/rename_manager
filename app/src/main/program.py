import app.lib.tools as tools
import app.lib.screen as screen
from os import system
from cmd import Cmd
from app.lib.books import ArgumentError, ArgumentRangeError, PathError
from colorama import Fore, Style

class Program (Cmd):

    def do_EOF(self, arg):

        """Presiones CTRL + D para cerrar de forma segura el programa"""

        return True

    def do_save(self, arg:str):

        """Guarda los cambios echos"""

        tools.save(self.currentFiles, self.newNameFiles)
        self.newNameFiles.clear()

    def do_select(self, arg:str):

        """
        Comandos para aplicar cambios a la cadena de texto

        select [opcion] [complementos]

        Opcion:
        
        - all                       Todos los archivos o carpetas
        - one                       Un archivo o carpeta

        Complementos:

        - punctuations_off          Elimina los singnos de puntuacion
        - punctuations_spc          Renplaza los signos de puntuacion por espacios
        - lower                     convierte en minusculas
        - upper                     convierte en mayusculas
        - normalize_spc             eleminina los espacios de mas en la cadena
        - capitalize                convierte la primera letra en mayuscula
        - del_right [n]             elemina un numero de caracteres a la derecha
        - del_left [n]              elemina un numero de caracteres a la izquierda
        - rename [name]             renombra
        """

        try:

            self.newNameFiles = tools.select(arg, self.currentFiles)
            screen.select_show(**self.newNameFiles)
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_select(self, text:str, arg:str, begindx:int, endidx:int):

        return tools.get_complete_select(text)

    def do_here(self, arg:str):

        """Se mueve a la ruta actual de ejecucion del programa"""

        self.currentPath = tools.here()
        screen.show(self.currentPath, self.currentPath)

    def do_listing(self, arg:str):

        """
        Enlista los archivos del directorio actual

        - all         todos los archivos del directorio
        - d           solo las carpetas
        - f           solo los archivos
        """

        try:

            self.currentFiles = tools.listing(arg, self.currentPath)
            screen.listing_show(**self.currentFiles)

        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_listing(self, text:str, arg:str, begidx:int, endidx:int):

        return tools.get_complete_listing(text, self.currentPath)

    def do_show(self, arg:str):

        """
        Imprime una lista de directorio, actual o otra

        - show [foldername]         muestra los archivos y carpetas de la ruta definida
        - show                      muestra los archivos y carpetas de la ruta actual
        """

        try:

            self.newPath = tools.get_current_path(arg, self.currentPath)
            screen.show(self.currentPath, self.newPath)
        
        except PathError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_show(self, text:str, arg:str, begidx:int, endidx:int):

        return tools.get_complete_show(text, self.currentPath, self.newPath)

    def do_go(self, arg:str):

        """
        Cambia de directorio

        - go [foldername]           se mueve a la ruta definida
        """

        try:

            self.currentPath = tools.go(arg, self.currentPath)
            screen.show(self.currentPath, self.currentPath)
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

        except PathError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_go(self, text:str, arg:str, begidx:int, endidx:int):

        completation = tools.get_complete_go(text, self.currentPath)

        return completation

    def do_cls(self, arg:str):

        """Limpia la pantalla"""

        system("clear")
        print(screen.BANER)

    def do_back(self, arg:str):

        """
        Regresa al directorio anterior

        - back [n]          regresa atras segun el numero de carpeta definida
        """

        try:

            self.currentPath = tools.back(arg, self.currentPath)
            screen.show(self.currentPath, self.currentPath)
        
        except ArgumentRangeError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def do_quit(self, arg:str):

        """Termina con la ejecución del programa"""

        return True

    def __init__(self):

        super(Program, self).__init__()

        self.user = tools.USER
        self.currentPath = tools.HOME
        self.newPath = ""
        self.currentFiles = {}
        self.newNameFiles = {}
        self.prompt = tools.PROMPT

        screen.show(self.currentPath, self.currentPath)
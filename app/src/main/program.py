from cmd import Cmd
from app.lib.tools import get_initial_path, go, get_current_path, back, listing, here, select, save, USER, PROMPT
from app.lib.screen import baner, show, listing_show, select_show, clear
from app.lib.book_errors import ArgumentError, ArgumentRangeError
from colorama import Fore, Style

class Program (Cmd):

    def do_EOF(self, arg):

        """Presiones CTRL + D para cerrar de forma segura el programa"""

        return True

    def do_save(self, arg:str):

        """
        Guarda los cambios echos
        ==============================================================
        """

        save(self.currentFiles, self.newNameFiles)
        self.newNameFiles.clear()

    def do_select(self, arg:str):
        """
        Comandos para aplicar cambios a la cadena de texto
        ==============================================================

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

            self.newNameFiles = select(arg, self.currentFiles)
            select_show(**self.newNameFiles)
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_select(self, text:str, arg:str, begidx, endidx):

        pass

    def do_here(self, arg:str):

        """
        Se mueve a la ruta actual de ejecucion del programa
        ==============================================================
        """

        self.currentPath = here()
        show(self.currentPath, self.currentPath)

    def do_listing(self, arg:str):

        """
        Enlista los archivos del directorio actual
        ==============================================================

        - all         todos los archivos del directorio
        - d           solo las carpetas
        - f           solo los archivos
        """

        try:

            self.currentFiles = listing(arg, self.currentPath)
            listing_show(**self.currentFiles)

        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def complete_listing(self, text, arg, begidx, endidx):

        pass

    def do_show(self, arg:str):

        """
        Imprime una lista de directorio, actual o otra
        ==============================================================

        - show [foldername]         muestra los archivos y carpetas de la ruta definida
        - show                      muestra los archivos y carpetas de la ruta actual
        """

        try:

            self.newPath = get_current_path(arg, self.currentPath)
            show(self.currentPath, self.newPath)
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def do_go(self, arg:str):

        """
        Cambia de directorio
        ==============================================================
        - go [foldername]           se mueve a la ruta definida
        """

        try:

            self.currentPath = go(arg, self.currentPath)
            show(self.currentPath, self.currentPath)
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def do_cls(self, arg:str):

        """
        Limpia la pantalla
        ==============================================================
        """

        clear()

    def do_back(self, arg:str):

        """
        Regresa al directorio anterior
        ==============================================================
        - back [n]          regresa atras segun el numero de carpeta definida
        """

        try:

            self.currentPath = back(arg, self.currentPath)
            show(self.currentPath, self.currentPath)
        
        except ArgumentRangeError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")
        
        except ArgumentError as msg:

            print(f"{Fore.LIGHTRED_EX}[-] {msg}{Style.RESET_ALL}")

    def do_quit(self, arg:str):

        """
        Termina con la ejecución del programa
        ==============================================================
        """

        return True

    def __init__(self):

        super(Program, self).__init__()

        self.user = USER
        self.currentPath = get_initial_path(self.user)
        self.newPath = ""
        self.currentFiles = {}
        self.newNameFiles = {}
        self.prompt = PROMPT

        show(self.currentPath, self.currentPath)
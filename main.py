from app.src.program import Program
from os import system
from colorama import Fore, Style

def main():

    try:
        system("clear")
        app = Program()
        app.cmdloop()
    
    except KeyboardInterrupt:

        print(f"\n\n{Fore.LIGHTYELLOW_EX}[!] Programa finalizado por el usuario.{Style.RESET_ALL}")
    
    finally:

        print(f"\n{Fore.LIGHTGREEN_EX}[+] Gracias por usar nuestro servicio.{Style.RESET_ALL}")

if __name__ == "__main__":

    main()
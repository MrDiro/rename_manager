from app.src.main.program import Program
from app.lib.tools import cls
from colorama import Fore, Style

def main():

    try:
        cls()
        app = Program()
        app.cmdloop()
    
    except KeyboardInterrupt:

        print(f"\n{Fore.LIGHTYELLOW_EX}[!] Programa finalizado por el usuario.{Style.RESET_ALL}")
    
    finally:

        print(f"{Fore.LIGHTGREEN_EX}[+] Gracias por usar nuestro servicio.{Style.RESET_ALL}")

if __name__ == "__main__":

    main()
import os
from colorama import Fore, Style
from glob import glob

BANER = f"""{Fore.LIGHTCYAN_EX}------------------------------------------------------------
|                                                          |
|                     RENAME MANAGER                       |
|                                                          |
------------------------------------------------------------{Style.RESET_ALL}"""

def show(*args):

    os.system("clear")
    print(BANER)
    print("------------------------------------------------------------")
    print(f"Ubicación: {args[0]}")
    print("------------------------------------------------------------")

    for i in glob(f"{args[1]}/*"):

        if os.path.isdir(i):
            
            print(f"[{Fore.LIGHTRED_EX}d{Style.RESET_ALL}] {os.path.basename(i)}")

        else:

            print(f"[{Fore.LIGHTYELLOW_EX}f{Style.RESET_ALL}] {os.path.basename(i)}")

    print("------------------------------------------------------------")

def listing_show(**kwargs):

    os.system("clear")
    print(BANER)
    print("------------------------------------------------------------")
    print(f"Total: {len(kwargs)}")
    print("------------------------------------------------------------")

    for k, v in kwargs.items():

        print(f"[{k}] {os.path.basename(v)}")

    print("------------------------------------------------------------")

def select_show(**kwargs):

    os.system("clear")
    print(BANER)

    print("------------------------------------------------------------")
    print(f"Listo para guardar cambios: [{len(kwargs)}]")
    print("------------------------------------------------------------")

    for k, v in kwargs.items():

        print(f"{k} {os.path.basename(v)}")

    print("------------------------------------------------------------")
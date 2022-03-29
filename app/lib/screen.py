from colorama import Fore, Style
from glob import glob
from os.path import isdir, basename
from app.lib.tools import cls

baner = f"""{Fore.LIGHTCYAN_EX}------------------------------------------------------------
|                                                          |
|                     RENAME MANAGER                       |
|                                                          |
------------------------------------------------------------{Style.RESET_ALL}"""

def clear():

    cls()
    print(baner)

def show(*args):

    cls()
    print(baner)
    print("------------------------------------------------------------")
    print(f"Ubicación: {args[0]}")
    print("------------------------------------------------------------")

    for i in glob(f"{args[1]}/*"):

        if isdir(i):
            
            print(f"[{Fore.LIGHTRED_EX}d{Style.RESET_ALL}] {basename(i)}")

        else:

            print(f"[{Fore.LIGHTYELLOW_EX}f{Style.RESET_ALL}] {basename(i)}")

    print("------------------------------------------------------------")

def listing_show(**kwargs):

    cls()
    print(baner)
    print("------------------------------------------------------------")
    print(f"Total: {len(kwargs)}")
    print("------------------------------------------------------------")

    for k, v in kwargs.items():

        print(f"[{k}] {basename(v)}")

    print("------------------------------------------------------------")

def select_show(**kwargs):

    cls()
    print(baner)

    print("------------------------------------------------------------")
    print(f"Listo para guardar cambios: [{len(kwargs)}]")
    print("------------------------------------------------------------")

    for k, v in kwargs.items():

        print(f"{k} {basename(v)}")

    print("------------------------------------------------------------")
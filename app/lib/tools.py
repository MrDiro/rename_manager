import os
from app.lib.books import ArgumentError, ArgumentRangeError, PathError
from time import sleep
from colorama import Fore, Style
from re import sub
from glob import glob

SELECT_CMD = ("all", "one", "punctuations_off", "punctuations_spc", "lower", "upper", "normalize_spc", "capitalize", "del_right", "del_left", "rename")
LISTING_CMD = ("all", "f", "d")
USER = os.getenv("USER")
PROMPT = f"{Fore.CYAN}[{USER}]:>{Style.RESET_ALL} "
HOME = os.path.expanduser('~')

def get_complete_select(text) -> tuple:

    if not text:

        return SELECT_CMD

    else:

        return tuple(i for i in SELECT_CMD if i.startswith(text))

def get_complete_show(text, currentpath, newpath) -> tuple:

    items = tuple()

    if not newpath:

        items = tuple(os.path.split(i)[1] for i in glob(f"{currentpath}/*"))
    
    else:

        items = tuple(os.path.split(i)[1] for i in glob(f"{newpath}/*"))

    if not text:

        return items

    else:

        return tuple(i for i in items if i.startswith(text))

def get_complete_listing(text, currenpath) -> tuple:

    if not text:

        return LISTING_CMD

    else:

        return tuple(i for i in LISTING_CMD if i.startswith(text))

def get_complete_go(text, currentpath) -> tuple:

    items = tuple(os.path.split(i)[1] for i in glob(f"{currentpath}/*"))

    if not text:

        return items
    
    else:

        return tuple(i for i in items if i.startswith(text))

def splitpathfile(arg:str) -> tuple:

    return (f"{os.path.split(arg)[0]}/", os.path.splitext(os.path.split(arg)[1])[0], os.path.splitext(os.path.split(arg)[1])[1])

def slice_all(**kwargs) -> dict:

    return dict(map(lambda v : (v[0], splitpathfile(v[1])), kwargs.items()))

def slice_one(arg, **kwargs) -> tuple:

    return (arg[1], splitpathfile(kwargs[arg[1]]))

def select(*args) -> dict:

    cmd = args[0].split(" ")
    currentfiles = args[1].copy()

    if SELECT_CMD[0] in cmd:
        
        if SELECT_CMD[2] in cmd:

            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], sub(r"[^a-zA-Z0-9 áéíóú]", "", v[1][1]), v[1][2]))), slice_all(**currentfiles).items()))
        
        if SELECT_CMD[3] in cmd:

            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], sub(r"[^a-zA-Z0-9 áéíóú]", " ", v[1][1]), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[4]in cmd:
            
            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], str(v[1][1]).lower(), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[5] in cmd:

            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], str(v[1][1]).upper(), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[6] in cmd:

            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], str(sub(r" {2,}", " ", v[1][1])).strip(), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[7] in cmd:

            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], str(v[1][1]).capitalize(), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[8] in cmd:

            i = cmd[cmd.index(SELECT_CMD[8]) + 1]
            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], sub(r".{" + i + "}$", "", v[1][1]), v[1][2]))), slice_all(**currentfiles).items()))
        
        if SELECT_CMD[9] in cmd:

            i = cmd[cmd.index(SELECT_CMD[9]) + 1]
            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], sub(r"^.{" + i + "}", "", v[1][1]), v[1][2]))), slice_all(**currentfiles).items()))

        if SELECT_CMD[10] in cmd:

            nm = str("").join(cmd[cmd.index(SELECT_CMD[10]) + 1:])
            currentfiles = dict(map(lambda v : (v[0], str("").join((v[1][0], f"{nm} {int(v[0]):02}", v[1][2]))), slice_all(**currentfiles).items()))

    elif SELECT_CMD[1] in cmd:

        if SELECT_CMD[2] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], sub(r"[^a-zA-Z0-9 áéíóú]", "", v[1][1]), v[1][2]))}

        if SELECT_CMD[3] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], sub(r"[^a-zA-Z0-9 áéíóú]", " ", v[1][1]), v[1][2]))}

        if SELECT_CMD[4] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], str(v[1][1]).lower(), v[1][2]))}

        if SELECT_CMD[5] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], str(v[1][1]).upper(), v[1][2]))}

        if SELECT_CMD[6] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], str(v[1][1]).capitalize(), v[1][2]))}

        if SELECT_CMD[7] in cmd:

            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], str(sub(r"[ {2,}]", " ", v[1][1])).strip(), v[1][2]))}

        if SELECT_CMD[8] in cmd:

            i = cmd[cmd.index(SELECT_CMD[8]) + 1]
            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], sub(r".{" + i + "}$", "", v[1][1]), v[1][2]))}

        if SELECT_CMD[9] in cmd:

            i = cmd[cmd.index(SELECT_CMD[9]) + 1]
            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], sub(r"^.{" + i + "}", "", v[1][1]), v[1][2]))}

        if SELECT_CMD[10] in cmd:
            
            #corregir la entrada del nombre con espacios
            nm = str("").join(cmd[cmd.index(SELECT_CMD[10]) + 1:])
            v = slice_one(cmd, **currentfiles)
            currentfiles = {v[0]: str("").join((v[1][0], nm, v[1][2]))}
    else:

        raise ArgumentError("Argumento Invalido")
    
    return currentfiles

def save(*args):

    if len(args[1]) > 1:

        total = len(args[0])
        ca = '#'
        i = 1

        for k, v in args[0].items():

            os.rename(v, args[1][k])
            sleep(0.01)
            print(f"\rRenombrando: [{round(100 * (i / float(total)), 0)}%]{ca * i}", end='')
            i += 1
        
        print()

    else:

        k = tuple(args[1])[0]
        newname = args[1][k]
        oldname = args[0][k]
        
        os.rename(oldname, newname)

    print("------------------------------------------------------------")
    print("{Fore.LIGHTGREEN_EX}[+] Operación realizada exitosa mente!{Style.RESET_ALL}")

def here() -> str:

    path = os.getcwd()

    print(f"{Fore.LIGHTGREEN_EX}[+] {path}{Style.RESET_ALL}")

    return path

def back(*args) -> str:

    lp = args[1].split("/")
    newpath = ""

    if not args[0]:

        raise ArgumentError("Falta el argumento")
    
    elif not args[0].isnumeric():

        raise ArgumentError("Argumento invalido.")
    
    elif int(args[0]) > len(lp[2:]):

        raise ArgumentRangeError("Indice fuera del rango permitido.")
    
    del lp[len(lp) - int(args[0]):]

    newpath = str('/').join(lp)

    print(f"{Fore.LIGHTGREEN_EX}[+] {newpath}{Style.RESET_ALL}")

    return newpath

def get_current_path(*args) -> str:

    pat = ""

    if not args[0]:

        pat = args[1]

    else:

        pat = os.path.join(args[1], args[0])

    if not os.path.exists(pat):

        raise PathError("El directorio no existe")

    return pat

def go(*args) -> str:

    newpath = ""

    if not args[0]:

        raise ArgumentError("Argumento Invalido")
    
    if not os.path.exists(args[0]):

        raise PathError("El directorio no existe")
        
    newpath = os.path.join(args[1], args[0])

    print(f"{Fore.LIGHTGREEN_EX}[+] {newpath}{Style.RESET_ALL}")

    return newpath

def listing(*args) -> dict:

    olddom = glob(f"{args[1]}/*")
    newdom = {}

    if LISTING_CMD[0] in args:

        newdom = {str(k + 1): v for k, v in enumerate(olddom)}
    
    elif LISTING_CMD[1] in args:

        newdom = {str(k + 1): v for k, v in enumerate(olddom) if os.path.isfile(v)}

    elif LISTING_CMD[2] in args:

        newdom = {str(k + 1): v for k, v in enumerate(olddom) if os.path.isdir(v)}
    
    else:

        raise ArgumentError("Argumento invalido")

    return newdom
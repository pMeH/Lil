import os
import time
from datetime import datetime

# Função começo
def comeco():
    print(""".            .              .      ,_
|    ,-. ,-. |-    . ,-.    |    . |_ ,-.
|    | | `-. |     | | |    |    | |  |-'
`--' `-' `-' `'    ' ' '    `--' ' |  `-'

Available Regions:

euw, na, eune, br, lan, las, oce, ru, tr, kr.

Type --h for help
""")

# Função help

def help():
    print("""
Welcome to Lost in life's help utility!

If this is your first time using Lost in life follow this steps:

    -p                  Player
    -r                  Region
    -b                  Birthdate

Optional:

    clear               Clear screen
    -P                  Proxy

e.g. -p Hide on bush -r kr -b 7/5/1996
""")

# Função som
def som():
    file = open("testfile.txt","w")
    file.write("")
    file.close()
    os.startfile("som.py")

# Função end
def end():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color C')
    print("""███▓███████▓▓╬╬╬╬╬╬╬╬╬╬╬╬▓███▓▓▓▓█▓╬╬╬▓█
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█""")
    time.sleep(0.1)
    os.system('color F')
    print("""████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█""")
    time.sleep(0.1)
    os.system('color C')
    print("""████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█""")
    time.sleep(0.1)
    os.system('color F')
    print("""████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█""")
    time.sleep(0.1)
    os.system('color C')
    print("""████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█""")
    time.sleep(0.1)
    os.system('color F')
    print("""█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██""")
    time.sleep(0.1)
    os.system('color C')
    print("""█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██""")
    time.sleep(0.1)
    os.system('color F')
    print("""████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██""")
    time.sleep(0.1)
    os.system('color C')
    print("""█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███""")
    time.sleep(0.1)
    os.system('color F')
    print("""███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████""")
    time.sleep(0.1)
    os.system('color C')
    print("""████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████""")
    time.sleep(0.1)
    os.system('color F')
    print("""██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████""")
    time.sleep(0.1)
    os.system('color C')
    print("""██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████""")
    time.sleep(0.1)

    os.system('color F')
    time.sleep(0.1)
    os.system('color C')
    time.sleep(0.1)
    os.system('color F')
    time.sleep(0.1)
    os.system('color C')
    time.sleep(0.1)
    os.system('color F')
    time.sleep(0.1)
    os.system('color C')
    time.sleep(0.1)
    os.system('color F')
    time.sleep(0.1)
    os.system('color C')
    time.sleep(0.1)
    os.system('color F')
    time.sleep(0.1)
    os.system('color C')
    time.sleep(0.1)
    os.system('color F')
    time.sleep(0.1)

    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color A')

    print("We are Anonymous.")
    time.sleep(2.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("We are Legion.")
    time.sleep(2.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("We do not forgive.")
    time.sleep(2.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("We do not forget.")
    time.sleep(2.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Expect us.")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

# Função: diferença entre datas com clear/color
def ddia(date1, date2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color A')
    return abs((d2 - d1).days)

# Função: separar dados do main
def descript(x):
    player = ""
    region = ""
    date = ""
    proxy = ""

    for h in range(len(x)):
        if x[h:h+2] == "-p":
            for i in range(len(x)):
                if x[h+3+i:h+4+i] == "-" or i == len(x) - 1:
                    n = h+2+i
                    break
            player += x[h+3:n]
        if x[h:h+2] == "-r":
            for i in range(len(x)):
                if x[h+3+i:h+4+i] == "-" or i == len(x) - 1:
                    n = h+2+i
                    break
            region += x[h+3:n]
        if x[h:h+2] == "-b":
            for i in range(len(x)):
                if x[h+3+i:h+4+i] == "-" or i == len(x) - 1:
                    n = h+2+i
                    break
            date += x[h+3:n]
        if x[h:h+2] == "-P":
            for i in range(len(x)):
                if x[h+3+i:h+4+i] == "-" or i == len(x) - 1:
                    n = h+2+i
                    break
            proxy += x[h+3:n]

    return player, region, date, proxy

# Version 2.2 date 12/05/2017 for windows

from funcoes import *
import requests
from bs4 import BeautifulSoup
import math
import os
import time

intro()

os.system('color F')

print(""".            .              .      ,_
|    ,-. ,-. |-    . ,-.    |    . |_ ,-.
|    | | `-. |     | | |    |    | |  |-'
`--' `-' `-' `'    ' ' '    `--' ' |  `-'

Available Regions:

euw, na, eune, br, lan, las, oce, ru, tr, kr.

Type --h for help
""")


try:
    while True:
        main = input(">>> ")
        if main in ("help", "h", "--h", "-h", "--help", "-help"):
            print("""
Welcome to Lost in life's help utility!

If this is your first time using Lost in life follow this steps:

    -p                  Player
    -r                  Region
    -b                  Birthdate

Optional:

    -P                  Proxy

e.g. -p Hide on bush -r kr -b 7/5/1996
""")
        elif main in ("-c", 'c', 'clear', '--c', '--clear', '-clear'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(""".            .              .      ,_
|    ,-. ,-. |-    . ,-.    |    . |_ ,-.
|    | | `-. |     | | |    |    | |  |-'
`--' `-' `-' `'    ' ' '    `--' ' |  `-'

Available Regions:

euw, na, eune, br, lan, las, oce, ru, tr, kr.

Type --h for help
""")
        else:
            player_com_espaço = descript(main)[0]
            player = ""
            proxy = descript(main)[3]
            for h in range(len(player_com_espaço)):
                if player_com_espaço[h] != " ":
                    player += player_com_espaço[h] # Agora o player está pronto.

            region = descript(main)[1]

            # Baixando site
            page = requests.get("http://www.loltimeplayed.com/timeplayed.php?region=%s&summoner=%s" % (region.lower(), player.lower()), proxies=proxy)
            # Criando a sopa
            soup = BeautifulSoup(page.content, 'html.parser')

            try:
                oito = soup.find(class_="totaltimeplayedtexttest")
                s = oito.find("b").get_text()
                data_2 = time.strftime('%d/%m/%Y')
                data_1 = descript(main)[2] # Agora data_1 está pronto.
                dias = ddia(data_2, data_1)
                anos = math.floor(dias/365)
                if region in ("euw", "na", "eune", "br", "lan", "las", "oce", "ru", "tr", "kr"):
                    break
            except:
                print("""Error""")
    if main not in ("help", "h", "--h", "-h", "-c", 'c', 'clear', '--c', '--clear', '-clear'):
        # Ajeitando a srt
        tempolol = 0
        for i in range(len(s)):
            try:
                tempolol = tempolol * 10 + int(s[i])
            except:
                if s[i] != "," and s[i] != ".":
                    break

        # Resultado
        calculos = (tempolol * 100)/(dias * 24)
        porcento = str("%.2f" % calculos) + str("%")

        # Antes do resultado, pegar os dados do player com uma adaptação do codigo de ISyther (https://github.com/ISyther/LoLSearch/blob/master/LolSearch.py)

        url = 'https://%s.op.gg/summoner/userName=%s' % (region, player)
        req=requests.get(url, proxies=proxy)

        try:
            elo=req.text
            elo=elo.split('<span class="tierRank">',maxsplit=1)
            del elo[0]
            elo="".join(elo)
            elo=elo.split(r'</span>',maxsplit=1)
            del elo[1]
            elo="".join(elo)
        except:
            elo = "There are no recorded results."

        #==============================#

        try:
            vitoria=req.text
            vitoria=vitoria.split(r'<div class="Text">')
            del vitoria[0]
            vitoria = "".join(vitoria)
            vitoria=vitoria.split(r'</div>',maxsplit=1)
            del vitoria[1]
            vitoria="".join(vitoria)
        except:
            vitoria = "There are no recorded results."

        #==============================#

        try:
            champ=req.text
            champ=champ.split(r'<div class="ChampionName" title="',maxsplit=1)
            del champ[0]
            champ = "".join(champ)
            champ=champ.split(r'">',maxsplit=1)
            del champ[1]
            champ="".join(champ)
        except:
            champ = 'There are no recorded results.'

        #==============================#
        try:
            amigo=req.text
            amigo=amigo.split(r'<a href="//br.op.gg/summoner/userName=',maxsplit=1)
            del amigo[0]
            amigo = "".join(amigo)

            amigo=amigo.split(r'" class="Link">',maxsplit=1)
            del amigo[0]
            amigo = "".join(amigo)

            amigo=amigo.split(r'</a>',maxsplit=1)
            del amigo[1]
            amigo="".join(amigo)
            amigo = (("""
    Recently Played With: %s
            """) % (amigo))
        except:
            amigo = ""

        print("""#====================================================#

    Nick: %s

    Ranked Solo: %s

    Win Ratio for last 20 games: %s

    Most Played Champion: %s

    Number of hours played: %d

    Age: %d

    You spent %s of your life playing lol..
    %s
#====================================================#
        """ % (player, elo, vitoria, champ, tempolol, anos, porcento, amigo))


        # Sair
        while exit not in ("r", 'R', ''):
            exit = input("Press enter to exit or type R to restart the program:")

            file = open("testfile.txt","w")
            file.write("ola")
            file.close()

            if exit == "r" or exit == "R":
                os.startfile("Lil.py")

except:
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('color C')
    print("Error inesperado.")
    time.sleep(5)

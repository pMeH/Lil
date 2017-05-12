import winsound
import os
os.system('mode con: cols=40 lines=8')

print("""
███╗   ███╗██╗   ██╗███████╗██╗ ██████╗
████╗ ████║██║   ██║██╔════╝██║██╔════╝
██╔████╔██║██║   ██║███████╗██║██║
██║╚██╔╝██║██║   ██║╚════██║██║██║
██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝""")
while True:
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    file = open("testfile.txt","r")
    a = str(file.read())
    file.close
    if a == """ola""":
        file2 = open("testfile.txt","w")
        file2.write("")
        file2.close()
        break


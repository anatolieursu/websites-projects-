#Script
from functions import ipTrack, phoneTrack

console = open("console", "a+")

console.seek(0)

# Reading the file
content = console.read()

print("\nComenzi disponibile : \n1. /ip-track\n2. /phoneNumber-track\n")
cmds = input("Introdu comanda: ")


if cmds == "/ip-track" or cmds == "1":
        ip = input("Introdu ip-ul: ")
        ipTrack.ip_track(ip)
elif cmds == "/phoneNumber-track" or cmds == "2":
        number = input("Introdu numarul de telefon: ")
        phoneTrack.phone_track(number)
else: print("Comanda nu a fost gasita")

console.close()



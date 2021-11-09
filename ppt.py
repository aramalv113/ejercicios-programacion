import os

os.system("cls")

j1 = ["piedra","papel","tijera"]
j2 = ["tijera","piedra","papel"]

jugada1 = "papel"
jugada2 = "piedra"

if j1.index(jugada1)==j2.index(jugada2):
    print("victoria")
else:
    print("derrota")


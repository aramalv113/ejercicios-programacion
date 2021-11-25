inicio = 1
fin = 50

print(inicio, ",", fin, end=", ")

while inicio!=((fin/2)):
    
    inicio += 2
    
    print(inicio, end=", ")
    print(fin-inicio+1, end=", ")
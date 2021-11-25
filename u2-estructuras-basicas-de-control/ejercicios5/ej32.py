decimal = int(input("Introduce el número decimal: "))
cociente = decimal
restos = ""

while cociente!=0:
    restos += str(cociente%2)

    cociente = cociente // 2

print(f" >> El número {decimal} en formato decimal se corresponde con el número {restos[::-1]} en formato binario.")

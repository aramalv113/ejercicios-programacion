import math

# la progresion es S = 1 + x^1 + x*2 + ··· + x^n
def calcula_progresion_geometrica(x:float=0.0,n:int=0) -> float:
    try:
        contador = 1
        progresion = 1.0

        while contador <= n:
            progresion += math.pow(x,contador)
            contador += 1

        return progresion
    
    except TypeError:
        return None

print(calcula_progresion_geometrica(2,0))

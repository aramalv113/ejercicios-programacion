a1=0
a2=1
an=0
n=3

print (f"{a1}, {a2}, ",end="")

while an<=1000:
    an = 3*a2 + 2*a1
    
    if an>1000:
        print(f"{an}\n\n",end="")
    else:
        print(f"{an}, ",end="")
    

    a1 = a2
    a2 = an
    n += 1

print(f" >> El primer término de la sucesión mayor a 1000 es el {n}.")

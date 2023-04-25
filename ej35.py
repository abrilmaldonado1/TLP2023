contador=0
superficie=0
submayor=[]
totalmayores=0
par=int (input ("ingrese la cantidad de pares que quiere registrar: "))
for contador in range (par):
    base=int (input("ingrese la base del triangulo: "))
    altura=int (input("ingrese la altura del triangulo: "))
    superficie= (base*altura)/2
    print ("la base del triangulo es: ",base, "la altura es: ",altura, "la superficie es: ",superficie)
    
    if superficie>12:
        submayor.append(superficie)
        contador=+1
totalmayores=len(submayor)
print ("la cantidad de triangulos con superficie mayor a 12 es de: ",totalmayores)

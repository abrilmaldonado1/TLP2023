notamayor=0
notamenor=0
for x in range (10):
    nota= int (input("ingrese un valor: "))

    if nota>=7:
        notamayor=notamayor+1
        
    else:
        notamenor=notamenor+1    
print ("las notas mayores o iguales a 7 son: ",notamayor)
print ("las notas menores a 7 son: ",notamenor)


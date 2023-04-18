x=1
notamayor=0
notamenor=0

while x<=10:
    nota=int (input ("ingrese nota: "))

    if nota>=7:
        notamayor=notamayor+1
        
    else:
        notamenor=notamenor+1
    x=x+1    
print ("las notas mayores o iguales a 7 son: ",notamayor)
print ("las notas menores a 7 son: ",notamenor)

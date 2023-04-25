num=0
contador=0
contador1=0
for x in range (10):
    num= int (input("ingrese un valor: "))
    if num%3==0:
        contador= contador+1
    if num%5==0:
        contador1= contador1+1
print("los valores multiplos de 3 son: ",contador)
print ("los valores multiplos de 5 son: ",contador1)

sueldo= int (input("ingrese su sueldo: "))
edad= int(input("ingrese su antiguedad: "))
if sueldo<500 and edad>10:
    aumento1=sueldo*100/20
    print ("se le otorga un 20% de aumento",aumento1)
   
if sueldo<500 and edad<10:
    aumento2=sueldo*100/5
    print ("se le otorga un 5% de aumento",aumento2)
    
if sueldo>500 and sueldo>=500:
    print ("no hay cambios")
    

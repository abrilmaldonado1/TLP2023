sueldos = []

for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(sueldo)

print("La lista de sueldos es:", sueldos)

promedio = sum(sueldos) / len(sueldos)
print("El promedio de los sueldos es:", promedio)

lista = []

while True:
    valor = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
    if valor == 0:
        break
    lista.append(valor)

tamaño = len(lista)
print("El tamaño de la lista es:", tamaño)

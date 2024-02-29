def contar_numeros_en_rango(numeros):
    contador = 0
    for numero in numeros:
        if 10<= numero <= 20:
            contador += 1
    return contador
cantidad_numeros = int(input("Ingrese la cantidad de numeros a capturar:"))
numeros = []
for i in range(cantidad_numeros):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
numeros_en_rango = contar_numeros_en_rango(numeros)

print("Numeros en rango",numeros_en_rango)

    
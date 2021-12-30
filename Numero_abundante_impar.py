n = 1

def obtener_divisores(num):

    divisores = []

    for d in range(1, num):

        if num%d == 0:

            divisores.append(d)
    
    return divisores

def sumar_elementos(lista):

    suma_total = 0

    for numero in lista:

        suma_total += numero
    
    return suma_total

while True:

    if n%2 != 0:

        if sumar_elementos(obtener_divisores(n)) > n:

            print(str(n) + " Es un número abundante impar")

            break
    
    n += 1
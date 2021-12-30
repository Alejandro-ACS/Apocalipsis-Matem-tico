def obtener_divisores(num):

    divisores = []

    for d in range(1, num):

        if num%d == 0:

            divisores.append(d)
    
    return divisores

def separar_numero(n):

    separado = []

    for d in str(n):

        separado.append(int(d))

    return separado

def sumar_elementos(lista):

    suma_total = 0

    for numero in lista:

        suma_total += numero
    
    return suma_total

def elevar_y_sumar(lista):

    resultado = 0

    for d in lista:

        resultado += d*d

    return resultado

def comprobar_ciclo(num):

    numeros = []

    numeros.append(num)

    TrueOrFalse = True

    while TrueOrFalse:

        num = elevar_y_sumar(separar_numero(num))

        numeros.append(num)

        if num == 1:

            return "feliz"
        
        else:

            numeros2 = numeros[:-1]

            for x in range(len(numeros2)):

                if num == numeros2[x]:

                    return "infeliz"

n = 1

while True:

    if sumar_elementos(obtener_divisores(n)) == n:

        if comprobar_ciclo(n) == "feliz":

            print(str(n) + " Es un número perfecto y feliz")

            break

    n += 1
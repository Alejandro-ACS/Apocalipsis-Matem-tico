def separar_numero(n):

    separado = []

    for d in str(n):

        separado.append(int(d))

    return separado

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

def comprobar_todos_ciclos(num):

    orden = [num]

    for x in range(len(str(num))-1):

        separado = separar_numero(orden[-1])

        primer_d = separado[0]

        del separado[0]

        separado.append(primer_d)

        nuevo_n = ""
        
        for y in range(len(separado)):

            nuevo_n += str(separado[y])

        orden.append(int(nuevo_n))
    
    return orden

m = int(input("¿Hasta que número quieres comprobar? >> "))

n = 1

while True:

    numeros_a_probar = comprobar_todos_ciclos(n)

    resultados = []

    for numero in numeros_a_probar:

        resultados.append(comprobar_ciclo(numero))

    for resultado in resultados:

        if comprobar_ciclo(n) != resultado:

            print("Esto es absurdo")

            break

    n += 1

    if n == m:

        print("Todos los números del 1 al " + str(n) + " cumplen esa propiedad")

        break
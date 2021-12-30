def factorial(n):

    if n == 1:

        return 1
    
    else:

        return n*factorial(n-1)

def separar_numero(n):

    separado = []

    for d in str(n):

        separado.append(int(d))

    return separado

def sumar(lista):

    resultado = 0

    for d in lista:

        resultado += d

    return resultado

n = 1

while True:

    resto = factorial(n)%sumar(separar_numero(factorial(n)))

    if resto != 0:

        print(str(n) + " No es harshad")
        
        print("El resto es: " + str(resto))

        break

    n += 1
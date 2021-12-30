from math import log

def convertir_base(num, base):

    numero = {i: "0123456789ABCDEF"[i] for i in range(16)}

    l_num = int(log(num, base))

    convertido = ""

    for x in range(l_num, -1, -1):

        convertido += numero[num // (base**x)]

        num %= base**x
    
    return int(convertido)

def separar_numero(n):

    separado = []

    for d in str(n):

        separado.append(int(d))

    return separado

def elevar_y_sumar(lista, b):

    resultado = 0

    for d in lista:

        resultado += d**d

    return convertir_base(resultado, b)

n = 1

b = int(input("Introduce la base (3 o 4): "))

encontrados = 0

while True:

    if elevar_y_sumar(separar_numero(convertir_base(n, b)), b) == convertir_base(n, b):

        print(str(convertir_base(n, b)) + " Es un numero de Munchausen")

        encontrados += 1
    
    if encontrados == 3:
        
        break

    n += 1
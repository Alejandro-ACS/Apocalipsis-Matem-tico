def separar_numero(n):

    separado = []

    for d in str(n):

        separado.append(int(d))

    return separado

def reordenar_m(lista):

    lista.sort()

    nuevo_n = ""

    for numero in lista:

        nuevo_n += str(numero)
    
    nuevo_n = int(nuevo_n)

    return nuevo_n

def reordenar_M(lista):

    lista.sort()

    lista = lista[::-1]

    nuevo_n = ""

    for numero in lista:

        nuevo_n += str(numero)
    
    nuevo_n = int(nuevo_n)

    return nuevo_n

intervalo = int(input("¿De cuantas cifras quieres calcular la constante? >> "))-1

n = 10**intervalo

resultados = []

while True:

    if reordenar_M(separar_numero(n))-reordenar_m(separar_numero(n)) != 0:

        resultados.append(reordenar_M(separar_numero(n))-reordenar_m(separar_numero(n)))

    n += 1

    if n == 10**(intervalo+1):

        break

posible_kaprekar = []

for element in resultados:

    if reordenar_M(separar_numero(element))-reordenar_m(separar_numero(element)) == element:

        posible_kaprekar.append(element)

resultado = []

for elemento in posible_kaprekar:

    if elemento not in resultado:

        resultado.append(elemento)

if resultado == []:

    print("No existe una constante Kaprekar")

elif len(resultado) == 1:

    print("Constante Kaprekar: " + str(resultado))

else:

    print("Constantes Kaprekar: " + str(resultado))
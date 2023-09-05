"""
    Se pide escribir un programa que nos calcule la suma de los 4 primeros números pares desde un número que introducimos por teclado. 
    Es decir, si insertamos un 5, nos haga la suma de 6+8+10+12
"""
print("**Este programa calcula la suma de 4 numeros pares")
numero = int(input("Ingresa un numero: "))

print("\n____________Programa iniciado____________")
print(f'- Numero ingresado: {numero}')

def detectar(tipo):
    tipo = numero % 2

    if tipo == 0:
        positionUno = numero + 2
        positionTwo = numero + 4
        positionThree = numero + 6
        positionFour = numero + 8

        x = [positionUno, positionTwo, positionThree, positionFour]
        print(f"\n- Listado de numeros pares a partir del {numero} \n  Numeros: {x}")

        suma = int(positionUno + positionTwo + positionThree + positionFour)

        print(f"\n- La suma de los numeros pares es igual a:\n  Numeros: {x} = {suma}")

    elif tipo >= 0:
        positionUno = numero + 1
        positionTwo = numero + 3
        positionThree = numero + 5
        positionFour = numero + 7

        x = [positionUno, positionTwo, positionThree, positionFour]
        print(f"\n- Listado de numeros pares a partir del {numero} \n  Numeros: {x}")

        suma = int(positionUno + positionTwo + positionThree + positionFour)

        print(f"\n- La suma de los numeros pares es igual a:\n  Numeros: {x} = {suma}")

    else:
        print("Error")
    
    print("____________Programa finalizado____________")
detectar('tipo')
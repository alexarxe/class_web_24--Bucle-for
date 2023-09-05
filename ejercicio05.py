"""
    Cargar una lista de N componentes. Hallar e imprimir el promedio de los valores impares.
"""
print("\n____________Programa iniciado____________")

n = [ ]

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))
num3 = int(input("Ingrese un valor: "))

n = [num1, num2, num3]

print(f'\n- Lista de valores: {n}')

def impares( a, b, c):
    # SECCION 1
    valor = int(num1)
    a = valor % 2

    if a >= 1:
        print(f'\n- El valor {num1} es un numero impar')
        elements = len(n)
        a = num1 / elements

        print(f'- El promedio de {num1} es: {a}')
    elif a == 0:
        print()
    
    # SECCION 2
    valor = int(num2)
    b = valor % 2

    if b >= 1:
        print(f'\n- El valor {num2} es un numero impar')
        elements = len(n)
        b = num2 / elements

        print(f'- El promedio de {num2} es: {b}')
    elif b == 0:
        print()

    # SECCION 3
    valor = int(num3)
    c = valor % 2

    if c >= 1:
        print(f'\n- El valor {num3} es un numero impar')
        elements = len(n)
        c = num3 / elements

        print(f'- El promedio de {num3} es: {c}')
    elif c == 0:
        print()

impares('a', 'b', 'c')

print("____________Programa finalizado____________")
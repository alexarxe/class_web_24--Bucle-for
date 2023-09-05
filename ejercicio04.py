"""
    Cargar una lista con N numeros y luego hallar el promedio de los elementos en él que no sean cero.
"""
print("\n____________Programa iniciado____________")

n = [ ]

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))
num3 = int(input("Ingrese un valor: "))

n = [num1, num2, num3]

print(f'\n- Lista de valores: {n}')

def promedio(a, b, c):
    a = int(num1)
    elements = len(n)
    a = a / elements

    if a >= 0.1:
        print(f'- El promedio de {num1} es igual a:')
        print(float(a))
    elif a <= 0:
        print()

    b = int(num2)
    elements = len(n)
    b = b / elements

    if b >= 0.1:
        print(f'- El promedio de {num2} es igual a:')
        print(float(b))
    elif b <= 0:
        print()

    c = int(num3)
    elements = len(n)
    c = c / elements

    if c >= 0.1:
        print(f'- El promedio de {num3} es igual a:')
        print(float(c))
    elif c <= 0:
        print()

promedio('a', 'b', 'c')

print("____________Programa finalizado____________")
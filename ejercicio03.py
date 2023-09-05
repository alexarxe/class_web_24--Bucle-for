"""
    Cargar una lista de N numeros, sumar sus componentes e imprimir la suma y el promedio de los números.
"""

n = [ ]
print("\n____________Programa iniciado____________")

for x in range(5):
    valor = int(input("Ingrese un valor: "))
    n.append(valor)

def calculo(suma, promedio):
    suma = 0

    for num in n:
        suma = suma + num
    
    print(f'\n- La suma es de los numeros es igual a {suma}')

    elementos = len(n)
    promedio = suma / elementos

    print(f'\n- El promedio de la suma es igual a {promedio}')
    print("____________Programa finalizado____________")
calculo('suma', 'promedio')

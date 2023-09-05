"""
    1- Escribir un programa que nos calcule el cuadrado de los 9 primeros
    numeros naturales (utiliza la estructura for)
"""
print("\n____________Programa iniciado____________")
def calculo():
    print("1- Escribir un programa que nos calcule el cuadrado de los 9 primeros \n numeros naturales (utiliza la estructura for) \n")

    numeroNaturales = ["1", "2", "3", "4", "5", "6", "7", "8"]

    for i in numeroNaturales:
        cuadrado = int(i)
        raiz = int(cuadrado * cuadrado)
        print(f"El cuadrado de {cuadrado} es {raiz}")
    
    print("____________Programa finalizado____________")
calculo()
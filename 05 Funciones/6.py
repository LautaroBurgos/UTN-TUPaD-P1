def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

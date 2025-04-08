# Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
total = 0
while True:
    num = int(input("Introduzca un numero (introduzca 0 para terminar): "))
    if num == 0:
        break
    total += num
print("Suma total:", total)

# ) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
n = int(input("Introduzca un numero entero positivo: "))
suma = sum(range(n + 1))
print("Suma:", suma)

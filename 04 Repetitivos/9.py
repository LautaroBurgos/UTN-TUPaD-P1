# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)
cantidad = 100
total = 0
for _ in range(cantidad):
    num = int(input("Introduzca un numero: "))
    total += num
media = total / cantidad
print("Media:", media)

# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Introduzca el primer numero: "))
fin = int(input("Introduzca el segundo numero: "))
suma = 0
for i in range(min(inicio, fin) + 1, max(inicio, fin)):
    suma += i
print("Suma:", suma)

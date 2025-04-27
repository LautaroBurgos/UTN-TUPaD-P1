# Ejercicio 5:
# Analizar el siguiente programa y explicar con tus palabras qué realiza.
#Define una lista que contiene numeros enteros
numeros = [8,15,3,22,7]
# max(numeros) -> devuelve el numero mas grande dentro de la lista,  en este
#caso 22.
#numeros.remove elimina el elemento que se le pasa por parametro , de la lista, en este caso el 22
numeros.remove(max(numeros))
#print(numeros)-> Imprime por pantalla la lista de numeros , con el valor 22 removido.
print(numeros)
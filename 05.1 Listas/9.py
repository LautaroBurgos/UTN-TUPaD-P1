# Ejercicio 9:
# Dada la lista “compras”, realizar las siguientes operaciones:
# a) Agregar "jugo" a la lista del tercer cliente
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
# c) Eliminar "pan" de la lista del primer cliente
# d) Imprimir la lista resultante

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

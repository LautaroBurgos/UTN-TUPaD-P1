
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel mas bajo: "))
print("Total de bloques necesarios:", contar_bloques(niveles))
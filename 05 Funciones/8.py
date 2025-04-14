def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Introduce tu peso (KG): "))
altura = float(input("Introduce tu altura (Metros): "))
print("Tu indice de masa corporal es:", round(calcular_imc(peso, altura), 2))

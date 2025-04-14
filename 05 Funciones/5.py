def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Introduce la cantidad de segundos: "))
print("Equivalente en horas:", segundos_a_horas(segundos))

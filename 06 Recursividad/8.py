def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito (0-9): "))
print(f"El digito {digito} aparece {contar_digito(numero, digito)} veces.")

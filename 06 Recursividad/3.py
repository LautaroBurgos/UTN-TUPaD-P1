def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")
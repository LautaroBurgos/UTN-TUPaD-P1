def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

num = int(input("Ingrese un numero entero positivo: "))
print("Suma de sus digitos:", suma_digitos(num))

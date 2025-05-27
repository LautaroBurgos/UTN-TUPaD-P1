def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un numero en decimal: "))
binario = decimal_a_binario(num)
print("Binario:", binario if binario else "0")

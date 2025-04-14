def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Error : Division por cero")

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}\nResta: {resta}\nMultiplicacion: {multiplicacion}\nDivision: {division}")

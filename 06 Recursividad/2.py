def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese la cantidad de terminos de fibonacci: "))
for i in range(pos):
    print(fibonacci(i), end=" ")
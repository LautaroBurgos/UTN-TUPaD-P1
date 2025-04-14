def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

celsius = float(input("Introduce la temperatura en grados Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))

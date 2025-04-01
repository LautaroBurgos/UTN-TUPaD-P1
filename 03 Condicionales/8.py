nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no valida")
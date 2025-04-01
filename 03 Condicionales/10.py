hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el numero del mes (1-12): "))
dia = int(input("Ingrese el dia del mes: "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (10 <= mes <= 12 and (mes != 12 or dia <= 20)):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print(f"Estacion: {estacion_norte}")
else:
    print(f"Estacion: {estacion_sur}")
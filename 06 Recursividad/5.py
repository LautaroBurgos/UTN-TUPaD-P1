def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print("Es palindromo:", es_palindromo(palabra))

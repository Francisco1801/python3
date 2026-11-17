frase = input("Dime una frase: ")
letra = input("Dime una letra: ")

contador = 0

for i in range(len(frase)):
    if frase[i] == letra:
        contador = contador + 1

print("La letra aparece", contador, "veces")
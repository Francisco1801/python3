nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (hombre o mujer): ")

if sexo.lower() == "mujer" and nombre.lower() < "m":
    print("Perteneces al grupo A")
elif sexo.lower() == "hombre" and nombre.lower() > "n":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

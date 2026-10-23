pizza = input("¿Quieres una pizza vegetariana? (si/no): ")

if pizza == "si":
    print("Ingredientes vegetarianos:")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente = input("Elige un ingrediente: ")

    if ingrediente == "1":
        print("Tu pizza es vegetariana")
        print("Ingredientes: mozzarella, tomate y pimiento")
    elif ingrediente == "2":
        print("Tu pizza es vegetariana")
        print("Ingredientes: mozzarella, tomate y tofu")
    else:
        print("Ingrediente no valido")

elif pizza == "no":
    print("Ingredientes no vegetarianos:")
    print("1. Peperoni")
    print("2. Jamon")
    print("3. Salmon")
    ingrediente = input("Elige un ingrediente: ")

    if ingrediente == "1":
        print("Tu pizza no es vegetariana")
        print("Ingredientes: mozzarella, tomate y peperoni")
    elif ingrediente == "2":
        print("Tu pizza no es vegetariana")
        print("Ingredientes: mozzarella, tomate y jamon")
    elif ingrediente == "3":
        print("Tu pizza no es vegetariana")
        print("Ingredientes: mozzarella, tomate y salmon")
    else:
        print("Ingrediente no valido")

else:
    print("Respuesta no valida")
producto = input("Nombre del producto: ")
precio = float(input("Precio: "))
unidades = int(input("Número de unidades: "))

total = precio * unidades

print(f"{producto} {precio:09.2f} {unidades:03d} {total:011.2f}")
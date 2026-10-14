precio = float(input("Introduce el precio: "))

euros = int(precio)
centimos = int((precio - euros) * 100)

print("Euros:", euros)
print("Céntimos:", centimos)
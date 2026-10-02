pan = int(input("¿Cuasntas barras has vendido que no son del dia?: "))

precio_original = 3.49
descuento = 0.60

precio_descuento = precio_original * (1 - descuento)
coste = pan * precio_descuento

print (f"El precio habitual de una barra de pan es {precio_original}, el precio con el descuento del 60% es {round(precio_descuento, 2)}, el coste final de las barras vendidas con el descuento es de {coste}")
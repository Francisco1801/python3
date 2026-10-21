puntuacion = float(input("Introduce tu puntuación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = "Puntuación no válida"

dinero = 2400 * puntuacion

print("Nivel de rendimiento:", nivel)
print("Dinero recibido:", dinero, "euros")

cant = int(input("Introduce la cantidad a invertir: "))
interes =  float(input("Interes Anual (%): "))
años = int(input("Numero de años: "))
capital = cant * (1+interes /100) ** años
print(f"El capital obtenido es: {capital}")

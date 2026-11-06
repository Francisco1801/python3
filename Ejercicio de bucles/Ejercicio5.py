num = float(input("Cantidad a invertir: "))
interes = float(input("Interes anual en %: "))
años = int(input("Numero de años: "))

for i in range(1, años+1):
    num = num * (1 + interes / 100)
    print("Año", i, ":", round(num, 2), "€")
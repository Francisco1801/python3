num = int(input("Introduce un numero entero: "))

primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False

if primo and num > 1:
    print("El numero es primo")
else:
    print("El numero no es primo")
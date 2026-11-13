num = int(input("Dime un numero entero: "))

for i in range(1, num+1):
    for j in range(2*i-1, 0, -2):
        print(j, end=" ")
    print()
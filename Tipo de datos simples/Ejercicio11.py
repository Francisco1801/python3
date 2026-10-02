deposito = int(input("Dime la cantidad de dinero en tu cuneta de ahorro: "))

año1 = deposito * 1.04
año2 = año1 * 1.04
año3 = año2 * 1.04

print(f"En primer año tendras {round(año1)}, el segundo año tendras {round(año2)}, el tercer año tendras {round(año3)}")
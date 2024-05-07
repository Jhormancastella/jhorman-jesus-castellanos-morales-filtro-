import os
os.system('cls')

def pesos_a_dolares(pesos):
    return pesos / 3944

def pesos_a_euros(pesos):
    return pesos / 3944

def euros_a_pesos(euros):
    return euros * 4279

def pesos_a_yenes(pesos):
    return pesos * 26.30

def yenes_a_pesos(yenes):
    return yenes / 26.30

def main():
    print("1. Pesos a Dólares")
    print("2. Pesos a Euros")
    print("3. Euros a Pesos")
    print("4. Pesos a Yenes")
    print("5. yenes a pesos")
    
    opcion = int(input("Ingrese el número de la operación que desea realizar: "))
    
    if opcion == 1:
        pesos = float(input("Ingrese la cantidad de pesos: "))
        print("Dólares:", pesos_a_dolares(pesos))
    elif opcion == 2:
        pesos = float(input("Ingrese la cantidad de pesos: "))
        print("Euros:", pesos_a_euros(pesos))
    elif opcion == 3:
        euros = float(input("Ingrese la cantidad de euros: "))
        print("Pesos:", euros_a_pesos(euros))
    elif opcion == 4:
        pesos = float(input("Ingrese la cantidad de pesos: "))
        print("Yenes:", pesos_a_yenes(pesos))
    elif opcion == 5:
        yenes = float(input("ingrese la cantidad de yenes:"))
        print("yenes:", yenes_a_pesos(yenes))
    else:
        print('Opcion ingresada no pertenece al menu de opciones')
        main(0)



if __name__ == "__main__":
    main()

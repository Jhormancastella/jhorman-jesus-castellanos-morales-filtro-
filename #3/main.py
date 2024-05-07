import json
import os
os.system('cls')
def registrarProductos():
    productos = []
    while True:
        producto = {}
        producto['id'] = input("Ingrese el ID del producto: ")
        producto['nombre'] = input("Ingrese el nombre del producto: ")
        producto['valorUnitario'] = float(input("Ingrese el valor unitario del producto: "))
        producto['stockmin'] = int(input("Ingrese el stock mínimo del producto: "))
        producto['stockmax'] = int(input("Ingrese el stock máximo del producto: "))
        productos.append(producto)
        
        continuar = input("¿Desea registrar otro producto? (si/no): ").lower()
        if continuar != 'si':
            break
    with open('data/productos.json', 'w') as archivo:
        json.dump(productos, archivo)

if __name__ == "__main__":
    registrarProductos()

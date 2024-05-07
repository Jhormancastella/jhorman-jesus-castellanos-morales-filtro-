import os
os.system('cls')
def leer_informacion_usuario():
    usuario = {}
    usuario['id'] = input("Ingrese el ID del usuario: ")
    usuario['nombres'] = input("Ingrese los nombres del usuario: ")
    usuario['apellidos'] = input("Ingrese los apellidos del usuario: ")
    usuario['ubicación'] = input("Ingrese la ubicación del usuario: ")
    usuario['dirección'] = input("Ingrese la dirección del usuario: ")
    usuario['ciudad'] = input("Ingrese la ciudad del usuario: ")
    usuario['longitud'] = input("Ingrese la longitud del usuario: ")
    usuario['latitud'] = input("Ingrese la latitud del usuario: ")
    usuario['email'] = input("Ingrese el email del usuario: ")
    usuario['edad'] = input("Ingrese la edad del usuario: ")
    usuario['ocupación'] = input("Ingrese la ocupación del usuario: ")
    
    return usuario

if __name__ == "__main__":
    informacion_usuario = leer_informacion_usuario()
    print("Información del usuario:", informacion_usuario)
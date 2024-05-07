import modules.corefile as cf
import funciones.globales as gf
import funciones.empleados as fe
import main

def MenuEmpleado(op: int):
    title = """
    ()()()()()()()()()()()()()()()
   ()menu de registro de empleado()
    ()()()()()()()()()()()()()()()
    """
    menuEmpleadosOp = '1. registro de empleado\n2. editar empleado\n3. Salir'
    gf.borrar_pantalla()
    if op != 4:
        print(title)
        print(menuEmpleadosOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 4):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuEmpleado(0)

        match op:
            case 1:
                try:
                    fe.Newempleado()
                except Exception as e:
                    print("Error al agregar paciente:", e)
                else:
                    print("Trabajador agregado exitosamente")
                gf.pausar_pantalla()
                MenuEmpleado(0)

            case 2:
                try:
                    fe.ModifyData()
                except Exception as e:
                    print("Error al editar Trabajador:", e)
                else:
                    print("Datos del Trabajador editados exitosamente")
                gf.pausar_pantalla()
                MenuEmpleado(0)

            case 3:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuEmpleado(0)

import modules.corefile as cf
import funciones.globales as gf
import funciones.resultados as rt
import funciones.colilla as fc
import main

def MenuResultados(op: int):
    title = """
    ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
   ()Consultar la colilla de pago de un determinado empleado.()
    ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
    """
    menuEmpleadosOp = '1. pagos de nomina\n2. colilla de pago\n3. Salir'
    gf.borrar_pantalla()
    if op != 4:
        print(title)
        print(menuEmpleadosOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 3
                                   ):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuResultados(0)

        match op:
            case 1:
                try:
                    rt.imprimir_monina()
                except Exception as e:
                    print("Error al agregar Trbajador:", e)
                else:
                    print("Trabjador agregado exitosamente")
                gf.pausar_pantalla()
                MenuResultados(0)

            case 2:
                try:
                    fc.imprimir_colilla()
                except Exception as e:
                    print("Error al imprimir colilla:", e)
                else:
                    print("Datos de colilla")
                gf.pausar_pantalla()
                MenuResultados(0)
            case 3:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuResultados(0)

import ui.uimnempleado as uimnp
import ui.uimnresultado as uiRt
import json
import os
import funciones.globales as fg
import modules.corefile as mc

def mainMenu(op):
    fg.borrar_pantalla()
    title = """
    **°°°**°°°**°°°****°°°**°°°**°°°****°°°**°°°**°°°**
                empresa de trabajadores
    **°°°**°°°**°°°****°°°**°°°**°°°****°°°**°°°**°°°**
            """
    mainMenuOp = "1. trabajadores\n2. pagos y colilla\3. salir" 
    if op != 3:
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('Error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            if opcion == 1:
                uimnp.MenuEmpleado(0)
            elif opcion == 2:
                uiRt.MenuResultados(0)
            elif opcion == 3:
                pass
            else:
                print('Opcion ingresada no pertenece al menu de opciones')
                fg.pausar_pantalla()
                mainMenu(0)

if __name__ == '__main__':
    mc.MY_DATABASE = 'data/trabajadores.json'
    mc.checkFile(fg.NominaDeTrabajo)
    mainMenu(0)
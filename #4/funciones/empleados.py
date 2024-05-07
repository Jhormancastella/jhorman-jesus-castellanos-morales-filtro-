import json
import os
import funciones.globales as gf
import modules.corefile as cfp
import ui.uimnempleado as uimp

def Newempleado():
    title = """
    *****************************
    * Registro De  Trabajadores *
    *****************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input("Ingrese el Nro de Identificacion: ")
    nombretrabajador = input("Ingrese Nombre del trabajador: ")
    Diastrabajados = int(input('ingrese dias trabajados: '))
    HorasExtras = int(input('Ingrese horas extras: '))
    ValorDia = int(input('ingrese el valor del dia'))
    descuentoxCafeteria = int(input('ingrese valor de descuento'))
    CuotaPrestamos = int(input('ingrese la cuota de prestamos'))
    print("Seleccione su cargo:")
    print("1. Almacenista")
    print("2. Jefe IT")
    print("3. Administrador")
    print("4. Mensajero")
    print("5. Gerente")
    cargo = input("Ingrese el número correspondiente a la especialización: ")
    cargos = ["Almacenista", "jefe IT", "Administrador", "Mensajero", "Gerente"]
    cargo= cargos[int(cargo) - 1]
    trabajador = {
        'identificacion': identificacion,
        'nombreTrabajador': nombretrabajador,
        'cargo': cargos,
        'Diastrabajados': Diastrabajados,
        'HorasExtras': HorasExtras,
        'valorDia': ValorDia,
        'descuentoxCafeteria': descuentoxCafeteria,
        'CuotaPrestamos': CuotaPrestamos
    }
    cfp.AddData('data', identificacion, trabajador)
    gf.NominaDeTrabajo.get('data').update({identificacion: trabajador})
    if bool(input('Desea registrar otro Trabajador (Sí) o Enter (No): ')):
        Newempleado()
    else:
        uimp.MenuEmpleado(0)

def SearchData():
    criterio = input('Ingrese el Nro de Identificacion del Trabajador: ')
    data = gf.NominaDeTrabajo.get('data').get(criterio)
    return data

def ModifyData():
    dataTrabajador = SearchData()
    if dataTrabajador:
        identificacion, nombreEspecialista, cargo = dataTrabajador.values()
        for key in dataTrabajador.keys():
            if key not in ['identificacion', 'cargo']:
                if bool(input(f'Desea modificar {key} (sí) o Enter (No): ')):
                    if key == 'Trabajador':
                        print("Seleccione trabajo:")
                        print("1. Almacenista")
                        print("2. Jefe IT")
                        print("3. Administrador")
                        print("4. Mensajero")
                        print("5. Gerente")
                        especializacion = input("Ingrese el número correspondiente Cargo: ")
                        especializaciones = ["Almacenista", "Jefe IT", "Administrador", "Mensajero", "Gerente"]
                        dataTrabajador[key] = especializaciones[int(especializacion) - 1]
                    elif key == 'jornada':
                        print("Seleccione nuevo Horario:")
                        print("1. Mañana")
                        print("2. Tarde")
                        horario = input("Ingrese el número correspondiente al horario: ")
                        horarios = ["Mañana", "Tarde"]
                        dataTrabajador[key] = horarios[int(horario) - 1]
                    else:
                        dataTrabajador[key] = input(f'Ingrese el nuevo valor para {key}: ')
        gf.NominaDeTrabajo.get('data').update({identificacion: dataTrabajador})
        cfp.UpdateFile(gf.NominaDeTrabajo)
        uimp.MenuEmpleado(0)
    else:
        print("Especialista no encontrado.")
        
def DeleteData():
    identificacion = input('Ingrese el Nro de Identificacion del especialista a eliminar: ')
    if identificacion in gf.centroClinico.get('data'):
        del gf.centroClinico.get('data')[identificacion]
        cfp.UpdateFile(gf.centroClinico)
        print("Especialista eliminado correctamente.")
        uimp.MenuEmpleado(0)
    else:
        print("Especialista no encontrado.")


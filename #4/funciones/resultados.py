import json

def imprimir_monina(identificacion):
    try:
        with open("data/trabjadores.json", "r") as file:
            nomina = json.load(file)
            tratamiento = nomina.get(identificacion)
            if tratamiento:
                print("la nomina del trabajador es :",nomina)
            else:
                print("No se encontró la nomina del trabajador .")
    except FileNotFoundError:
        print("El archivo trabajadores.json no encontrado.")
    except json.JSONDecodeError:
        print("El archivo trabajadores no tiene un formato JSON válido.")
    except Exception as e:
        print("Se produjo un error:", e)

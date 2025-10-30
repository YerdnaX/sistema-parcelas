def menu() -> int:
    continuar = True
    while continuar:
        print("Menú de opciones")
        print("1: Parcela")
        print("2: Sensores")
        print("3: Lecturas de sensores")
        print("4: Alertas")
        print("5: Volumen de riesgo")
        print("6: Salir")
        opcion = obtenerInputUsuario()
        match opcion:
            case 1:
                opcionfinal = menuParcela()
                if opcionfinal == 17:
                    continue
                return opcionfinal
            case 2:
                opcionfinal = menuSensor()
                if opcionfinal == 27:
                    continue
                return opcionfinal
            case 3:
                opcionfinal = menuLecturaSensores()
                if opcionfinal == 35:
                    continue
                return opcionfinal
            case 4:
                opcionfinal = menuAlertas()
                if opcionfinal == 43:
                    continue
                return opcionfinal
            case 5:
                opcionfinal = menuVolumenRiesgo()
                if opcionfinal == 52:
                    continue
                return opcionfinal
            case 6:
                continuar = False
                print("Saliendo del menú...")
            case _:
                print("Opción no válida, intente de nuevo.")
                continue     
        return opcion

##Funciones de submenus / Retornan un valor sumando 10/20/30/40/50 al valor seleccionado segun el sub menu
def menuParcela() -> int:
    continuar = True
    while continuar:
        print("Menú de Parcelas")
        print("1: Agregar Parcela")               
        print("2: Modificar Parcela")
        print("3: Modificar Datos Generales de la Parcela")
        print("4: Eliminar Parcela")
        print("5: Ver Parcelas por ID")
        print("6: Ver Todas las Parcelas")
        print("7: Atras")
        opcionfinal = obtenerInputUsuario()
        if opcionfinal < 1 or opcionfinal > 7:
            print("Opción no válida, intente de nuevo.")
            continue
        return opcionfinal + 10

def menuSensor() -> int:
    continuar = True
    while continuar:
        print("Menú de Sensores")
        print("1: Agregar Sensor")               
        print("2: Modificar Sensor")
        print("3: Eliminar Sensor")
        print("4: Ver Sensor por ID")
        print("5: Ver Todos los Sensores")
        print("6: Ver Sensores por Parcela")
        print("7: Atras")
        opcionfinal = obtenerInputUsuario()
        if opcionfinal < 1 or opcionfinal > 7:
            print("Opción no válida, intente de nuevo.")
            continue
        return opcionfinal + 20
    
def menuLecturaSensores() -> int:
    continuar = True
    while continuar:
        print("Menú de Lecturas de Sensores")
        print("1: Agregar Lectura de Sensor")               
        print("2: Cargar Lecturas de Sensor desde el Archivo XML")
        print("3: Ver Lectura por parcela y sensor")
        print("4: Borrar informacion de sensor por fecha")
        print("5: Atras")
        opcionfinal = obtenerInputUsuario()
        if opcionfinal < 1 or opcionfinal > 5:
            print("Opción no válida, intente de nuevo.")
            continue
        return opcionfinal + 30
    
def menuAlertas() -> int:
    continuar = True
    while continuar:
        print("Menú de Alertas")
        print("1: Ver Alertas para fecha determinada")               
        print("2: Ver Alertar por parcela y fecha")
        print("3: Atras")
        opcionfinal = obtenerInputUsuario()
        if opcionfinal < 1 or opcionfinal > 3:
            print("Opción no válida, intente de nuevo.")
            continue
        return opcionfinal + 40

def menuVolumenRiesgo() -> int:
    continuar = True
    while continuar:
        print("Menú de Volumen de Riesgo")
        print("1: Calcular Volumen de Riesgo")               
        print("2: Atras")
        opcionfinal = obtenerInputUsuario()
        if opcionfinal < 1 or opcionfinal > 2:
            print("Opción no válida, intente de nuevo.")
            continue
        return opcionfinal + 50
    
def obtenerInputUsuario() -> int:
    try:
        opcionfinal = int(input("Seleccione una opción: "))
        return opcionfinal
    except ValueError:
        return -1
    

if __name__ == "__main__":
    menu()
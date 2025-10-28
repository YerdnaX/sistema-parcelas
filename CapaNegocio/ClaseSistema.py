import CapaNegocio.ClaseParcela as Parcela
import CapaNegocio.ClaseSensor as Sensor
import CapaNegocio.ClaseLectura as Lectura
import CapaNegocio.ClaseAlerta as Alertas
from CapaNegocio.ClaseValidaciones import *
import CapaDatos.ClaseJsonManager as JsonManager
import CapaDatos.ClaseXmlManager as XmlManager
from datetime import datetime

## Listas globales para almacenar los objetos en memorias ##
ListaParcelas = []
ListaSensores = []
ListaLecturas = []
ListaAlertas = []
Encontrada = False

################## Funciones de parcelas :D ##################

## agregar nueva parcela y actualiza el json de parcelas ##
def nuevaparcela():
    print("Creando una nueva parcela...")

    while True:
        idParcela = input("Ingrese el ID de la parcela: ")
        if ClaseValidaciones.esNumericoNoVacio(idParcela):
            if ClaseValidaciones.existeParcelaID(idParcela, ListaParcelas):
                print("El ID de la parcela ya existe. Ingrese un ID diferente.")
            else:
                break
        else:
            print("Ingrese un ID que sea un codigo de numeros enteros")

    while True:
        nombre = input("Ingrese el nombre de la parcela: ")
        if ClaseValidaciones.estaVacioString(nombre):
            break
        else:
            print("Ingrese un nombre adecuado")
    
    while True:
        ubicacion = input("Ingrese la ubicación de la parcela: ")
        if ClaseValidaciones.estaVacioString(ubicacion):
            break
        else:
            print("Ingrese una ubicacion adecuado")

    while True:
        tipoCultivo = input("Ingrese el tipo de cultivo: ")
        if ClaseValidaciones.estaVacioString(tipoCultivo):
            break
        else:
            print("Ingrese un tipo de cultivo")

    while True:
        area = input("Ingrese el área de la parcela (en m²): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(area):
            break
        else:
            print("Ingrese un area en valores numericos")

    while True:
        profundidadRaiz = input("Ingrese la profundidad de la raíz (en cm): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(profundidadRaiz):
            break
        else:
            print("Ingrese una profundidad de raiz en valores numericos")
    
    while True:
        eficienciaRiego = input("Ingrese la eficiencia de riego (en %): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(eficienciaRiego):
            break
        else:
            print("Ingrese una eficiencia de riego en valores numericos")

    while True:
        umbralHumedadMin = input("Ingrese el umbral de humedad mínimo (en %): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(umbralHumedadMin):
            break
        else:
            print("Ingrese un umbral de humedad minino en valores numericos")

    while True:
        umbralHumedadMax = input("Ingrese el umbral de humedad máximo (en %): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(umbralHumedadMax):
            if float(umbralHumedadMax) > float(umbralHumedadMin):
                break
            else:
                print("El umbral de humedad maximo debe ser mayor al umbral de humedad minimo")
        else:
            print("Ingrese un umbral de humedad maximo en valores numericos")



    while True:
        volumenDeseado = input("Ingrese el volumen deseado de agua (en litros): ")
        if ClaseValidaciones.esNumericoNoVacioFloat(volumenDeseado):
            break
        else:
            print("Ingrese un volumen deseado en valores numericos")

    parcela = Parcela.ClaseParcela(idParcela, nombre, ubicacion, tipoCultivo, area, profundidadRaiz, eficienciaRiego, umbralHumedadMin, umbralHumedadMax, volumenDeseado)
## agrega a lista en memoria
    ListaParcelas.append(parcela)
## genera una lista de diccionarios para guardar en json
    Parcelasguardar = [parcela.transformarDiccionario() for parcela in ListaParcelas]
## guarda en json a partir del diccionario creado
    JsonManager.guardarParcelaJson(Parcelasguardar, "./Parcelas.json")
    print("Parcela agregada exitosamente.")

## leer el json de parcelas y cargar en la lista en memoria ##
def leerParcelasJson():
    ListaParcelas.clear()
    datosParcelas = JsonManager.cargarParcelaJson("./Parcelas.json")
    for diccionario in datosParcelas:
        parcela = Parcela.ClaseParcela.crearDesdeDiccionario(diccionario)
        ListaParcelas.append(parcela)

## modificar parcela existente ##
def modificarParcela():
    idparcelamodificar = input("Ingrese el ID de la parcela que desea modificar: ")
    for parcela in ListaParcelas:
        if parcela.idParcela == idparcelamodificar:
            Encontrada = True
            print("Parcela encontrada. Ingrese los nuevos datos:")
            
            while True:
                parcela.nombre = input("Ingrese el nuevo nombre de la parcela: ")
                if ClaseValidaciones.estaVacioString(parcela.nombre):
                    break
                else:
                    print("Ingrese un nombre adecuado")

            while True:
                parcela.ubicacion = input("Ingrese la nueva ubicación de la parcela: ")
                if ClaseValidaciones.estaVacioString(parcela.ubicacion):
                    break
                else:
                    print("Ingrese una ubicacion adecuado")
            
            while True:
                parcela.tipoCultivo = input("Ingrese el nuevo tipo de cultivo: ")
                if ClaseValidaciones.estaVacioString(parcela.tipoCultivo):
                    break
                else:
                    print("Ingrese un tipo de cultivo")
            
            while True:
                area = input("Ingrese la área de la parcela (en m²): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(area):
                    parcela.area = float(area)
                    break
                else:
                    print("Ingrese un area en valores numericos")

            while True:
                parcela.profundidadRaiz = input("Ingrese la nueva profundidad de la raíz (en cm): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(parcela.profundidadRaiz):
                    break
                else:
                    print("Ingrese una profundidad de raiz en valores numericos")
            
            while True:
                parcela.eficienciaRiego = input("Ingrese la nueva eficiencia de riego (en %): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(parcela.eficienciaRiego):
                    break
                else:
                    print("Ingrese una eficiencia de riego en valores numericos")

            while True:
                parcela.umbralHumedadMin = input("Ingrese el nuevo umbral de humedad mínimo (en %): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(parcela.umbralHumedadMin):
                    break
                else:
                    print("Ingrese un umbral de humedad minino en valores numericos")

            while True:
                parcela.umbralHumedadMax = input("Ingrese el nuevo umbral de humedad máximo (en %): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(parcela.umbralHumedadMax):
                    if float(parcela.umbralHumedadMax) > float(parcela.umbralHumedadMin):
                        break
                    else:
                        print("El umbral de humedad maximo debe ser mayor al umbral de humedad minimo")
                else:
                    print("Ingrese un umbral de humedad maximo en valores numericos")

            while True:
                parcela.volumenDeseado = input("Ingrese el nuevo volumen deseado de agua (en litros): ")
                if ClaseValidaciones.esNumericoNoVacioFloat(parcela.volumenDeseado):
                    break
                else:
                    print("Ingrese un volumen deseado en valores numericos")

            Parcelasguardar = [parcela.transformarDiccionario() for parcela in ListaParcelas]
            JsonManager.guardarParcelaJson(Parcelasguardar, "./Parcelas.json")
            print("Parcela modificada exitosamente.")
            return
    if not Encontrada:
        print("Parcela no encontrada.")

## eliminar parcela existente ##
def eliminarParcela():
    while True:
        idparcelaeliminar = input("Ingrese el ID de la parcela que desea modificar: ")
        if ClaseValidaciones.esNumericoNoVacio(idparcelaeliminar):
            break
        else:
            print("Ingrese un ID que sea un codigo de numeros enteros")

    for parcela in ListaParcelas:
        if parcela.idParcela == int(idparcelaeliminar):
            ListaParcelas.remove(parcela)
            Parcelasguardar = [parcela.transformarDiccionario() for parcela in ListaParcelas]
            JsonManager.guardarParcelaJson(Parcelasguardar, "./Parcelas.json")
            print("Parcela eliminada exitosamente.")
            return
    print("Parcela no encontrada.")

## ver parcela por ID ##
def verParcelaPorID(): 
    while True:
        idparcelaver = input("Ingrese el ID de la parcela que desea ver: ")
        if ClaseValidaciones.esNumericoNoVacio(idparcelaver):
            break
        else:
            print("Ingrese un ID que sea un codigo de numeros enteros")
    for parcela in ListaParcelas:
        if parcela.idParcela == idparcelaver:
            print(parcela)
            return
    print("Parcela no encontrada.")

## ver todas las parcelas ##
def verTodasLasParcelas():
    if not ListaParcelas:
        print("No hay parcelas registradas.")
        return
    for parcela in ListaParcelas:
        print(parcela)



################## Funciones de sensores :D ##################

## Funciones de lecturas de sensores :D ##
def nuevoSensor():
    print("Creando una nuevo Sensor...")

    while True:
        idSensor = input("Ingrese el ID del sensor: ")
        if ClaseValidaciones.esNumericoNoVacio(idSensor):
            if ClaseValidaciones.existeSensorID(idSensor, ListaSensores):
                print("El ID del sensor ya existe. Ingrese un ID diferente.")
            else:
                break
        else:
            print("Ingrese un ID que sea un codigo de numeros enteros")
    
    while True:
        tipo = input("Ingrese el tipo de sensor (HumedadSuelo/Temperatura/LLuvia):  ").lower()
        if ClaseValidaciones.esValidoTipoSensor(tipo):
            break
        else:
            print("Ingrese un tipo de sensor adecuado")

    while True:
        idParcela = input("Ingrese el ID de la parcela asociada al sensor: ")
        if ClaseValidaciones.esNumericoNoVacio(idParcela):
            if ClaseValidaciones.existeParcelaID(idParcela, ListaParcelas):
                break
            else:
                print("El ID de la parcela no existe. Ingrese un ID válido.")
        else:
            print("Ingrese un ID que sea un codigo de numeros enteros")

    while True:
        estado = input("Ingrese el estado del sensor (Activo/Inactivo/Mantenimiento o Revision): ").lower()
        if ClaseValidaciones.esValidoEstadoSensor(estado):
            break
        else:
            print("Ingrese un estado válido: activo, inactivo, mantenimiento o revision")

    while True:
        ubicacionParcela = input("Ingrese la ubicación del sensor en la parcela: ")
        if ClaseValidaciones.estaVacioString(ubicacionParcela):
            break
        else:
            print("Ingrese una ubicacion adecuada")

    while True:
        unidadMedida = input("Ingrese la unidad de medida del sensor: ")
        if ClaseValidaciones.estaVacioString(unidadMedida):
            break
        else:
            print("Ingrese una unidad de medida adecuada")

    while True:
        rangoValido = input("Ingrese el rango válido de medición del sensor: ")
        if ClaseValidaciones.estaVacioString(rangoValido):
            break
        else:
            print("Ingrese un rango válido adecuado")

    sensor = Sensor.ClaseSensor(idSensor, tipo, idParcela, estado, ubicacionParcela, unidadMedida, rangoValido)
## agrega a lista en memoria
    ListaSensores.append(sensor)
## genera una lista de diccionarios para guardar en json
    Sensoresguardar = [sensor.transformarDiccionario() for sensor in ListaSensores]
## guarda en json a partir del diccionario creado
    JsonManager.guardarSensorJson(Sensoresguardar, "./Sensores.json")
    print("Sensor agregado exitosamente.")

## leer el json de sensores y cargar en la lista en memoria ##
def leerSensoresJson():
    ListaSensores.clear()
    datosSensores = JsonManager.cargarSensorJson("./Sensores.json")
    for diccionario in datosSensores:
        sensor = Sensor.ClaseSensor.crearDesdeDiccionario(diccionario)
        ListaSensores.append(sensor)

## modificar sensor existente ## TESTEAR----------------------------
def modificarSensor():
    idsensormodificar = input("Ingrese el ID del sensor que desea modificar: ")
    for sensor in ListaSensores:
        if sensor.idSensor == idsensormodificar:
            print("Sensor encontrado. Ingrese los nuevos datos:")

            while True:
                sensor.tipo = input("Ingrese el nuevo tipo de sensor (HumedadSuelo/Temperatura/LLuvia):  ").lower()
                if ClaseValidaciones.esValidoTipoSensor(sensor.tipo):
                    break
                else:
                    print("Ingrese un tipo de sensor adecuado")
            
            while True:
                sensor.idParcela = input("Ingrese el nuevo ID de la parcela asociada al sensor: ")
                if ClaseValidaciones.esNumericoNoVacio(sensor.idParcela):
                    if ClaseValidaciones.existeParcelaID(sensor.idParcela, ListaParcelas):
                        break
                    else:
                        print("El ID de la parcela no existe. Ingrese un ID válido.")
            
            while True:
                sensor.estado = input("Ingrese el nuevo estado del sensor (activo/inactivo): ")
                if ClaseValidaciones.esValidoEstadoSensor(sensor.estado):
                    break
                else:
                    print("Ingrese un estado de sensor adecuado")

            while True:
                sensor.ubicacionParcela = input("Ingrese la nueva ubicación del sensor en la parcela: ")
                if ClaseValidaciones.estaVacioString(sensor.ubicacionParcela):
                    break
                else:
                    print("Ingrese una ubicación adecuada")

            while True:
                sensor.unidadMedida = input("Ingrese la nueva unidad de medida del sensor: ")
                if ClaseValidaciones.estaVacioString(sensor.unidadMedida):
                    break
                else:
                    print("Ingrese una unidad de medida adecuada")

            while True:
                sensor.rangoValido = input("Ingrese el nuevo rango válido de medición del sensor: ")
                if ClaseValidaciones.estaVacioString(sensor.rangoValido):
                    break
                else:
                    print("Ingrese un rango válido adecuado")

            Sensoresguardar = [sensor.transformarDiccionario() for sensor in ListaSensores]
            JsonManager.guardarSensorJson(Sensoresguardar, "./Sensores.json")
            print("Sensor modificado exitosamente.")
            return
    print("Sensor no encontrado.")

##  eliminar sensor existente ##
def eliminarSensor():
    idsensormodificar = input("Ingrese el ID del sensor que desea modificar: ")
    for sensor in ListaSensores:
        if sensor.idSensor == idsensormodificar:
            ListaSensores.remove(sensor)
            Sensoresguardar = [sensor.transformarDiccionario() for sensor in ListaSensores]
            JsonManager.guardarSensorJson(Sensoresguardar, "./Sensores.json")
            print("Sensor eliminado exitosamente.")
            return
    print("Sensor no encontrado.")

## ver sensor por ID ##
def verSensorPorID():
    idsensorver = input("Ingrese el ID del sensor que desea ver: ")
    for sensor in ListaSensores:
        if sensor.idSensor == idsensorver:
            print(sensor)
            return
    print("Sensor no encontrado.")

## ver todos los sensores ##
def verTodosLosSensores(): 
    
    if not ListaSensores:
        print("No hay sensores registrados.")
        return
    for sensor in ListaSensores:
        print(sensor)


######################## Funciones de lecturas de sensores :D ########################


## agregar nueva lectura y actualiza el json de lecturas  ----- VALIDAR SI FUNCIONAAAAAAAA
def nuevaLectura():
    print("Creando una nueva lectura de sensor...")

    while True:
        idLectura = input("Ingrese el ID de la lectura: ")
        if ClaseValidaciones.existeLectura(idLectura, ListaLecturas):
            print("El ID de la lectura ya existe. Ingrese un ID diferente.")
        else:
            break

    while True:
        idSensor = input("Ingrese el ID del sensor: ")
        if ClaseValidaciones.existeSensorID(idSensor, ListaSensores):
            break
        else:
            print("El ID del sensor no existe. Ingrese un ID válido.")

    while True:
        idParcela = input("Ingrese el ID de la parcela: ")
        if ClaseValidaciones.existeParcelaID(idParcela, ListaParcelas):
            break
        else:
            print("El ID de la parcela no existe. Ingrese un ID válido.")

    fechaHora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    while True:
        valorMedido = input("Ingrese el valor medido: ")
        if ClaseValidaciones.esNumericoNoVacioFloat(valorMedido):
            break
        else:
            print("Ingrese un valor medido en valores numericos")

    ##Crear el objeto lectura 
    lectura = Lectura.ClaseLectura(idLectura, idSensor, idParcela, fechaHora, valorMedido)
    ## agrega a lista en memoria
    ListaLecturas.append(lectura)
    ## genera una lista de diccionarios para guardar en json
    Lecturasguardar = [lectura.transformarDiccionario() for lectura in ListaLecturas]
    ## guarda en json a partir del diccionario creado
    JsonManager.guardarLecturaSensorJson(Lecturasguardar, "./Lecturas.json")
    print("Lectura de sensor agregada exitosamente.")
    determinarAlertas(lectura)

## cargar lecturas de sensores desde archivo XML ## 
def cargarLecturasSensoresXML():

    lecturas = XmlManager.cargarLecturasXML()
    for diccionario in lecturas:
        lectura = Lectura.ClaseLectura.crearDesdeDiccionario(diccionario)
        ids = [lecturamemoria.idLectura for lecturamemoria in ListaLecturas]
        if lectura.idLectura not in ids:
            ListaLecturas.append(lectura)
    guardar = [lectura.transformarDiccionario() for lectura in ListaLecturas]
    JsonManager.guardarLecturaSensorJson(guardar, "./Lecturas.json")

## leer el json de lecturas y cargar en la lista en memoria ##
def leerLecturasJson():
    ListaLecturas.clear()
    datosLecturas = JsonManager.cargarLecturaSensorJson("./Lecturas.json")
    for diccionjarioLectura in datosLecturas:
        lectura = Lectura.ClaseLectura.crearDesdeDiccionario(diccionjarioLectura)
        ListaLecturas.append(lectura)

## ver lectura por parcela y sensor ## TESTEAR SI FUNCIONA ----------------------------
def verLecturaPorParcelaYSensor():

    while True:
        idparcelaver = input("Ingrese el ID de la parcela que desea ver: ")
        if ClaseValidaciones.existeParcelaID(idparcelaver, ListaParcelas):
            break
        else:
            print("El ID de la parcela no existe. Ingrese un ID válido.")

    while True:
        idsensorver = input("Ingrese el ID del sensor que desea ver: ")
        if ClaseValidaciones.existeSensorID(idsensorver, ListaSensores):
            break
        else:
            print("El ID del sensor no existe. Ingrese un ID válido.")
            
    for lectura in ListaLecturas:
        if lectura.idParcela == idparcelaver and lectura.idSensor == idsensorver:
            print(lectura)
            return
    print("Lectura no encontrada.")

## borrar lecturas por fecha ## TESTEAR SI FUNCIONA ----------------------------
def borrarLecturaFecha():

    while True:
        fechaBorrar = input("Ingrese la fecha (YYYY-MM-DD) de las lecturas que desea borrar: ")
        if ClaseValidaciones.esFechaValida(fechaBorrar):
            break
        else:
            print("La fecha ingresada no es válida. Ingrese una fecha en el formato YYYY-MM-DD.")
    
    lecturasaborrar = [lectura for lectura in ListaLecturas if lectura.fechaHora.startswith(fechaBorrar)]
    if not lecturasaborrar:
        print("No se encontraron lecturas para la fecha especificada.")
        return
    for lectura in lecturasaborrar:
        ListaLecturas.remove(lectura)
    Lecturasguardar = [lectura.transformarDiccionario() for lectura in ListaLecturas]
    JsonManager.guardarLecturaSensorJson(Lecturasguardar, "./Lecturas.json")
    print(f"Se borraron {len(lecturasaborrar)} lecturas para la fecha {fechaBorrar}.")

## leer el json de lecturas y cargar en la lista en memoria
def leerLecturasJson():
    ListaLecturas.clear()
    datosLecturas = JsonManager.cargarLecturaSensorJson("./Lecturas.json")
    for diccionjarioLectura in datosLecturas:
        lectura = Lectura.ClaseLectura.crearDesdeDiccionario(diccionjarioLectura)
        ListaLecturas.append(lectura)

######################## Funciones de alertas :D ########################
def determinarAlertas(lectura):
    lecturaIDParcela = lectura.idParcela
    lecturaIDSensor = lectura.idSensor
    LecturaValorMedido = lectura.valorMedido
    for parcela in ListaParcelas:
        if parcela.idParcela == lecturaIDParcela:
            LecturaUmbralMin = parcela.umbralHumedadMin
            LecturaUmbralMax = parcela.umbralHumedadMax
            LecturaVolumenDeseado = parcela.volumenDeseado
            break
    for sensor in ListaSensores:
        if sensor.idSensor == lecturaIDSensor:
            tipoSensor = sensor.tipo
            break
    if tipoSensor == "humedadsuelo":
        alertanueva = Alertas.ClaseAlerta(lecturaIDParcela, lecturaIDSensor, tipoSensor, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), LecturaValorMedido, mensajeAlertaHumedadSuelo(LecturaValorMedido, LecturaUmbralMax))
        nuevaAlerta(alertanueva)
    if tipoSensor == "temperatura":
        pass
    if tipoSensor == "lluvia":
        pass

def nuevaAlerta(NuevaAlerta):
    ListaAlertas.append(NuevaAlerta)
    Alertasguardar = [alerta.transformarDiccionario() for alerta in ListaAlertas]
    JsonManager.guardarAlertaJson(Alertasguardar, "./Alertas.json")
    print("Alerta generada exitosamente.")
    ##HumedadSuelo/Temperatura/LLuvia

def mensajeAlertaHumedadSuelo(LecturaValorMedido, LecturaUmbralMax) -> str:
    if LecturaValorMedido > LecturaUmbralMax:
        return "Alerta de humedad excesiva: el umbral máximo de {}%. Se recomienda suspender el riego.".format(LecturaUmbralMax)
    return "La humedad del suelo está dentro de los niveles óptimos."



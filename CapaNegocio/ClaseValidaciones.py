class ClaseValidaciones:
##Validaciones Generales 
    def estaVacioString(stringVerificar) -> bool:
        return stringVerificar != ""
    
    def esNumericoNoVacio(DatosVerificar):
        if DatosVerificar != "" and DatosVerificar.isdigit():
            return int(DatosVerificar) >= 0
        return False
    def esNumericoNoVacioFloat(DatosVerificar):
        try:
            DatosVerificar = float(DatosVerificar)
            if DatosVerificar >= 0:
                return True
        except:
            return False

        
##Validaciones Parcela

    def existeParcelaID(idParcela, listaParcelas) -> bool:
        for parcela in listaParcelas:
            if parcela.idParcela == idParcela:
                return True
        return False
    
##Validaciones Sensor

    def existeSensorID(idSensor, listaSensores) -> bool:
        for sensor in listaSensores:
            if sensor.idSensor == idSensor:
                return True
        return False
    
    def esValidoEstadoSensor(estadoSensor) -> bool:
        estadosValidos = ["activo", "inactivo", "mantenimiento", "revision"]
        return estadoSensor.lower() in estadosValidos
    
    def esValidoTipoSensor(tipoSensor) -> bool:
        tiposValidos = ["humedadsuelo", "temperatura", "lluvia"]
        return tipoSensor in tiposValidos
    
##Validaciones Lectura

    def existeLectura(idLectura, listaLecturas) -> bool:
        for lectura in listaLecturas:
            if lectura.idLectura == idLectura:
                return True
        return False
class ClaseAlerta:
    def __init__(self, idAlerta, idParcela, idSensor, tipo, fechaGeneracion, valorDetectado):
        self.__idAlerta = idAlerta
        self.__idParcela = idParcela
        self.__idSensor = idSensor
        self.__tipo = tipo 
        self.__fechaGeneracion = fechaGeneracion
        self.__valorDetectado = valorDetectado

## Getters and Setters para cada atributo
    @property
    def idAlerta(self):
        return self.__idAlerta
    
    @idAlerta.setter
    def idAlerta(self, nuevoIdAlerta):
        self.__idAlerta = nuevoIdAlerta

    @property
    def idParcela(self):
        return self.__idParcela
    
    @idParcela.setter
    def idParcela(self, nuevoIdParcela):
        self.__idParcela = nuevoIdParcela

    @property
    def idSensor(self):
        return self.__idSensor
    
    @idSensor.setter
    def idSensor(self, nuevoIdSensor):
        self.__idSensor = nuevoIdSensor


    @property
    def tipo(self):
        return self.__tipo 
    
    @tipo.setter
    def tipo(self, nuevoTipo):
        self.__tipo = nuevoTipo

    @property
    def fechaGeneracion(self):
        return self.__fechaGeneracion
    
    @fechaGeneracion.setter
    def fechaGeneracion(self, nuevaFecha):
        self.__fechaGeneracion = nuevaFecha

    @property
    def valorDetectado(self):
        return self.__valorDetectado
    
    @valorDetectado.setter
    def valorDetectado(self, nuevoValor):
        self.__valorDetectado = nuevoValor
    
## string para imprimir la informacion
    def __str__(self):
        return f"Alerta ID: {self.__idAlerta}, Parcela ID: {self.__idParcela}, Sensor ID: {self.__idSensor}, Tipo: {self.__tipo}, Fecha Generacion: {self.__fechaGeneracion}, Valor Detectado: {self.__valorDetectado}"
    
    def transformarDiccionario(self):
        return {
            "idAlerta": self.__idAlerta,
            "idParcela": self.__idParcela,
            "idSensor": self.__idSensor,
            "tipo": self.__tipo,
            "fechaGeneracion": self.__fechaGeneracion,
            "valorDetectado": self.__valorDetectado
        }
    

    def crearDesdeDiccionario(data): 
        return ClaseAlerta(
            data["idAlerta"],
            data["idParcela"],
            data["idSensor"],
            data["tipo"],
            data["fechaGeneracion"],
            data["valorDetectado"]
        )
from enum import Enum

class TipoLugar(Enum):
    AUTO = "Auto"
    MOTO = "Moto"
    CUALQUIERA = "Cualquiera"

# CLASE + ENCAPSULAMIENTO
# ParkingSpot representa un lugar físico del estacionamiento.
# Sus atributos son privados — solo se modifican mediante métodos
# que validan las reglas del negocio.
class LugarEstacionamiento:
    def __init__(self, spot_id: str, tipo_permitido: TipoLugar):
        self.__spot_id = spot_id
        self.__tipo_permitido = tipo_permitido
        self.__ocupado = False
        self.__vehiculo_actual = None

    def get_id(self) -> str:
        return self.__spot_id

    def get_tipo(self) -> TipoLugar:
        return self.__tipo_permitido

    def esta_ocupado(self) -> bool:
        return self.__ocupado

    # ENCAPSULAMIENTO: la validación vive DENTRO del método
    # Nadie puede meter dos vehículos en el mismo lugar
    def es_compatible(self, vehiculo) -> bool:
        from models.vehicle import TipoVehiculo
        if self.__ocupado:
            return False
        if self.__tipo_permitido == TipoLugar.CUALQUIERA:
            return True
        if self.__tipo_permitido == TipoLugar.AUTO:
            return vehiculo.get_tipo() == TipoVehiculo.AUTO
        if self.__tipo_permitido == TipoLugar.MOTO:
            return vehiculo.get_tipo() == TipoVehiculo.MOTO
        return False

    def estacionar(self, vehiculo):
        self.__ocupado = True
        self.__vehiculo_actual = vehiculo

    def liberar(self):
        self.__ocupado = False
        self.__vehiculo_actual = None

    def __repr__(self):
        estado = "ocupado" if self.__ocupado else "libre"
        return f"Lugar({self.__spot_id} | {self.__tipo_permitido.value} | {estado})"
from datetime import datetime
from enum import Enum

class EstadoTicket(Enum):
    ACTIVO = "ACTIVO"
    CERRADO = "CERRADO"

# CLASE + COMPOSICIÓN
# Ticket TIENE un Vehiculo y un LugarEstacionamiento.
# No hereda de ellos — los contiene. Eso es composición.
class Ticket:
    def __init__(self, ticket_id: int, vehiculo, lugar):
        self.__ticket_id = ticket_id
        self.__vehiculo = vehiculo        # composición
        self.__lugar = lugar              # composición
        self.__hora_entrada = datetime.now()
        self.__hora_salida = None
        self.__estado = EstadoTicket.ACTIVO

    def get_id(self) -> int:
        return self.__ticket_id

    def get_vehiculo(self):
        return self.__vehiculo

    def get_lugar(self):
        return self.__lugar

    def get_hora_entrada(self):
        return self.__hora_entrada

    def get_estado(self) -> EstadoTicket:
        return self.__estado

    def get_duracion_horas(self) -> float:
        if self.__hora_salida:
            delta = self.__hora_salida - self.__hora_entrada
        else:
            delta = datetime.now() - self.__hora_entrada
        return round(delta.total_seconds() / 3600, 2)

    # ENCAPSULAMIENTO: cerrar ticket valida que no esté ya cerrado
    def cerrar(self, hora_salida: datetime = None):
        if self.__estado == EstadoTicket.CERRADO:
            raise ValueError("El ticket ya está cerrado.")
        self.__hora_salida = hora_salida or datetime.now()
        self.__estado = EstadoTicket.CERRADO

    def __repr__(self):
        return (f"Ticket(#{self.__ticket_id} | "
                f"{self.__vehiculo.get_placa()} | "
                f"Lugar: {self.__lugar.get_id()} | "
                f"{self.__estado.value})")
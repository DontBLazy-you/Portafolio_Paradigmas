from models.vehicle import Vehiculo
from models.spot import LugarEstacionamiento, TipoLugar
from models.ticket import Ticket, EstadoTicket
from models.rates import PoliticaTarifa, TarifaPorHora
from datetime import datetime

# CLASE PRINCIPAL + COMPOSICIÓN
# ParkingLot TIENE una lista de lugares y tickets.
# También recibe una PoliticaTarifa (inyección de dependencia).
# Centraliza toda la lógica del negocio.
class Estacionamiento:
    def __init__(self, politica: PoliticaTarifa = None):
        # COMPOSICIÓN: el estacionamiento administra sus propios objetos
        self.__lugares = self.__crear_lugares()
        self.__tickets_activos: dict[int, Ticket] = {}
        self.__politica = politica or TarifaPorHora()
        self.__siguiente_id = 1
        self.__total_recaudado = 0.0

    def __crear_lugares(self) -> list:
        lugares = []
        for i in range(1, 6):
            lugares.append(LugarEstacionamiento(f"A{i}", TipoLugar.AUTO))
        for i in range(1, 4):
            lugares.append(LugarEstacionamiento(f"M{i}", TipoLugar.MOTO))
        return lugares

    # ENCAPSULAMIENTO: buscar lugar compatible es interno
    def __buscar_lugar(self, vehiculo) -> LugarEstacionamiento:
        for lugar in self.__lugares:
            if lugar.es_compatible(vehiculo):
                return lugar
        return None

    def registrar_entrada(self, vehiculo: Vehiculo) -> Ticket:
        lugar = self.__buscar_lugar(vehiculo)
        if not lugar:
            raise ValueError("No hay lugares disponibles para este vehículo.")
        lugar.estacionar(vehiculo)
        ticket = Ticket(self.__siguiente_id, vehiculo, lugar)
        self.__tickets_activos[self.__siguiente_id] = ticket
        self.__siguiente_id += 1
        return ticket

    def registrar_salida(self, ticket_id: int) -> dict:
        if ticket_id not in self.__tickets_activos:
            raise ValueError(f"Ticket #{ticket_id} no encontrado o ya fue cerrado.")
        ticket = self.__tickets_activos[ticket_id]
        ticket.cerrar()
        horas = ticket.get_duracion_horas()
        # POLIMORFISMO: no importa qué política sea, se llama igual
        costo = self.__politica.calcular(horas, ticket.get_vehiculo())
        ticket.get_lugar().liberar()
        self.__total_recaudado += costo
        del self.__tickets_activos[ticket_id]
        return {"ticket": ticket, "horas": horas, "costo": costo}

    def get_ocupacion(self) -> dict:
        libres = sum(1 for l in self.__lugares if not l.esta_ocupado())
        ocupados = len(self.__lugares) - libres
        return {"libres": libres, "ocupados": ocupados, "lugares": self.__lugares}

    def get_tickets_activos(self) -> list:
        return list(self.__tickets_activos.values())

    def get_total_recaudado(self) -> float:
        return self.__total_recaudado
from typing import Protocol, runtime_checkable

# ─────────────────────────────────────────────
# 🔷 ABSTRACCIÓN + POLIMORFISMO
# 'PoliticaTarifa' es una INTERFAZ (Protocol).
# Define el CONTRATO: cualquier política de cobro
# DEBE tener un método 'calcular(horas, vehiculo)'.
# El sistema no sabe NI LE IMPORTA qué política
# es — solo llama a 'calcular()' y ya.
# Eso es polimorfismo: mismo método, distinto comportamiento.
# ─────────────────────────────────────────────
@runtime_checkable
class PoliticaTarifa(Protocol):
    def calcular(self, horas: float, vehiculo) -> float:
        ...


# ─────────────────────────────────────────────
# 🔷 POLIMORFISMO en acción
# Dos clases distintas implementan el mismo contrato.
# El estacionamiento puede usar cualquiera de las dos
# sin cambiar su código interno.
# ─────────────────────────────────────────────

class TarifaPorHora:
    """Cobra según las horas y el tipo de vehículo."""
    def __init__(self, tarifa_auto: float = 20.0, tarifa_moto: float = 10.0):
        # 🔷 ENCAPSULAMIENTO: atributos privados con valores por defecto
        self.__tarifa_auto = tarifa_auto
        self.__tarifa_moto = tarifa_moto

    def calcular(self, horas: float, vehiculo) -> float:
        from models.vehicle import TipoVehiculo
        if vehiculo.get_tipo() == TipoVehiculo.AUTO:
            return round(horas * self.__tarifa_auto, 2)
        else:
            return round(horas * self.__tarifa_moto, 2)


class TarifaFija:
    """Cobra una cantidad fija sin importar el tiempo."""
    def __init__(self, monto: float = 50.0):
        self.__monto = monto

    def calcular(self, horas: float, vehiculo) -> float:
        # El vehículo y las horas no importan — siempre es lo mismo
        return self.__monto
from abc import ABC, abstractmethod
from enum import Enum

# Enum para los tipos de vehículo permitidos
class TipoVehiculo(Enum):
    AUTO = "Auto"
    MOTO = "Moto"

# ─────────────────────────────────────────────
# ABSTRACCIÓN + CLASE BASE (HERENCIA)
# ─────────────────────────────────────────────
# 'Vehiculo' es una clase abstracta: define QUÉ
# deben tener todos los vehículos, pero no puede
# usarse directamente. Obliga a crear subclases.
class Vehiculo(ABC):
    def __init__(self, placa: str, tipo: TipoVehiculo):
        # ─────────────────────────────────────
        # ENCAPSULAMIENTO
        # Los atributos con __ son PRIVADOS.
        # Nadie fuera de la clase puede tocarlos
        # directamente. Solo se acceden con métodos.
        # ─────────────────────────────────────
        self.__placa = placa
        self.__tipo = tipo

    def get_placa(self) -> str:
        return self.__placa

    def get_tipo(self) -> TipoVehiculo:
        return self.__tipo

    def __repr__(self):
        return f"{self.__tipo.value}({self.__placa})"

# ─────────────────────────────────────────────
# HERENCIA + POLIMORFISMO (base)
# 'Auto' y 'Moto' HEREDAN de 'Vehiculo'.
# Son subtipos: tienen todo lo de Vehiculo
# pero cada uno representa un tipo distinto.
# Esto permite tratarlos igual en el sistema
# (polimorfismo) aunque sean clases distintas.
# ─────────────────────────────────────────────
class Auto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.AUTO)

class Moto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.MOTO)
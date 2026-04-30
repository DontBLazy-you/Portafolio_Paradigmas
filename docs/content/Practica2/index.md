+++
date = '2026-04-19T23:27:26-08:00'
draft = false
title = 'Practica 2: Simulador de estacionamiento'
tags = []
+++

## 1. Introducción

El presente reporte documenta el desarrollo de un Simulador de Estacionamiento implementado en Python aplicando el paradigma de Programación Orientada a Objetos (POO). El sistema permite registrar la entrada y salida de vehículos, calcular cobros según el tipo de vehículo y el tiempo de estancia, y mostrar el estado de ocupación del estacionamiento.

El proyecto se desarrolló en tres sesiones:

- **Sesión 1:** Modelo orientado a objetos y menú en consola.
- **Sesión 2:** Polimorfismo y subtipos de vehículos y tarifas.
- **Sesión 3:** Interfaz web con Flask bajo el patrón MVC.

---

## 2. Modelo del Dominio

### 2.1 Diagrama UML de Clases

```
┌─────────────────┐         ┌──────────────────────┐
│   <<abstract>>  │         │  <<Protocol>>         │
│    Vehiculo     │         │   PoliticaTarifa      │
│─────────────────│         │──────────────────────│
│ -__placa: str   │         │ +calcular(horas,      │
│ -__tipo: Tipo   │         │   vehiculo): float    │
│─────────────────│         └──────────┬───────────┘
│ +get_placa()    │                    │
│ +get_tipo()     │         ┌──────────┴───────────┐
└────────┬────────┘    ┌────┴──────────┐  ┌────────┴──────────┐
         │             │ TarifaPorHora │  │   TarifaFija      │
    ┌────┴────┐        │───────────────│  │───────────────────│
    │         │        │-__tarifa_auto │  │ -__monto: float   │
  ┌─┴──┐  ┌──┴─┐      │-__tarifa_moto │  │ +calcular()       │
  │Auto│  │Moto│       │ +calcular()   │  └───────────────────┘
  └────┘  └────┘       └───────────────┘

┌──────────────────────────────────────────┐
│              Estacionamiento             │
│──────────────────────────────────────────│
│ -__lugares: list[LugarEstacionamiento]   │
│ -__tickets_activos: dict[int, Ticket]    │
│ -__politica: PoliticaTarifa              │
│ -__total_recaudado: float                │
│──────────────────────────────────────────│
│ +registrar_entrada(vehiculo): Ticket     │
│ +registrar_salida(ticket_id): dict       │
│ +get_ocupacion(): dict                   │
│ +get_tickets_activos(): list             │
└──────────────────────────────────────────┘
         │ composición              │ composición
         ▼                         ▼
┌─────────────────────┐   ┌──────────────────────┐
│ LugarEstacionamiento│   │       Ticket          │
│─────────────────────│   │──────────────────────│
│ -__spot_id: str     │   │ -__ticket_id: int     │
│ -__tipo: TipoLugar  │   │ -__vehiculo: Vehiculo │
│ -__ocupado: bool    │   │ -__lugar: Lugar       │
│─────────────────────│   │ -__hora_entrada       │
│ +es_compatible()    │   │ -__estado             │
│ +estacionar()       │   │──────────────────────│
│ +liberar()          │   │ +cerrar()             │
└─────────────────────┘   │ +get_duracion_horas() │
                          └──────────────────────┘
```

### 2.2 Clases y Responsabilidades

| Clase | Responsabilidad |
|---|---|
| `Vehiculo` | Clase abstracta base para todos los vehículos |
| `Auto` | Subtipo de Vehiculo, representa un automóvil |
| `Moto` | Subtipo de Vehiculo, representa una motocicleta |
| `LugarEstacionamiento` | Representa un lugar físico, controla disponibilidad |
| `Ticket` | Registra la estancia de un vehículo (entrada/salida) |
| `Estacionamiento` | Orquesta toda la lógica del negocio |
| `PoliticaTarifa` | Interfaz común para calcular cobros |
| `TarifaPorHora` | Implementación: cobra por hora según tipo de vehículo |
| `TarifaFija` | Implementación: cobra un monto fijo sin importar el tiempo |

---

## 3. Conceptos de Programación Orientada a Objetos

### 3.1 Clase y Objeto

Una **clase** es una plantilla o molde que define atributos (datos) y métodos (comportamiento). Un **objeto** es una instancia concreta de esa clase.

En el sistema, `Auto` y `Moto` son clases. Al registrar un vehículo se crea un objeto:

```python
# Clase: Auto
class Auto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.AUTO)

# Objeto: instancia de Auto
vehiculo = Auto("ABC-123")
```

Cada vez que un vehículo entra al estacionamiento, se crea un objeto `Auto` o `Moto` y un objeto `Ticket` que representa esa estancia.

---

### 3.2 Encapsulamiento

El **encapsulamiento** consiste en ocultar los datos internos de un objeto y exponer solo lo necesario mediante métodos. Protege el estado interno de modificaciones no autorizadas.

En el sistema, todos los atributos son privados (doble guion bajo `__`) y solo se acceden mediante métodos:

```python
class Vehiculo(ABC):
    def __init__(self, placa: str, tipo: TipoVehiculo):
        self.__placa = placa   # privado — nadie puede modificarlo directamente
        self.__tipo = tipo     # privado

    def get_placa(self) -> str:
        return self.__placa    # solo se accede mediante este método
```

También las validaciones de negocio viven dentro de los métodos, protegiendo las invariantes del sistema:

```python
# En LugarEstacionamiento — nadie puede meter dos vehículos en el mismo lugar
def es_compatible(self, vehiculo) -> bool:
    if self.__ocupado:         # si ya está ocupado, rechaza inmediatamente
        return False
    ...
```

---

### 3.3 Abstracción

La **abstracción** consiste en mostrar solo lo esencial, ocultando los detalles internos. Se implementa mediante clases abstractas e interfaces.

En el sistema hay dos niveles de abstracción:

**Clase abstracta `Vehiculo`** — No puede instanciarse directamente. Define qué tienen todos los vehículos sin importar el tipo:

```python
from abc import ABC

class Vehiculo(ABC):
    def __init__(self, placa: str, tipo: TipoVehiculo):
        self.__placa = placa
        self.__tipo = tipo

    def get_placa(self) -> str:
        return self.__placa
```

**Interfaz `PoliticaTarifa`** — Define el contrato de cobro. El estacionamiento no sabe cómo se calcula, solo sabe que puede llamar a `calcular()`:

```python
class PoliticaTarifa(Protocol):
    def calcular(self, horas: float, vehiculo) -> float:
        ...
```

---

### 3.4 Herencia

La **herencia** permite que una clase hija reutilice atributos y métodos de una clase padre, especializando su comportamiento.

`Auto` y `Moto` heredan de `Vehiculo`. No repiten código — solo indican su tipo:

```python
class Auto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.AUTO)  # llama al padre

class Moto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.MOTO)  # llama al padre
```

Ventaja: si mañana se agrega un atributo a `Vehiculo` (por ejemplo, color), automáticamente lo heredan `Auto` y `Moto` sin modificar esas clases.

---

### 3.5 Polimorfismo

El **polimorfismo** permite que objetos de distintas clases respondan al mismo mensaje (método) de forma diferente. El código que los usa no necesita saber qué tipo específico es.

**Polimorfismo por tarifa:** `TarifaPorHora` y `TarifaFija` tienen el mismo método `calcular()` pero comportamiento distinto. El estacionamiento llama a `calcular()` sin saber cuál es:

```python
# En Estacionamiento — polimorfismo en acción
costo = self.__politica.calcular(horas, ticket.get_vehiculo())
# Si __politica es TarifaPorHora: cobra $20/hr para Auto, $10/hr para Moto
# Si __politica es TarifaFija: cobra siempre $50
# El código es IDÉNTICO en ambos casos
```

**Polimorfismo por subtipo:** el sistema trata a `Auto` y `Moto` como `Vehiculo`. La compatibilidad con el lugar cambia según el tipo real:

```python
# TarifaPorHora — comportamiento distinto según el subtipo
def calcular(self, horas: float, vehiculo) -> float:
    if vehiculo.get_tipo() == TipoVehiculo.AUTO:
        return round(horas * self.__tarifa_auto, 2)   # $20/hr
    else:
        return round(horas * self.__tarifa_moto, 2)   # $10/hr
```

---

## 4. MVC con Flask

El patrón **Modelo-Vista-Controlador** separa las responsabilidades del sistema en tres capas:

| Capa | Archivo(s) | Responsabilidad |
|---|---|---|
| **Modelo** | `models/` | Lógica del negocio: vehículos, lugares, tickets, tarifas |
| **Vista** | `templates/` | Presentación HTML que el usuario ve en el navegador |
| **Controlador** | `app.py` | Rutas Flask: recibe peticiones, llama al modelo, responde con la vista |

### Rutas implementadas

```python
GET  /          → dashboard()     # muestra ocupación y tickets activos
GET  /entrada   → entrada_get()   # muestra formulario de entrada
POST /entrada   → entrada_post()  # procesa la entrada del vehículo
GET  /salida    → salida_get()    # muestra formulario de salida
POST /salida    → salida_post()   # procesa la salida y calcula cobro
```

### Ejemplo de ruta (Controlador llamando al Modelo)

```python
@app.route("/entrada", methods=["POST"])
def entrada_post():
    placa = request.form.get("placa", "").strip().upper()
    tipo  = request.form.get("tipo", "")
    # Controlador crea objeto del Modelo
    vehiculo = Auto(placa) if tipo == "Auto" else Moto(placa)
    # Controlador llama al Modelo
    ticket = estacionamiento.registrar_entrada(vehiculo)
    # Controlador redirige a la Vista
    return redirect(url_for("dashboard"))
```

---

## 5. Pruebas Manuales

### Flujo 1 — Entrada y salida de un Auto

1. Se accede a `/entrada` y se registra placa `ABC-123`, tipo Auto.
2. El sistema asigna el lugar `A1` y crea el Ticket `#1`.
3. En el dashboard se ve `1 ocupado`, `7 libres`, Ticket `#1` activo.
4. Se accede a `/salida`, se selecciona Ticket `#1`.
5. El sistema calcula el costo ($20/hr) y libera el lugar `A1`.
6. El dashboard muestra `8 libres`, `0 ocupados`, total recaudado actualizado.

### Flujo 2 — Entrada y salida de Auto y Moto (polimorfismo visible)

1. Se registra Auto `ABC-123` → Ticket `#1`, lugar `A1`.
2. Se registra Moto `XYZ-777` → Ticket `#2`, lugar `M1`.
3. Se registra salida de Ticket `#1` (Auto) → costo por hora con tarifa de Auto.
4. Se registra salida de Ticket `#2` (Moto) → costo por hora con tarifa de Moto (menor).
5. Se confirma que el cobro fue distinto para cada tipo — polimorfismo funcionando.

---

## 6. Conclusiones

La Programación Orientada a Objetos resulto muy conveniente a la hora de de modelar el sistema de estacionamiento. Cada entidad del mundo real (vehículo, lugar, ticket) se convirtio en una clase, lo que hizo todo mucho mas sencillo y a el código más legible y mantenible.

El **encapsulamiento** garantizó que las reglas del negocio (un lugar = un vehículo) nunca pudieran violarse desde fuera del objeto. La **abstracción** permitió separar la política de cobro del resto del sistema, de modo que cambiar las tarifas no requiere tocar la lógica principal. La **herencia** evitó duplicar código entre `Auto` y `Moto`. El **polimorfismo** permitió que el estacionamiento calculara cobros distintos para diferentes tipos de vehículos y tarifas con el mismo método, sin condiciones adicionales en el controlador.

Al final el lograr que todo se juntara bajo el modelo MVC lo hizo todo mas accecible en el ascpecto de que es facil entenderlo todo separando sus partes, el modelo no sabe nada de HTTP, la vista no sabe nada de lógica, y el controlador solo conecta ambos. Esta arquitectura facilita escalar el sistema en el futuro.

---

## 7. Referencias

- Pallets Projects. (2026). *Welcome to Flask — Flask Documentation (3.1.x)*. https://flask.palletsprojects.com/
- Python Software Foundation. (2026). *dataclasses — Data Classes*. https://docs.python.org/3/library/dataclasses.html
- Fowler, M. (2004). *Inversion of Control Containers and the Dependency Injection pattern*. https://martinfowler.com/articles/injection.html
- Python Typing Team. (2026). *Protocols — typing specification*. https://typing.python.org/en/latest/spec/protocol.html

## 8. Portafolio y Página estatica

[Portafolio Paradigmas de la Programación](https://github.com/DontBLazy-you/Portafolio_Paradigmas)

[Página Estatica](https://dontblazy-you.github.io/Portafolio_Paradigmas/)

from models.vehicle import Auto, Moto
from models.parking_lot import Estacionamiento
from models.rates import TarifaPorHora, TarifaFija

def menu():
    print("\n=== Selecciona política de cobro ===")
    print("1. Por hora (Auto: $20/hr | Moto: $10/hr)")
    print("2. Tarifa fija ($50)")
    opcion = input("Opción: ").strip()
    if opcion == "2":
        estacionamiento = Estacionamiento(TarifaFija())
    else:
        estacionamiento = Estacionamiento(TarifaPorHora())

    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Ver ocupación")
        print("4. Ver tickets activos")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            placa = input("Placa del vehículo: ").strip().upper()
            print("Tipo: 1) Auto  2) Moto")
            tipo = input("Tipo: ").strip()
            try:
                vehiculo = Auto(placa) if tipo == "1" else Moto(placa)
                ticket = estacionamiento.registrar_entrada(vehiculo)
                print(f"\nEntrada registrada: {ticket}")
            except ValueError as e:
                print(f"\nError: {e}")

        elif opcion == "2":
            try:
                ticket_id = int(input("Número de ticket: ").strip())
                resultado = estacionamiento.registrar_salida(ticket_id)
                print(f"\n Salida registrada:")
                print(f"   Ticket: {resultado['ticket']}")
                print(f"   Horas: {resultado['horas']}")
                print(f"   Costo: ${resultado['costo']}")
            except ValueError as e:
                print(f"\nError: {e}")

        elif opcion == "3":
            ocupacion = estacionamiento.get_ocupacion()
            print(f"\nOcupación: {ocupacion['libres']} libres | {ocupacion['ocupados']} ocupados")
            for lugar in ocupacion["lugares"]:
                print(f"   {lugar}")

        elif opcion == "4":
            tickets = estacionamiento.get_tickets_activos()
            if tickets:
                for t in tickets:
                    print(f"   {t}")
            else:
                print("\nNo hay tickets activos.")

        elif opcion == "5":
            print(f"\nTotal recaudado: ${estacionamiento.get_total_recaudado()}")
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
from flask import Flask, render_template, request, redirect, url_for, flash
from models.vehicle import Auto, Moto
from models.parking_lot import Estacionamiento
from models.rates import TarifaPorHora, TarifaFija

app = Flask(__name__)
app.secret_key = "estacionamiento123"

# OBJETO GLOBAL — instancia del estacionamiento
# Este es el modelo en el patrón MVC
estacionamiento = Estacionamiento(TarifaPorHora())

# ─────────────────────────────────────────────
# CONTROLLER (rutas Flask)
# Las rutas son el controlador: reciben peticiones,
# llaman al modelo y mandan datos a la vista (HTML)
# ─────────────────────────────────────────────

@app.route("/")
def dashboard():
    ocupacion = estacionamiento.get_ocupacion()
    tickets = estacionamiento.get_tickets_activos()
    total = estacionamiento.get_total_recaudado()
    return render_template("dashboard.html",
                           ocupacion=ocupacion,
                           tickets=tickets,
                           total=total)

@app.route("/entrada", methods=["GET"])
def entrada_get():
    return render_template("entry.html")

@app.route("/entrada", methods=["POST"])
def entrada_post():
    placa = request.form.get("placa", "").strip().upper()
    tipo = request.form.get("tipo", "")
    if not placa or tipo not in ("Auto", "Moto"):
        flash("Datos inválidos. Verifica placa y tipo.", "error")
        return redirect(url_for("entrada_get"))
    try:
        vehiculo = Auto(placa) if tipo == "Auto" else Moto(placa)
        ticket = estacionamiento.registrar_entrada(vehiculo)
        flash(f"Entrada registrada: Ticket #{ticket.get_id()} — Lugar {ticket.get_lugar().get_id()}", "success")
    except ValueError as e:
        flash(f"{e}", "error")
    return redirect(url_for("dashboard"))

@app.route("/salida", methods=["GET"])
def salida_get():
    tickets = estacionamiento.get_tickets_activos()
    return render_template("exit.html", tickets=tickets)

@app.route("/salida", methods=["POST"])
def salida_post():
    try:
        ticket_id = int(request.form.get("ticket_id", ""))
        resultado = estacionamiento.registrar_salida(ticket_id)
        flash(f"Salida: Ticket #{resultado['ticket'].get_id()} — "
              f"Horas: {resultado['horas']} — Costo: ${resultado['costo']}", "success")
    except ValueError as e:
        flash(f"{e}", "error")
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
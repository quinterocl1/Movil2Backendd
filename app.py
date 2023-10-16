from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
from api.aerolinea import Aerolinea, ruta_aerolinea
from api.avion import Avion, ruta_avion
from api.aeropuerto import Aeropuerto, ruta_aeropuerto
from api.vuelo import Vuelo, ruta_vuelo

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_aerolinea, url_prefix = '/api')
app.register_blueprint(ruta_avion, url_prefix = '/api')
app.register_blueprint(ruta_aeropuerto, url_prefix = '/api')
app.register_blueprint(ruta_vuelo, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['GET'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente, Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id
        }
    return datos

@app.route('/avionaerolinea', methods=['GET'])
def avionaerolinea():
    datos = {}
    resultado = db.session.query(Aerolinea, Avion).select_from(Aerolinea).join(Avion).all()
    i=0
    for aerolinea, avion in resultado:
        i+=1
        datos[i]={
            'aerolinea':aerolinea.nombre,
            'avion':avion.id
        }
    return datos

@app.route('/vueloreserva', methods=['GET'])
def vueloreserva():
    datos = {}
    resultado = db.session.query( Reserva, Vuelo).select_from(Reserva).join(Vuelo).all()
    i=0
    for reserva, vuelo in resultado:
        i+=1
        datos[i]={
            'reserva':reserva.asiento,
            'vuelo':vuelo.id
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
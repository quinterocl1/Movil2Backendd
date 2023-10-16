from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vuelo import Vuelo, VueloSchema

ruta_vuelo = Blueprint("ruta_vuelo", __name__)

vuelo_schema = VueloSchema()
vuelos_schema = VueloSchema(many=True)

@ruta_vuelo.route('/vuelo', methods=['GET'])
def vuelo():
    resultall = Vuelo.query.all() #Select * from Vuelo
    resultado_vuelo= vuelos_schema.dump(resultall)
    return jsonify(resultado_vuelo)

@ruta_vuelo.route('/savevuelo', methods=['POST'])
def save():
    idreserva = request.json['idreserva']
    idavion = request.json['idavion']
    origen = request.json['origen']
    destino = request.json['destino']
    new_vuelo = Vuelo(idreserva, idavion, origen, destino)
    db.session.add(new_vuelo)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_vuelo.route('/updatevuelo', methods=['PUT'])
def Update():
    id = request.json['id']
    idreserva = request.json['idreserva']
    idavion = request.json['idavion']
    origen = request.json['origen']
    destino = request.json['destino']
    vuelo = Vuelo.query.get(id)   
    if vuelo :
        print(vuelo) 
        vuelo.idreserva = idreserva
        vuelo.idavion = idavion
        vuelo.origen = origen
        vuelo.destino = destino
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_vuelo.route('/deletevuelo/<id>', methods=['DELETE'])
def eliminar(id):
    vuelo = Vuelo.query.get(id)
    db.session.delete(vuelo)
    db.session.commit()
    return jsonify(vuelo_schema.dump(vuelo))
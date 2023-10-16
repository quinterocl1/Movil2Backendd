from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionesSchema

ruta_avion = Blueprint("ruta_avion", __name__)

avion_schema = AvionesSchema()
aviones_schema = AvionesSchema(many=True)

@ruta_avion.route('/avion', methods=['GET'])
def avion():
    resultall = Avion.query.all() #Select * from Aviones
    resultado_avion= aviones_schema.dump(resultall)
    return jsonify(resultado_avion)

@ruta_avion.route('/saveavion', methods=['POST'])
def save():
    idaerolinea =request.json['idaerolinea']
    modelo = request.json['modelo']
    new_avion = Avion(idaerolinea, modelo)
    db.session.add(new_avion)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_avion.route('/updateavion', methods=['PUT'])
def Update():
    id = request.json['id']
    idaerolinea = request.json['idaerolinea']
    modelo = request.json['modelo']
    avion = Avion.query.get(id)   
    if avion :
        print(avion) 
        avion.idaerolinea = idaerolinea
        avion.modelo = modelo
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_avion.route('/deleteavion/<id>', methods=['DELETE'])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(avion_schema.dump(avion))
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aerolinea import Aerolinea, AerolineasSchema

ruta_aerolinea = Blueprint("ruta_aerolinea", __name__)

aerolinea_schema = AerolineasSchema()
aerolineas_schema = AerolineasSchema(many=True)

@ruta_aerolinea.route('/aerolinea', methods=['GET'])
def aerolinea():
    resultall = Aerolinea.query.all() #Select * from Aerolinea
    resultado_aerolinea= aerolineas_schema.dump(resultall)
    return jsonify(resultado_aerolinea)

@ruta_aerolinea.route('/saveaerolinea', methods=['POST'])
def save():
    nombre = request.json['nombre']
    new_aerolinea = Aerolinea(nombre)
    db.session.add(new_aerolinea)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_aerolinea.route('/updateaerolinea', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    aerolinea = Aerolinea.query.get(id)   
    if aerolinea :
        print(aerolinea) 
        aerolinea.nombre = nombre
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_aerolinea.route('/deleteaerolinea/<id>', methods=['DELETE'])
def eliminar(id):
    aerolinea = Aerolinea.query.get(id)
    db.session.delete(aerolinea)
    db.session.commit()
    return jsonify(aerolinea_schema.dump(aerolinea))
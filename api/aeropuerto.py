from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aeropuerto import Aeropuerto, AeropuertoSchema

ruta_aeropuerto = Blueprint("ruta_aeropuerto", __name__)

aeropuerto_schema = AeropuertoSchema()
aeropuertos_schema = AeropuertoSchema(many=True)

@ruta_aeropuerto.route('/aeropuerto', methods=['GET'])
def aeropuerto():
    resultall = Aeropuerto.query.all() #Select * from Aeropuerto
    resultado_aeropuerto= aeropuertos_schema.dump(resultall)
    return jsonify(resultado_aeropuerto)

@ruta_aeropuerto.route('/saveaeropuerto', methods=['POST'])
def save():
    nombre = request.json['nombre']
    ciudad = request.json['ciudad']
    pais = request.json['pais']
    new_aeropuerto = Aeropuerto(nombre, ciudad, pais)
    db.session.add(new_aeropuerto)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_aeropuerto.route("/updateaeropuerto", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre"]
    ciudad = request.json["ciudad"]
    pais = request.json["pais"]
    aeropuerto = Aeropuerto.query.get(id)   
    if aeropuerto :
        print(aeropuerto) 
        aeropuerto.nombre = nombre
        aeropuerto.ciudad = ciudad
        aeropuerto.pais = pais
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        print("PRUEBA DE DEBUG")   
        return "Error"

@ruta_aeropuerto.route('/deleteaeropuerto/<id>', methods=['DELETE'])
def eliminar(id):
    aeropuerto = Aeropuerto.query.get(id)
    db.session.delete(aeropuerto)
    db.session.commit()
    return jsonify(aeropuerto_schema.dump(aeropuerto))
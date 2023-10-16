
from config.db import  db, ma, app

class Cliente(db.Model):
    __tablename__ = "tblcliente"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.Integer)

    def __init__(self, nombre, correo, telefono) :
       self.nombre = nombre
       self.correo = correo
       self.telefono = telefono

with app.app_context():
    db.create_all()

class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'correo', 'telefono')

from config.db import  db, ma, app

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuerto"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    ciudad = db.Column(db.String(50))
    pais = db.Column(db.String(50))

    def __init__(self, nombre, ciudad, pais) :
       self.nombre = nombre
       self.ciudad = ciudad
       self.pais = pais

with app.app_context():
    db.create_all()

class AeropuertoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','ciudad','pais')
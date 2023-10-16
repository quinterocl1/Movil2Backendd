from config.db import  db, ma, app

class Vuelo(db.Model):
    __tablename__ = "tblvuelo"

    id = db.Column(db.Integer, primary_key =True)
    idreserva = db.Column(db.Integer, db.ForeignKey('tblreserva.id'))
    idavion = db.Column(db.Integer, db.ForeignKey('tblavion.id'))
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))

    def __init__(self, idreserva, idavion, origen, destino) :
       self.idreserva = idreserva
       self.idavion = idavion
       self.origen = origen
       self.destino = destino

with app.app_context():
    db.create_all()

class VueloSchema(ma.Schema):
    class Meta:
        fields = ('id','idreserva','idreserva','origen','destino')

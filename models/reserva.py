from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    fecha = db.Column(db.String(10))
    asiento = db.Column(db.String(5))

    def __init__(self, idcliente, fecha, asiento) :
       self.idcliente = idcliente
       self.fecha = fecha
       self.asiento = asiento

with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idcliente','fecha','asiento')

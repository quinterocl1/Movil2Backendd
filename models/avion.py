from config.db import  db, ma, app

class Avion(db.Model):
    __tablename__ = "tblavion"

    id = db.Column(db.Integer, primary_key =True)
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))
    modelo = db.Column(db.String(50))

    def __init__(self, idaerolinea, modelo) :
       self.idaerolinea = idaerolinea
       self.modelo = modelo

with app.app_context():
    db.create_all()

class AvionesSchema(ma.Schema):
    class Meta:
        fields = ('id','idaerolinea','modelo')
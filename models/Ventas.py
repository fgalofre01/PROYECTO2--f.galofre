import datetime
from utils.db import db

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    producto = db.relationship('Producto', backref=db.backref('ventas', lazy=True))

    def __init__(self,producto_id, cantidad, fecha):
        self._producto_id = producto_id
        self._cantidad = cantidad
        self._fecha = fecha
from utils.db import db

class Producto(db.Model):
         
        __tablename__ = 'productos'
        
        id = db.Column(db.Integer, primary_key = True)
        nombre = db.Column(db.String(100), nullable = False, unique = True)
        precio_publico = db.Column(db.Float, nullable = False)
        rentabilidad = db.Column(db.Float, nullable = False)
        tipo_vaso = db.Column(db.String(100))
        volumen = db.Column(db.Float)
        ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'),nullable = True)
        ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = True)
        ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable = True)
        ventas_totales = db.Column(db.Integer, default=0)

        ingrediente1 = db.relationship('Ingrediente', foreign_keys=[ingrediente1_id])
        ingrediente2 = db.relationship('Ingrediente', foreign_keys=[ingrediente2_id])
        ingrediente3 = db.relationship('Ingrediente', foreign_keys=[ingrediente3_id])
        
        def __init__(self, nombre: str, precio_publico: float, rentabilidad: float, tipo_vaso: str, volumen: float, ingrediente1_id: int, ingrediente2_id: int, ingrediente3_id: int ):
            self._nombre = nombre
            self._precio_publico = precio_publico
            self._rentabilidad = rentabilidad
            self._tipo_vaso = tipo_vaso
            self._volumen= volumen
            self._ingrediente1_id = ingrediente1_id
            self._ingrediente2_id = ingrediente2_id
            self._ingrediente3_id = ingrediente3_id
   

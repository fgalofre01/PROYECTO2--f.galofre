from db import db


class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)
    calorias = db.Column(db.Float)
    inventario = db.Column(db.Integer)
    es_vegetariano = db.Column(db.Boolean)
    sabor = db.Column(db.String(100)) 
    
    def __init__(self, nombre: str, precio: float, calorias: float, inventario: int, es_vegetariano: bool, sabor: str):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
        self._sabor = sabor

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

    def __init__(self, nombre: str, precio_publico: float, rentabilidad: float, tipo_vaso: str, volumen: float, ingredientes= [] ):
            self._nombre = nombre
            self._precio_publico = precio_publico
            self._rentabilidad = rentabilidad
            self._tipo_vaso = tipo_vaso
            self._volumen= volumen
            self._ingredientes = ingredientes
        
    def es_sano(self):
        """
        Un ingrediente es sano si tiene menos de 100 calorías y es vegetariano.
        """
        return self._calorias < 100 or self._es_vegetariano

    def abastecer(self, inventario):
        """
        Abastece el ingrediente sumando la cantidad proporcionada.
        Lanza un ValueError si la cantidad es negativa o no válida.
        """
        if inventario < 0:
            raise ValueError("La cantidad a abastecer no puede ser negativa")
        self._inventario += inventario

    def renovar_inventario(self):
        """
        Renueva el inventario del complemento, restableciendo su cantidad disponible a 0.
        """
        self.cantidad_disponible = 0
    
    def calcular_calorias(self):
        """
        Calcula las calorías totales del producto sumando las calorías de cada ingrediente.
        """
        return sum(ingrediente._calorias for ingrediente in self._ingredientes)
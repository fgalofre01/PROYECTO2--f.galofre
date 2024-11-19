from models.Ingredientes import Ingrediente
from models.Productos import Producto

class Heladeria():
    def __init__(self):
        self.inventario = {}
        self.productos = []
        self.ingredientes = []
    
    def obtener_productos(self):
        return self.productos

    def obtener_ingredientes(self):
        return self.ingredientes
    
    
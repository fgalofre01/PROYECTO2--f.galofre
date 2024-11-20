from models.Ventas import Venta
from utils import db

class Heladeria():
    def __init__(self):
        self.productos = []
        self.ingredientes = []
    
    def obtener_productos(self):
        return self.productos

    def obtener_ingredientes(self):
        return self.ingredientes
    
    def vender(self, producto):
        """
        Vende un producto, verificando si hay suficiente inventario de ingredientes.
        """
        for ingrediente in producto.ingredientes:
            if ingrediente.inventario < 1:
                raise ValueError(ingrediente.nombre)  # Lanzar error si no hay suficiente inventario

        # Reducir el inventario de los ingredientes del producto
        for ingrediente in producto.ingredientes:
            ingrediente.inventario -= 1
        
       # Registrar venta en la tabla Ventas
        nueva_venta = Venta(producto_id=producto.id)
        db.session.add(nueva_venta)
        db.session.commit()

        return "¡Vendido!"

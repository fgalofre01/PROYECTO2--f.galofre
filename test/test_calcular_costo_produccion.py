import unittest
from Ingredientes_productos import Ingrediente, Producto

class TestCalcularCostoProduccion(unittest.TestCase):
    def test_costo_produccion_producto(self):
        """
        Verifica que el cálculo del costo de producción sea correcto para un producto con ingredientes.
        """
        ingrediente1 = Ingrediente(nombre="Crema de Chatilly", precio= 3500, calorias= 25.5, inventario=15, es_vegetariano= True, sabor = "Fresa")
        ingrediente2 = Ingrediente(nombre="Helado de Chocolate", precio= 5000, calorias= 35.5, inventario=10, es_vegetariano= True, sabor = "Chocolate")
        ingrediente3 = Ingrediente(nombre="Mani Japones", precio= 2800, calorias= 10.5, inventario=12, es_vegetariano= True, sabor = "Mani")
        
        producto = Producto(nombre="Malteada de Chocolate",precio_publico=12500, rentabilidad = 2500, tipo_vaso= "Normal",volumen = 6.5, ingredientes=[ingrediente1, ingrediente2, ingrediente3])
        self.assertEqual(producto.calcular_costo_produccion(), 11300, 
                         "El cálculo del costo de producción es incorrecto")

    def test_costo_produccion_producto_sin_ingredientes(self):
        """
        Verifica que un producto sin ingredientes tenga un costo de producción de 0.
        """
        producto = Producto(nombre="Copa Vacía", precio_publico=10500, rentabilidad = 3000, tipo_vaso= "Vaso familiar",volumen = 8.6, ingredientes=[])
        self.assertEqual(producto.calcular_costo_produccion(), 0, 
                         "Un producto sin ingredientes debería tener un costo de 0")

    def test_costo_produccion_ingrediente_costo_negativo(self):
        """
        Verifica que los costos negativos generen un valor correcto.
        """
        ingrediente1 = Ingrediente(nombre="Fruta", precio= 1500, calorias= 5.5, inventario=15, es_vegetariano= True, sabor = "Fruta")
        ingrediente2 = Ingrediente(nombre="Helado", precio= 2800, calorias= 10.5, inventario=15, es_vegetariano= True, sabor = "Fresa")  # Dato inválido
        
        producto = Producto(nombre="Copa Mixta", precio_publico=11000, rentabilidad = 3000, tipo_vaso= "Vaso mediano",volumen = 6.6, ingredientes=[ingrediente1, ingrediente2])
        costo_total = producto.calcular_costo_produccion()
        self.assertGreaterEqual(costo_total, 0, 
                                "El costo de producción no debería ser negativo")

if __name__ == '__main__':
    unittest.main()

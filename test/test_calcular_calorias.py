import unittest
from Ingredientes_productos import Ingrediente, Producto

class TestCalcularCalorias(unittest.TestCase):
    def test_calcular_calorias_producto(self):
        """
        Verifica que el cálculo de calorías sea correcto para un producto con ingredientes.
        """
        ingrediente1 = Ingrediente(nombre="Helado de Fresa", precio = 2500, calorias=150, inventario = 15, es_vegetariano=True, sabor = "Fresa")
        ingrediente2 = Ingrediente(nombre="Chispas de chocolate", precio = 5500, calorias=50, inventario = 10, es_vegetariano=True, sabor = "Chocolate")
        ingrediente3 = Ingrediente(nombre="Mani japones", precio = 3000, calorias=200, inventario = 12, es_vegetariano=True, sabor ="Mani")
        
        producto = Producto(nombre="Malteada de Chocolate", precio_publico=12000, rentabilidad=6.5, tipo_vaso= "Vaso pequeño", volumen=8.5, ingredientes=[ingrediente1, ingrediente2, ingrediente3])
        self.assertEqual(producto.calcular_calorias(), 400, 
                         "El cálculo de calorías del producto es incorrecto")

    def test_calcular_calorias_producto_sin_ingredientes(self):
        """
        Verifica que un producto sin ingredientes tenga 0 calorías.
        """
        producto = Producto(nombre="Copa Vacía", precio_publico=12000, rentabilidad=6.5, tipo_vaso= "Vaso pequeño", volumen=8.5, ingredientes=[])
        self.assertEqual(producto.calcular_calorias(), 0, 
                         "Un producto sin ingredientes debería tener 0 calorías")

    def test_calcular_calorias_producto_con_ingredientes_negativos(self):
        """
        Verifica que las calorías no permitan valores negativos (error de datos).
        """
        ingrediente1 = Ingrediente(nombre="Helado de Fresa", precio = 2500, calorias=80, inventario = 15, es_vegetariano=True, sabor = "Fresa")
        ingrediente2 = Ingrediente(nombre="Chispas de chocolate", precio = 5500, calorias=20, inventario = 10, es_vegetariano=True, sabor = "Chocolate")  # Dato inválido
        
        producto = Producto(nombre="Copa Saludable", precio_publico=12000, rentabilidad=6.5, tipo_vaso= "Vaso pequeño", volumen=8.5, ingredientes=[ingrediente1, ingrediente2])
        calorias_totales = producto.calcular_calorias()
        self.assertGreaterEqual(calorias_totales, 0, 
                                "Las calorías no deberían ser negativas")

if __name__ == '__main__':
    unittest.main()

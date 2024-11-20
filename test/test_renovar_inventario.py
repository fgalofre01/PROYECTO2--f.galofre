import unittest
from Ingredientes_productos import Ingrediente

class TestRenovarInventario(unittest.TestCase):
    def test_renovar_inventario(self):
        """
        Probar si al renovar el inventario, la cantidad disponible se restablece a 0.
        """
        complemento = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 15, es_vegetariano=True, sabor = "Fresa")
        complemento.renovar_inventario()
        self.assertEqual(complemento.cantidad_disponible, 0, 
                         "La cantidad disponible no se renovó correctamente a 0")

    def test_renovar_inventario_sin_cantidad(self):
        """
        Probar si renovar el inventario funciona cuando la cantidad ya está en 0.
        """
        complemento = Ingrediente(nombre="Chispas de chocolate", precio = 2500,calorias=23.5, inventario = 0, es_vegetariano=True, sabor = "Fresa")
        complemento.renovar_inventario()
        self.assertEqual(complemento.cantidad_disponible, 0, 
                         "La cantidad debería seguir siendo 0 después de renovar el inventario")

if __name__ == '__main__':
    unittest.main()

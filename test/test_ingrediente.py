import unittest
from Ingredientes_productos import Ingrediente

class TestIngrediente(unittest.TestCase):
    def test_ingrediente_sano(self):
        """
        Probar si un ingrediente con menos de 100 calorías y vegetariano es sano.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 15, es_vegetariano=True, sabor = "Fresa")
        self.assertTrue(ingrediente.es_sano(), "El ingrediente debería ser sano")
        print(ingrediente.__dict__)

    def test_ingrediente_no_sano_calorias(self):
        """
        Probar si un ingrediente con más de 100 calorías no es sano.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=150, inventario = 15, es_vegetariano=False, sabor = "Fresa")
        self.assertFalse(ingrediente.es_sano(), "El ingrediente no debería ser sano debido a las calorías")
        print(ingrediente.__dict__)

    


if __name__ == '__main__':
    unittest.main()

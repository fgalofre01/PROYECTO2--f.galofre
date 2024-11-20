import unittest
from Ingredientes_productos import Ingrediente


class TestAbastecerIngrediente(unittest.TestCase):
    def test_abastecer_cantidad_valida(self):
        """
        Probar si el abastecimiento con una cantidad válida incrementa correctamente la cantidad disponible.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 10, es_vegetariano=True, sabor = "Fresa")
        ingrediente.abastecer(20)
        self.assertEqual(ingrediente.inventario, 30, "La cantidad disponible no se actualizó correctamente")
        print(ingrediente.__dict__)

    def test_abastecer_cantidad_cero(self):
        """
        Probar si el abastecimiento con 0 no modifica la cantidad disponible.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 15, es_vegetariano=True, sabor = "Fresa")
        ingrediente.abastecer(0)
        self.assertEqual(ingrediente.inventario, 15, "La cantidad no debería cambiar al abastecer con 0")
        print(ingrediente.__dict__)

    def test_abastecer_cantidad_negativa(self):
        """
        Probar si el abastecimiento con una cantidad negativa lanza un ValueError.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 10, es_vegetariano=True, sabor = "Fresa")
        with self.assertRaises(ValueError) as context:
            ingrediente.abastecer(-5)
        self.assertEqual(str(context.exception), "La cantidad a abastecer no puede ser negativa", 
                         "El mensaje de error no es el esperado")
        print(ingrediente.__dict__)

    def test_abastecer_desde_inicial(self):
        """
        Probar si el abastecimiento funciona correctamente con un ingrediente con cantidad inicial 0.
        """
        ingrediente = Ingrediente(nombre="Helado de Fresa", precio = 2500,calorias=23.5, inventario = 0, es_vegetariano=True, sabor = "Fresa")
        ingrediente.abastecer(15)
        self.assertEqual(ingrediente.inventario, 15, "El abastecimiento inicial no es correcto")
        print(ingrediente.__dict__)

if __name__ == '__main__':
    unittest.main()

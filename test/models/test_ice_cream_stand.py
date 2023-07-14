import unittest
from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):

    def setUp(self):
        self.ice_cream_stand = IceCreamStand("Minha Sorveteria", "Sorvete", ["Chocolate Belga", "Leite Ninho", "Nutella"])

    def test_flavors_available(self):
        result = '\nNo momento temos os seguintes sabores de sorvete disponiveis:\n\t- Chocolate Belga\n\t- Leite Ninho\n\t- Nutella'

        ic_stand = IceCreamStand('Minha Sorveteria', 'Sorvete', ['Chocolate Belga', 'Leite Ninho', 'Nutella'])

        found_result = ic_stand.list_available_flavors()
        self.assertEqual(result, found_result)

    def test_find_flavor_existing(self):
        flavor = "Chocolate Belga"
        expected_output = f"Temos no momento o sabor {flavor}!"
        found_output = self.ice_cream_stand.check_flavor_availability(flavor)
        self.assertEqual(expected_output, found_output)

    def test_find_flavor_non_existing(self):
        flavor = "Limão"
        expected_output = f"Não temos no momento o sabor {flavor}!"
        found_output = self.ice_cream_stand.check_flavor_availability(flavor)
        self.assertEqual(expected_output, found_output)

    def test_find_flavor_empty_inventory(self):
        empty_ice_cream_stand = IceCreamStand("Sorveteria Vazia", "Sorvete", [])
        flavor = "Leite Ninho"
        expected_output = "Estamos sem estoque atualmente!"
        found_output = empty_ice_cream_stand.check_flavor_availability(flavor)
        self.assertEqual(expected_output, found_output)

    def test_add_flavor_existing(self):
        flavor = "Chocolate Belga"
        expected_output = "\nSabor já disponível!"
        found_output = self.ice_cream_stand.add_flavor_to_inventory(flavor)
        self.assertEqual(expected_output, found_output)

    def test_add_flavor_non_existing(self):
        flavor = "Morango"
        expected_output = f"{flavor} adicionado ao estoque!"
        found_output = self.ice_cream_stand.add_flavor_to_inventory(flavor)
        self.assertEqual(expected_output, found_output)

    def test_add_flavor_empty_inventory(self):
        empty_ice_cream_stand = IceCreamStand("Sorveteria Vazia", "Sorvete", [])
        flavor = "Nutella"
        expected_output = f"{flavor} adicionado ao estoque!"
        found_output = empty_ice_cream_stand.add_flavor_to_inventory(flavor)
        self.assertEqual(expected_output, found_output)

    def test_str_representation(self):
        expected_output = "Sorveteria: Minha Sorveteria\nCulinária: Sorvete\nSabores Disponíveis: Chocolate Belga, Leite Ninho, Nutella"
        found_output = str(self.ice_cream_stand)
        self.assertEqual(expected_output, found_output)

    def test_flavors_unavailable(self):
        self.ice_cream_stand.flavors = []
        expected_output = "Estamos sem estoque atualmente!"
        found_output = self.ice_cream_stand.list_available_flavors()
        self.assertEqual(expected_output, found_output)

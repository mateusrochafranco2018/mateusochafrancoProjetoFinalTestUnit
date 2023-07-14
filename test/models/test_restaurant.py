import unittest
from src.models.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        restaurant_name = 'Restaurante Maffiosos'
        cuisine_type = 'Paulista'
        number_served = 1000
        is_open = True
        expected_output = f'Esse restaurante é chamado {restaurant_name} e serve {cuisine_type}.\n' \
                          f'Esse restaurante está servindo {number_served} consumidores desde que está aberto.'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.imprima_uma_descricao_do_restaurante()

        self.assertEqual(expected_output, found_output)

    def test_open_restaurant(self):
        restaurant_name = 'Restaurante Francos'
        cuisine_type = 'Mineira'
        number_served = 500
        is_open = False
        expected_output = f'{restaurant_name} agora está aberto!'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.open_restaurant()

        self.assertEqual(expected_output, found_output)

    def test_open_restaurant_validate_change_status(self):
        restaurant_name = 'Restaurante Felix'
        cuisine_type = 'magia'
        number_served = 100
        is_open = False
        expected_result = True

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        restaurant.open_restaurant()
        found_result = restaurant.open

        self.assertEqual(expected_result, found_result)

    def test_open_restaurant_validate_number_served(self):
        restaurant_name = 'Restaurante Geek'
        cuisine_type = 'frutos do mar'
        number_served = 545
        is_open = False
        expected_result = 0

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        restaurant.open_restaurant()
        found_result = restaurant.number_served

        self.assertEqual(expected_result, found_result)

    def test_open_restaurant_is_open(self):
        restaurant_name = 'Restaurante Apple'
        cuisine_type = 'paranaense'
        number_served = 457
        is_open = True
        expected_output = f'{restaurant_name} já está aberto!'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.open_restaurant()

        self.assertEqual(expected_output, found_output)

    def test_close_restaurant(self):
        restaurant_name = 'Felipe Restaurants'
        cuisine_type = 'paulista'
        number_served = 368
        is_open = True
        expected_output = f'{restaurant_name} agora está fechado!'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.close_restaurant()

        self.assertEqual(expected_output, found_output)

    def test_close_restaurant_closed(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 887
        is_open = False
        expected_output = f'{restaurant_name} já está fechado!'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.close_restaurant()

        self.assertEqual(expected_output, found_output)

    def test_close_restaurant_validate_status(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 786
        is_open = True
        expected_result = False

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        restaurant.close_restaurant()

        found_result = restaurant.open

        self.assertEqual(expected_result, found_result)

    def test_set_number_served(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 878
        new_number_served = 1002
        is_open = True
        expected_result = 1002

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        restaurant.set_number_served(new_number_served)

        found_result = restaurant.number_served

        self.assertEqual(expected_result, found_result)

    def test_set_number_served_close_restaurant(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 774
        new_number_served = 1002
        is_open = False
        expected_output = f'{restaurant_name} está fechado! Não é possível atualizar o número de clientes atendidos.'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.set_number_served(new_number_served)

        self.assertEqual(expected_output, found_output)

    def test_increment_number_served(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 1000
        increment = 120
        is_open = True
        expected_result = 1120

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        restaurant.increment_number_served(increment)

        found_result = restaurant.number_served

        self.assertEqual(expected_result, found_result)

    def test_increment_number_served_close_restaurant(self):
        restaurant_name = 'Restaurante Master Cheff'
        cuisine_type = 'diversos'
        number_served = 1000
        increment = 10
        is_open = False
        expected_output = f'{restaurant_name} está fechado!'

        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.number_served = number_served
        restaurant.open = is_open

        found_output = restaurant.increment_number_served(increment)

        self.assertEqual(expected_output, found_output)

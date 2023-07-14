from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Mudei todos os prints para Return"""
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def list_available_flavors(self):
        """Retorna uma string com a lista de sabores disponíveis."""
        if self.flavors:
            mensagem = "\nNo momento temos os seguintes sabores de sorvete disponiveis:"
            for flavor in self.flavors:
                # Concatenando sabores ao msg
                mensagem = f"{mensagem}\n\t- {flavor}"
            return mensagem
        else:
            return "Estamos sem estoque atualmente!"

    def check_flavor_availability(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento o sabor {flavor}!"
            else:
                return f"Não temos no momento o sabor {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor_to_inventory(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if self.flavors:  # Verifica se o estoque não está vazio
            if flavor in self.flavors:  # Verifica se o sabor já está no estoque
                return "\nSabor já disponível!"
            else:
                self.flavors.append(flavor)  # Adiciona o novo sabor ao estoque
                return f"{flavor} adicionado ao estoque!"
        else:
            self.flavors.append(flavor)  # Adiciona o novo sabor ao estoque vazio
            return f"{flavor} adicionado ao estoque!"

    def __str__(self):
        """Retorna uma representação em string da sorveteria."""
        return f"Sorveteria: {self.restaurant_name}\nCulinária: {self.cuisine_type}\nSabores Disponíveis: {', '.join(self.flavors)}"
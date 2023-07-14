class Restaurant:
    """Mudei todos os prints para Return"""
    """Modelo de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def imprima_uma_descricao_do_restaurante(self):
        """Retorna uma descrição simples da instância do restaurante."""
        description = f"Esse restaurante é chamado {self.restaurant_name} e serve {self.cuisine_type}.\n" \
                      f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."
        return description

    def open_restaurant(self):
        """Retorna uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Retorna uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Define o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            return f"{self.restaurant_name} está fechado! Não é possível atualizar o número de clientes atendidos."

    def increment_number_served(self, more_customers):
        """Aumenta o número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers
            return None  # ou pode retornar uma mensagem específica
        else:
            return f"{self.restaurant_name} está fechado!"

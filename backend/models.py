class Product:
    def __init__(self, name, rating, price):
        self.name = name
        self.rating = rating
        self.price = price
        
    def __str__(self):
        return f'{self.name} - Avaliação: {self.rating} - Preço: R$ {self.price}'


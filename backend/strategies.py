from models import Product

class IStrategy:
    def sort(self, products):
        raise NotImplementedError

class ByName(IStrategy):
    def sort(self, products):
        return sorted(products, key=lambda product: product.name.lower())  # Ordena por nome

class ByRating(IStrategy):
    def sort(self, products):
        return sorted(products, key=lambda product: product.rating, reverse=True)  # Ordena por avaliação (maior primeiro)

class ByPrice(IStrategy):
    def sort(self, products):
        return sorted(products, key=lambda product: product.price)  # Ordena por preço

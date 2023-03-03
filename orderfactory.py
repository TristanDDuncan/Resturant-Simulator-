from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:

    @staticmethod
    def create_order(order):
        if order == "pizza":
            return Pizza()
        if order == "pasta":
            return Pasta()
        if order == "salad":
            return Salad()
        

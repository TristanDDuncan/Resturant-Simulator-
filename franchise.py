from logger import Logger
from orderfactory import OrderFactory


class Franchise:
    def __init__(self,location):
        self.order_factory = OrderFactory()
        self.logger = Logger()
        self.location = location
    

    def place_order(self):
        
        dish = input("What food would you be ordering today \n Enter '1' for pizza '2' for pasta '3' for salad ")
        if dish not in ['1','2','3']:
            print("Invalid input. Please enter '1', '2', or '3'.")
            return
        order = self.order_factory.create_order(dish)
        self.logger.log_transaction(order)
        print(f"You ordered {order.dish}.At{self.location} Thank you!")
        
        

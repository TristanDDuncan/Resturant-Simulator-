from order import Order
class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0
    
    def log_transaction(self,order):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"{self.transaction_count}: {order.dish} at {order.location} - {order.price}. Total:{self.daily_sales}\n")
        file.close()

    
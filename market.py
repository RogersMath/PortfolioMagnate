import random

class Market:
    def __init__(self):
        self.stocks = self.generate_stocks()

    def generate_stocks(self):
        stocks = {}
        for i in range(10):
            stock_name = f"Stock{i}"
            stocks[stock_name] = {
                'price': random.uniform(50, 150),
                'beta': random.uniform(0.8, 1.2),
                'volatility': random.uniform(0.1, 0.3)
            }
        return stocks

    def simulate_market_movement(self):
        for stock in self.stocks:
            self.stocks[stock]['price'] *= random.uniform(0.95, 1.05)
        return self.stocks

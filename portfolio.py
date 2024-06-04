class Portfolio:
    def __init__(self):
        self.holdings = {}
        self.cash = 1000

    def buy_stock(self, stock, quantity, price):
        total_cost = quantity * price
        if total_cost > self.cash:
            print("Insufficient funds to buy stock.")
            return
        self.cash -= total_cost
        if stock in self.holdings:
            self.holdings[stock]['quantity'] += quantity
        else:
            self.holdings[stock] = {'quantity': quantity, 'price': price}

    def sell_stock(self, stock, quantity, price):
        if stock not in self.holdings or self.holdings[stock]['quantity'] < quantity:
            print("Insufficient stock to sell.")
            return
        self.cash += quantity * price
        self.holdings[stock]['quantity'] -= quantity
        if self.holdings[stock]['quantity'] == 0:
            del self.holdings[stock]

    def view_portfolio(self):
        return self.holdings

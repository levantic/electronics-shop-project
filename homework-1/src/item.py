class Item:
    all = []
    pay_rate = 0.85
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        Item.all.append(self)

    def apply_discount(self):
        self.price *= self.pay_rate


    def calculate_total_price(self):
        check = self.price * self.amount
        return check


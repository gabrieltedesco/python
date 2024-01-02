import csv
import math

#POO
#create the class and methods
class Item:
    pay_rate = 0.8 #class atributte for pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the receiveed arguments
        assert price >= 0, f'Price {price} is not greater than zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than zero'

        #Assign to sefl object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def total_price(self):
        return print(self.price*self.quantity)
    
    def apply_discount(self):
        self.price *= self.pay_rate

    #creating a class method
    @classmethod
    def instantiate_csv(cls):
        with open('class02.csv', 'r') as file:
            reader = csv.DictReader(file)
            items_reader = list(reader)
        
        for item in items_reader:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    #creating a static method
    @staticmethod
    def is_integer(num):
        if math.floor(num) < num:
            return False
        else: 
            return True

    #control the display of your objects
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


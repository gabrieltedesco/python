from class02_item import Item
from class02_phon import Phone

print(Item.all)
Item.instantiate_csv()
print(Item.all)

phone1 = Phone("red", 500, 10, 1)
print(phone1.total_price())
print(Item.all)

phone1.name = 'yellow'

#POO is based in four principles to desgin large programs
#1 Encapsulation: mechanism of restrcting the direct access to some of our attributes in a program
#2 Abstraction: process of focusing on essential features while ignoring irrelevant details
#3 Inheritance: process by which a new class is created from an existing class
#4 Polymorphism: ability of an object to take on multiple forms


from class02_item import Item
from class02_phone import Phone

print(Item.all)
Item.instantiate_csv()
print(Item.all)

phone1 = Phone("red", 500, 10, 1)
print(phone1.total_price())
print(Item.all)

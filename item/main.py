from item import Item

from phone import Phone


#Item.instantiate_from_csv()

#item1 = Item('myItem', 750)
#item1 = apply_increament(02)
#print(item1.price)

#print(Item.all)
item1 = Phone("iPhone12Pro", 1000, 3)
item1.apply_increament(0.2)

item1.send_email()
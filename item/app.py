import csv

class Item:

	# class attribute
	pay_rate = 0.65 # The pay rate for 20% discount
	all = []

	def __init__(self, name: str, price: float, quantity=0):

		# run validations to the recieved arguments
		assert price >=0, f'Price {price} is not greater  or equal to zero!'
		assert quantity >=0, f' Quantity {quantity} is not greater or equal to zero!'
		#assert broken_phone >=0, f' Broken Phones {broken_phone} is not greater  or equal to zero!'

		# assign to self object

		self.name = name 
		self.price = price
		self.quantity = quantity
		#self.broken_phone = broken_phone

		# actions to exucte
		Item.all.append(self)


	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * Item.pay_rate

	# convert methed to class method
	#classmethod used to manipulate different data structure 
	# to instantiatiate objects, like csv and others.
	# it takes class object but not instance of class
	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			#print(item)
			
			Item(
				name=item.get('name'),
				price=float(item.get('price')),
				quantity=int(item.get('quantity')),
			)
	# anything related to the class
	# something unique per instance
	# does not take self / class instance		
	@staticmethod
	def is_integer(num):
		# we will count out the floats that are point zero.
		if isinstance(num, float):
			# count out the floats that are point zero
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False
			


	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"




Item.instantiate_from_csv()
print(Item.all)

"""
print(Item.is_integer(4.0))
Item.instantiate_from_csv()

print(Item.all)
item1 = Item("iPhone", 800, 3)
item2 = Item("PC", 1500, 2)
item3 = Item("Airpod", 200, 1)
item4 = Item("Watch", 250, 5)
item5 = Item("Ipad", 900, 4)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(Item.__dict__)  # all the attributes of the class level
print(item1.__dict__) # all the attributes of the instance level
item1.apply_discount()
print(item1.price)
item2.apply_discount()
print(item2.price)

for i in Item.all:
	print(i.name)


"""




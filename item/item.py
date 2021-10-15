import csv


class Item:


	# class attribute
	pay_rate = 0.65 # The pay rate for 20% discount
	all = []

	def __init__(self, name: str, price: float, quantity=0):

		# run validations to the recieved arguments
		assert price >=0, f'Price {price} is not greater  or equal to zero!'
		assert quantity >=0, f' Quantity {quantity} is not greater or equal to zero!'
		

		# assign to self object

		self.__name = name 
		self.__price = price
		self.quantity = quantity
		

		# actions to exucte
		Item.all.append(self)

	@property
	def price(self):
		return self.__price


	def calculate_total_price(self):
		return self.__price * self.quantity

	def apply_discount(self):
		self.__price = self.__price * Item.pay_rate

	def apply_increment(self, increment_value):
		self.__price = self.__price + self.__price * increment_value

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
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

	

	def connect(self, smpt_server):
		pass 

	def prepare_body(self):
		return f"""
		 Hello Someone.
		 We have {self.name} {self.quantity} times.
		 Regards, RisasiCodingAcademy
		"""

	def send(self):
		pass 

	def send_email(self):
		self.connect()
		self.prepare_body()
		self.send()

	# Property Decorator = Read Only Attribute
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if len(value) > 10:
			raise Exception("The name is too long!")
		else:
			#print("You are trying to set")
			self.__name = value
	



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




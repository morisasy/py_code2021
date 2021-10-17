from item import Item



class Phone(Item):

	# class attribute
	#pay_rate = 0.65 # The pay rate for 20% discount
	#all = []

	def __init__(self, name: str, price: float, quantity=0, broken_phone =0):
		# call to super function to have access to all attributes / methods
		super().__init__(
			name, price, quantity
		)

		# run validations to the recieved arguments
		assert broken_phone >=0, f' Broken Phones {broken_phone} is not greater  or equal to zero!'

		# assign to self object
		self.broken_phone = broken_phone

		# actions to exucte
		#Phone.all.append(self)




#Item.instantiate_from_csv()
#print(Item.all)
phone1 = Phone("iPhone13ProMax", 500, 5, 1)
print(Item.all)
print(Phone.all)

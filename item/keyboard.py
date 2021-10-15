from item import Item



class Keyboard(Item):

	# class attribute
	#pay_rate = 0.65 # The pay rate for 20% discount
	#all = []

	def __init__(self, name: str, price: float, quantity=0):
		# call to super function to have access to all attributes / methods
		super().__init__(
			name, price, quantity
		)
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
	
		return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'
	


def validate_and_execute():
	try:

		#if user_input.isdigit():
		user_input_number = int(user_input)
		if user_input_number > 0:
			calculate_value = days_to_units(user_input_number)
			print(calculate_value)

		elif num_of_days ==0:
			return print(' you entered a 0, please enter a valid positive number')
		else:
			print(' you entered a naative number, please enter a valid positive number')


	except ValueError:
		print('Your input is not a balid number. Do not ruin my program!')

user_input = ""
	
while user_input != "exit":

	user_input = input("Hey user, enter a number of day and I will convert it to hours!\n")
	validate_and_execute()
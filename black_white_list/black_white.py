
def black_white_list(black_white):
	black_white_list = []

	for item in black_white:
		if item % 2 == 0:
			black_white_list.append('black')
		else:
			black_white_list.append('white')
	print(black_white_list)


list_of_black_and_white = [2,3,5, 8]

black_white_list(list_of_black_and_white)

list_of_black_and_white_short =['black' if item % 2 == 0 else 'white' for item in black_white]
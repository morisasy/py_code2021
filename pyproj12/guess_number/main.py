import random


def guess(x):
	"""
	 Guess a number game. Guess any number between 1 and 10. 
	 The program will quit and display contrats message when you guess a right number
	 otherwise, will prompt to guess the number!
	 this is the simple python game.
	 Enjoy the game and play safe!
	"""
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'guess a number between 1 and {x}: '))
		if guess < random_number:
			print('Sorry, guess agian. Too low.')
		elif guess> random_number:
			print('Sorry, guess agian. Too high.')

	print(f'Yay, Congrats. You have guessed the number: {random_number}')


def computer_guess(x):
	"""
	 In this game. The computer will guess the number.
	 A gamer first has to guess the number and
	 Computer will print the number and will ask if the number is correct or not!
	 The gamer has to reply 
	 low (l) / high (h) for a wrong answer and 
	 Correct (c) for a correct



	"""
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low # could be also be high b/c low = high

		
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1
	print('Yay! the computer guessed your number, {guess}, correctly!')


computer_guess(10)
#guess(10)
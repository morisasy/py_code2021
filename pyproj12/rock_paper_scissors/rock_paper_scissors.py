import random



def play():
	print("What's your choice?")
	user = input(" 'r' for rock, 'p' for paper, 's' for scissors\n ")
	computer = random.choice(['r', 'p', 's'])

	if user == computer:
		return 'It\'s a tie'

	# r > s, s > p, p > r
	if is_win(user, computer):
		return'You won!'


def is_win(player, opponent):
	# return ture if playe wins
	# r > s, s > p, p > r

	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
		or (player == 'p' and opponent == 'r'):
		return True

print(play())

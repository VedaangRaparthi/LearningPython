from random import choice
def play():
	user = input('Rock (r), Paper (p) or Scissors (s)?: ').lower()
	comp = choice(['r', 'p', 's'])
	print(f'Computer: {comp}')
	if user == comp:
		return 'It\'s a tie!'
	if winner(user, comp):
		return 'You won!'
	return 'You lost!'

def winner(user, comp):
	if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or \
	(user == 's' and comp == 'p'):
		return True

while True:
	print(play())
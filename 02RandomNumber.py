import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess > random_number:
			print('Too high. Try again.')
		elif guess < random_number:
			print('Too low. Try again.')
	print(f'Congratulations. You have guessed the number {random_number}')

guess(10)

def compguess(x):
	max = x
	min = 1
	feedback = ''
	while feedback != 'c':
		if max != min:
			guess = random.randint(min, max)
		else: 
			guess = min	
		feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)? ').lower()
		if feedback == 'h':
			max = guess - 1
		elif feedback == 'l':
			min = guess + 1
	print(f'Congratulations. I have guessed the number {guess}')

compguess(10)
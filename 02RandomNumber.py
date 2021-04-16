import random
numrange = input("Enter range over which a random number can be chosen: ")
numrange = numrange.split()
no = random.randint(int(numrange[0]), int(numrange[1]))
while True:
	guess = int(input("Guess the number: "))
	if guess not in range(int(numrange[0]), int(numrange[1])+1):
		print("Number not in range.")
	elif guess == no:
		print("You've guessed the correct number.")
		break
	else:
		print("Wrong number! Try again.")
		continue
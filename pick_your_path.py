"""
Project: Pick Your Path
Author: Rebecca Dang
Project Started: October 15, 2018
Project Completed: --- 

Program Objectives:
1. Give the user scenarios, and have them pick things which leads to other scenarios.
"""

from random import randint
from time import sleep

# Upon startup, welcome player to game
print('Welcome to Pick Your Path!')
sleep(0.5)
print('An interactive game where a combination of wise decision-making and a bit of luck will lead to success.')
sleep(0.5)
print('Mode: Zombie Apocalypse')
sleep(1)

def start_game():
	# Lists of names for random generation of names
	first_names = [
		'Rebecca',
		'Tommy',
		'Edward',
		'Justin',
		'Trinity',
		'Rohan',
		'Ananya',
		'Josephine',
		'Nidhir',
		'Jonathan',
		'Christopher'
	]

	last_names = [
		'Johnson',
		'Williams',
		'Devanath',
		'Chen',
		'Nguyen',
		'Luong',
		'Tran',
		'Guggilla',
		'Robin',
		'Garcia',
		'Ashikaga'
	]

	# Asks user if they want to use their own name or randomly generate one, and does what the users wishes
	while True:
		name_choice = input('Would you like to use your own name? (If not, your name will be randomly generated.) Y / N: ').upper()

		try:
			assert name_choice == 'Y' or name_choice == 'N'
		except AssertionError:
			print('Error, please type in Y or N.')
			print()
		else:
			if name_choice == 'Y':
				while True:
					try:
						name = input('Name (first and last): ')
						assert name.strip()
					# Raises exception if name string is empty or blank
					except AssertionError:
						print('Error, please make sure you have entered a name.')
						print()
					else:
						# Break out of inside while loop
						break
				# Break out of outside while loop
				break
			else:
				# Randomly generates first and last name
				first_name = first_names[randint(0,len(last_names)-1)]
				last_name = last_names[randint(0,len(last_names)-1)]

				# Combines first and last name into name variable
				name = first_name + ' ' + last_name 

				# Break out of outside while loop
				break

	# Prints name
	print('Your name is %s.' % name)
	print()

	sleep(0.5)

	# Asks user if they want to use their own age or randomly generate one, and does what the users wishes
	while True:
		age_choice = input('Would you like to use your own age? (If not, your age will be randomly generated.) Y / N: ').upper()

		try:
			assert age_choice == 'Y' or age_choice == 'N'
		except AssertionError:
			print('Error, please type in Y or N.')
			print()
		else:
			if age_choice == 'Y':
				while True:
					try:
						age = int(input('Age: '))
						assert age >= 20 and age <= 65
					# Raises exception if input entered isn't valid for the int() function
					except ValueError:
						print('Error, please enter an integer.')
						print()
					# Raises exception if age is not between 20 and 65
					except AssertionError:
						print('Error, please enter an age between 20 and 65.')
						print()
					else:
						# Breaks out of inside while loop
						break
				# Breaks out of outside while loop		
				break
			else:
				# Randomly generates age from 20-65 years
				age = randint(20, 66) 
				# Breaks out of outside while loop
				break
	
	# Prints age
	print("Your age is %d." % age)
	print()

	# If age is 20-30 
	if age >= 20 and age <= 30:
		age = 'young' 
		# Success rates 
		phys = 60 			#physical
		reflex = 80 		#reflexes
		intellect = 60 		#intellect
		ppl = 70 			#people skills

	# If age is 31-50
	elif age > 30 and age <= 50:
		age = 'midlife'
		phys = 70
		reflex = 60
		intellect = 70
		ppl = 70

	# If age is 51+
	else:
		age = 'old'
		phys = 40
		reflex = 50
		intellect = 50
		ppl = 70

	sleep(0.5)

	while True:
		occupation = input("""Choose an occupation:
			(1) Physics teacher
			(2) CEO
			(3) Chef
			(4) Police officer
			(5) Sales representative
			(6) Unemployed
Enter an integer from 1-6: """)
		print()

		try:
			assert occupation in '123456'
		except AssertionError:
			print('Sorry, please enter the integer from 1-6 that corresponds to your occupation choice.')
		else:
			if occupation == '1':
				print('You are a physics teacher.')
				phys -= 5
				reflex += 0
				intellect += 20
				ppl += 5
				occupation = 'physics teacher'
			elif occupation == '2':
				print('You are a CEO.')
				phys -= 5
				reflex += 0
				intellect += 10
				ppl += 10
				occupation = 'CEO'
			elif occupation == '3':
				print('You are a chef.')
				phys += 5
				reflex += 0
				intellect += 5
				ppl += 0
				occupation = 'chef'
			elif occupation == '4':
				print('You are a police officer.')
				phys += 20
				reflex += 10
				intellect += 5
				ppl -= 10
				occupation = 'police officer'
			elif occupation == '5':
				print('You are a sales representative.')
				phys += 0
				reflex += 0
				intellect += 5
				ppl += 20
				occupation = 'sales representative'
			elif occupation == '6':
				print('You are unemployed.')
				phys -= 10
				reflex += 0
				intellect -= 10
				ppl += 0
				occupation = 'unemployed'
			break
		finally:
			print()
			
	sleep(1)

	status = 4 # healthy (neutral)
	print('The game is now beginning. Good luck!')
	print()

	# game(name, age, occupation, phys, reflex, intellect, ppl, status)


def game(name, age, occupation, phys, reflex, intellect, ppl, status):
	playing_game = True

	sit = 1

	while playing_game == True:
		if sit == 1:
			print("""It's the weekend, and you're currently sitting at home. You've decided to binge watch Marvel's Agents of S.H.I.E.L.D., which your friend Brenda recommended to you, when suddenly you start to hear some sort of banging noise on your front door. Looking through the peephole, you see a horde of zombies trying to break through.

What do you do?
	(1) Grab your emergency supplies backpack and exit through the backyard
	(2) Grab your family's shotgun and a kitchen knife and try to mow down the zombies
""")
			print()
			make_choice = True
			while make_choice == True:
				choice = int(input("Enter 1 or 2: "))
				chance = randint(1, 100)
				if choice == 1:
					if phys >= chance:
						sit = 1.1 # change
					else:
						sit = 1.2 # change
					make_choice = False
				elif choice == 2:
					if phys >= chance:
						sit = 2.1 # change
					elif reflex >= chance:
						sit = 2.2 # change
					else:
						sit = 2.3 # change
					make_choice = False
				else:
					print('Please enter 1 or 2.')
					print()

		
	"""
		if status == 1 or status == 7:
			if status == 1:
				print('Game over. You have died!')
			if status == 7:
				print('Game over. You won!')
			sleep(0.5)
			play_game = (raw_input("Play again? Y/N: ")).upper()
			if play_game == 'Y':
				sleep(0.5)
				print('Game restarting...')
				sleep(1)
				status = 4
				playing_game = False
				start_game()
			elif play_game == 'N':
				print('Thanks for playing!')
				break
			else:
				print('Sorry, you did not enter Y or N. Please try again.')
	"""

# Helper functions

def pick_sit(name, age, occupation, phys, reflex, intellect, ppl, status):
	'''
	Picks a slightly random situation, based on status and occupation.
	Presents the user with 2 choices, and takes user's input.
	'''

start_game()

"""
Rate framework:
chance = randint(1, 100)
if rating >= chance:
	success
else:
	fail
"""



"""
Status System:
1 - dead/zombie
2 - infected
3 - injured
4 - alive (normal)
5 - alive (healthy)
6 - alive (close to being free)
7 - free (and alive)
"""
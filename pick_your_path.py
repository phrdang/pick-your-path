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

print "Welcome to Pick Your Path!"
sleep(0.5)
print "An interactive game where a combination of wise decision-making and a bit of luck will lead to success."
sleep(0.5)
print "Mode: Zombie Apocalypse"
sleep(1)

def start_game():
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

	first_name = first_names[randint(0,10)]
	last_name = last_names[randint(0,10)]

	name = first_name + ' ' + last_name 

	print 'Your name is %s.' % name

	sleep(0.5)

	age = randint(20, 65) 
	print "Your age is %d." % age

	if age >= 20 and age <= 30:
		age = 'young' 
		# Success rates 
		phys = 60 			#physical
		reflex = 80 		#reflexes
		intellect = 60 		#intellect
		ppl = 70 			#people skills
	elif age > 30 and age <= 50:
		age = 'midlife'
		phys = 70
		reflex = 60
		intellect = 70
		ppl = 70
	else:
		age = 'old'
		phys = 40
		reflex = 50
		intellect = 50
		ppl = 70

	sleep(0.5)

	pick_job = True
	while pick_job == True:
		occupation = raw_input("""Choose an occupation:
			(1) Physics teacher
			(2) CEO
			(3) Chef
			(4) Police officer
			(5) Sales representative
			(6) Unemployed
Enter an integer from 1-6: """)
		occupations = ['1', '2', '3', '4', '5', '6']
		if occupation not in occupations:
			pick_job = True
			print "Sorry, please enter the integer from 1-6 that corresponds to your occupation choice."
		else:
			pick_job = False
			if occupation == '1':
				print "You are a physics teacher."
				phys -= 5
				reflex += 0
				intellect += 20
				ppl += 5
				occupation = 'physics teacher'
			if occupation == '2':
				print "You are a CEO."
				phys -= 5
				reflex += 0
				intellect += 10
				ppl += 10
				occupation = 'CEO'
			if occupation == '3':
				print "You are a chef."
				phys += 5
				reflex += 0
				intellect += 5
				ppl += 0
				occupation = 'chef'
			if occupation == '4':
				print "You are a police officer."
				phys += 20
				reflex += 10
				intellect += 5
				ppl -= 10
				occupation = 'police officer'
			if occupation == '5':
				print "You are a sales representative."
				phys += 0
				reflex += 0
				intellect += 5
				ppl += 20
				occupation = 'sales representative'
			if occupation == '6':
				print "You are unemployed."	
				phys -= 10
				reflex += 0
				intellect -= 10
				ppl += 0
				occupation = 'unemployed'


	sleep(1)

	status = 4
	print "The game is now beginning. Good luck!"

	game(name, age, occupation, phys, reflex, intellect, ppl, status)


def game(name, age, occupation, phys, reflex, intellect, ppl, status):
	playing_game = True

	sit = 1

	while playing_game == True:
		if sit == 1:
			print """It's the weekend, and you're currently sitting at home. You've decided to binge watch Marvel's Agents of S.H.I.E.L.D., which your friend Brenda recommended to you, when suddenly you start to hear some sort of banging noise on your front door. Looking through the peephole, you see a horde of zombies trying to break through.

What do you do?
	(1) Grab your emergency supplies backpack and exit through the backyard
	(2) Grab your family's shotgun and a kitchen knife and try to mow down the zombies
"""
			make_choice = True
			while make_choice == True:
				choice = int(raw_input("Enter 1 or 2: "))
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
					print "Please enter 1 or 2."

		
	"""
		if status == 1 or status == 7:
			if status == 1:
				print 'Game over. You have died!'
			if status == 7:
				print 'Game over. You won!'
			sleep(0.5)
			play_game = (raw_input("Play again? Y/N: ")).upper()
			if play_game == 'Y':
				sleep(0.5)
				print 'Game restarting...'
				sleep(1)
				status = 4
				playing_game = False
				start_game()
			elif play_game == 'N':
				print 'Thanks for playing!'
				break
			else:
				print 'Sorry, you did not enter Y or N. Please try again.'
	"""

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
3 - infected
4 - alive (normal)
5 - alive (healthy)
6 - alive (close to being free)
7 - free (and alive)
"""

# Scenarios, 5 for each level (25 total b/c 1 and 7)

"""
Status 1:
1BBB

Status 2:
1BB

Status 3:
1B

Status 4: BEGIN GAME - you can never return to this?
1

Status 5:
1A

Status 6:
1AA

Status 7:
1AAA
"""


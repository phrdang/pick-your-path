import random as r
from time import sleep

### NAME DATABASE CREDITS ###
'''
ENGLISH FIRST AND LAST NAME:
https://github.com/smashew/NameDatabases 

FANTASY FIRST NAMES FOR FEMALE, MALE; LAST NAME:
https://www.mithrilandmages.com/utilities/MedievalBrowse.php?letter=B&fms=M
'''

### FUNCTIONS ###

def load_names(file_name, purpose):
    '''
    docstr
    '''
    names = []
    counter = 0

    file = open(file_name, 'r')

    for name in file:
        names.append(name.rstrip())
        counter += 1
    
    if purpose == 'f':
        print(counter, 'first names loaded.')
    else:
        print(counter, 'last names loaded.')
    
    file.close()

    return names

def choose_mode():
    '''
    docstr
    '''
    while True:
        mode = input('''Choose a mode:

    (1) Zombie Apocalypse
    (2) Medieval Fantasy
    (3) Natural Disaster

Enter 1, 2, or 3: ''')
        if mode == '1':
            mode = 'Zombie Apocalypse'
            break
        elif mode == '2':
            mode = 'Medieval Fantasy'
            break
        elif mode == '3':
            mode = 'Natural Disaster'
            break
        else:
            print('Error, please enter 1, 2, or 3.')
    return mode

def get_player_stats(mode):
    '''
    docstr
    '''
    # Stat caps after bonuses/handicaps added
    BONUS_MAX_STAT = 13
    HANDICAP_MIN_STAT = 2

    # Stat caps for original random number generation
    MAX_STAT = 10
    MIN_STAT = 5

    ### Name text files

    # English first and last names
    FN_FILE_NAME = 'first_names.txt'
    LN_FILE_NAME = 'last_names.txt'

    # Fantasy first and last names
    FANTASY_MALE_FN_FILE_NAME = 'fantasy_m_fn.txt'
    FANTASY_FEMALE_FN_FILE_NAME = 'fantasy_f_fn.txt'
    FANTASY_MIXED_FN_FILE_NAME = 'fantasy_o_fn.txt'
    FANTASY_LN_FILE_NAME = 'fantasy_ln.txt'

    if mode == 'Zombie Apocalypse' or mode == 'Natural Disaster':
        # Load names
        FIRST_NAMES = load_names(FN_FILE_NAME, 'f')
        LAST_NAMES = load_names(LN_FILE_NAME, 'l')

        # List of 10 possible jobs
        jobs = ['unemployed', 'CEO', 'chef', 'police officer', 'fire fighter', 'doctor', 'sales representative', 'waiter', 'teacher', 'fast food worker']

        # 2D dict of possible occupations and their corresponding stat bonuses or handicaps
        jobs_stats = {
            'unemployed':           {'str':-1, 'skl':-1, 'spd':-1, 'def':0, 'int':1, 'ppl':-1, 'luk':3}, 
            'CEO':                  {'str':-1, 'skl':1, 'spd':-1, 'def':1, 'int':3, 'ppl':2, 'luk':1}, 
            'chef':                 {'str':1, 'skl':1, 'spd':1, 'def':1, 'int':-1, 'ppl':0, 'luk':-1}, 
            'police officer':       {'str':3, 'skl':2, 'spd':1, 'def':3, 'int':0, 'ppl':0, 'luk':-2}, 
            'fire fighter':         {'str':3, 'skl':2, 'spd':2, 'def':2, 'int':0, 'ppl':0, 'luk':-2}, 
            'doctor':               {'str':0, 'skl':3, 'spd':0, 'def':-1, 'int':3, 'ppl':1, 'luk':1}, 
            'sales representative': {'str':-1, 'skl':0, 'spd':0, 'def':-1, 'int':1, 'ppl':3, 'luk':2}, 
            'waiter':               {'str':1, 'skl':1, 'spd':1, 'def':0, 'int':-1, 'ppl':1, 'luk':0}, 
            'teacher':              {'str':-1, 'skl':2, 'spd':0, 'def':0, 'int':2, 'ppl':1, 'luk':1},
            'fast food worker':     {'str':1, 'skl':0, 'spd':2, 'def':0, 'int':-1, 'ppl':1, 'luk':3}
        }
    elif mode == 'Medieval Fantasy':
        # Load names and pick jobs list based on gender
        while True:
            gender = input("Gender? Enter 'm', 'f', or 'o': ").lower()
            if gender == 'm':
                FIRST_NAMES = load_names(FANTASY_MALE_FN_FILE_NAME, 'f')
                # List of 10 possible jobs (male)
                jobs = ['court jester', 'knight', 'serf', 'king', 'prince', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']
                break
            elif gender == 'f':
                FIRST_NAMES = load_names(FANTASY_FEMALE_FN_FILE_NAME, 'f')
                # List of 10 possible jobs (female)
                jobs = ['court jester', 'knight', 'serf', 'queen', 'princess', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']
                break
            elif gender == 'o':
                FIRST_NAMES = load_names(FANTASY_MIXED_FN_FILE_NAME, 'f')
                # List of 12 possible jobs (other)
                jobs = ['court jester', 'knight', 'serf', 'king', 'queen', 'prince', 'princess', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']
                break
            else:
                print("Invalid input, please type 'm', 'f', or 'o'.")
        LAST_NAMES = load_names(FANTASY_LN_FILE_NAME, 'l')

        # 2D dict of possible occupations and their corresponding stat bonuses or handicaps
        jobs_stats = {
            'court jester':     {'str':-1, 'skl':1, 'spd':1, 'def':0, 'int':1, 'ppl':3, 'luk':3}, 
            'knight':           {'str':3, 'skl':2, 'spd':2, 'def':2, 'int':0, 'ppl':-1, 'luk':0}, 
            'serf':             {'str':1, 'skl':1, 'spd':-1, 'def':0, 'int':-1, 'ppl':2, 'luk':0}, 
            'king':             {'str':1, 'skl':2, 'spd':-1, 'def':1, 'int':2, 'ppl':2, 'luk':0}, 
            'queen':            {'str':1, 'skl':2, 'spd':-1, 'def':1, 'int':2, 'ppl':2, 'luk':0},
            'prince':           {'str':2, 'skl':1, 'spd':2, 'def':2, 'int':0, 'ppl':1, 'luk':-1}, 
            'princess':         {'str':2, 'skl':1, 'spd':2, 'def':2, 'int':0, 'ppl':1, 'luk':-1}, 
            'blacksmith':       {'str':3, 'skl':3, 'spd':-1, 'def':2, 'int':0, 'ppl':-1, 'luk':0}, 
            'wizard':           {'str':-1, 'skl':3, 'spd':0, 'def':2, 'int':1, 'ppl':-1, 'luk':2}, 
            'dragon rider':     {'str':3, 'skl':2, 'spd':3, 'def':3, 'int':-2, 'ppl':-3, 'luk':-1}, 
            'priest':           {'str':-1, 'skl':1, 'spd':0, 'def':-1, 'int':3, 'ppl':3, 'luk':1},
            'thief':            {'str':1, 'skl':2, 'spd':3, 'def':-1, 'int':2, 'ppl':-3, 'luk':2}
        }
    else:
        raise ValueError

    # Set name
    fn = r.choice(FIRST_NAMES)
    ln = r.choice(LAST_NAMES)
    name = fn + ' ' + ln

    # Set age
    age = r.randint(20, 65)

    # Set job
    job = r.choice(jobs)

    # Set strength, skill, speed, intellect, ppl, luck, and move
    strength = r.randint(MIN_STAT, MAX_STAT)
    skill = r.randint(MIN_STAT, MAX_STAT)
    speed = r.randint(MIN_STAT, MAX_STAT)
    defense = r.randint(MIN_STAT, MAX_STAT)
    intellect = r.randint(MIN_STAT, MAX_STAT)
    ppl = r.randint(MIN_STAT, MAX_STAT)
    luck = r.randint(MIN_STAT, MAX_STAT)

    move = r.randint(1, 5)

    # Change stats based on job bonuses/handicaps
    strength += jobs_stats[job]['str'] 
    skill += jobs_stats[job]['skl']
    speed += jobs_stats[job]['spd']
    defense += jobs_stats[job]['def']
    intellect += jobs_stats[job]['int']
    ppl += jobs_stats[job]['ppl']
    luck += jobs_stats[job]['luk']

    # stats list
    stats = [strength, skill, speed, defense, intellect, ppl, luck]

    # Check to make sure stats aren't above or below caps
    for i in range(0, len(stats)):
        if stats[i] < HANDICAP_MIN_STAT:
            stats[i] = HANDICAP_MIN_STAT
        if stats[i] > BONUS_MAX_STAT:
            stats[i] = BONUS_MAX_STAT

    # Add stats to the stats list
    return name, age, job, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], move

### CLASSES ###

class Player(object):
    '''
    doctsr
    '''
    # Constructor method
    def __init__(self, name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move):
        '''
        doctsr
        '''
        self.name = name # str, first last
        self.age = age # int from 20-65
        self.job = job # str

        self.strength = strength # int from 0-20
        self.skill = skill # int from 0-20
        self.speed = speed # int from 0-20
        self.defense = defense # int from 0-20
        self.intellect = intellect # int from 0-20
        self.ppl = ppl # int from 0-20
        self.luck = luck # int from 0-20

        self.move = move # int from 0-5

        self.status = ['alive', ['healthy']]
        # possible statuses: 
        # Overall: alive, dead, zombie
        # Specific: healthy (health, hunger, sleep all == 100), injured, gravely wounded, hungry, sleepy, thirsty
        self.health = 100
        # injured if health < 100
        # gravely wounded if health <= 50
        # dead if health <= 0
        # zombie if health == -1
        self.hunger = 100
        # hungry if hunger <= 50
        self.thirst = 100
        # thirsty if thirsty <= 50
        self.sleep = 100
        # sleepy if sleep <= 50

        # if hungry: strength -2, ppl -3
        # if thirsty: move -1, strength -3
        # if sleepy: speed -2, skill -3, intellect -3

        self.gear = {}
        self.weapons = {}

        self.level = 1
        self.exp = 0

    # str method
    def __str__(self):
        '''
        doctsr
        '''
        # To print gear and weapons as strings
        gear = ''
        weapons = ''

        for g in self.gear:
            gear += g + ' '
        
        for w in self.weapons:
            weapons += w + ' '

        # Lines of player stats, organized by category
        stats1 = 'IDENTITY\nName: %s | Age: %d | Job: %s' % (self.name, self.age, self.job)

        stats2 = 'STATS\nStrength: %d | Skill: %d | Speed: %d | Defense: %d | Intellect: %d | People Skills: %d | Luck: %d' % \
            (self.strength, self.skill, self.speed, self.defense, self.intellect, self.ppl, self.luck)

        stats3 = 'STATUS\nMove: %d | Overall Status: %s | Health: %d | Hunger: %d | Thirst: %d | Sleep: %d' % \
            (self.move, self.status[0], self.health, self.hunger, self.thirst, self.sleep)

        stats4 = 'Specific Status: %s' % (self.get_specific_status())

        stats5 = 'OTHER\nGear: %s | Weapons: %s | Level: %d | Experience: %d' % (gear, weapons, self.level, self.exp)

        return stats1 + '\n' + stats2 + '\n' + stats3 + '\n' + stats4 + '\n' + stats5

    # Condition checker methods
    def is_healthy(self):
        '''
        doctsr
        '''
        if self.health == 100 and self.hunger == 100 and self.thirst == 100 and self.sleep == 100:
            return True
        else:
            return False
    def is_injured(self):
        '''
        docstr
        '''
        if self.health < 100 and self.health > 50:
            return True
        else:
            return False
    def is_gravely_wounded(self):
        '''
        docstr
        '''
        if self.health <= 50 and self.health > 0:
            return True
        else:
            return False
    def is_dead(self):
        '''
        docstr
        '''
        if self.health == 0:
            return True
        else:
            return False
    def is_zombie(self):
        '''
        docstr
        '''
        if self.health == -1:
            return True
        else:
            return False
    def is_hungry(self):
        '''
        doctsr
        '''
        if self.hunger <= 50:
            return True
        else:
            return False
    def is_thirsty(self):
        '''
        doctsr
        '''
        if self.thirst <= 50:
            return True
        else:
            return False
    def is_sleepy(self):
        '''
        doctsr
        '''
        if self.sleep <= 50:
            return True
        else:
            return False
    
    def get_specific_status(self):
        '''
        doctsr
        '''
        specific_status = ''
        
        if self.is_healthy():
            specific_status += 'healthy '
        else:
            if self.is_injured():
                specific_status += 'injured '
            if self.is_gravely_wounded():
                specific_status += 'gravely wounded '
            if self.is_hungry():
                specific_status += 'hungry '
            if self.is_thirsty():
                specific_status += 'thirsty '
            if self.is_sleepy():
                specific_status += 'sleepy'

        return specific_status

    # setters and getters
    # str method
    # level up
    # change status
    # heal
    # eat
    # drink
    # equip gear
    # equip weapon
    # fight
    

### MAIN ###

def main():
    '''
    docstr
    '''
    # Upon startup, welcome player to game
    print('Welcome to Pick Your Path!')
    sleep(0.5)
    print('An interactive game where a combination of wise decision-making and a bit of luck will lead to success.')
    sleep(0.5)
    # Allow player to choose from different modes
    mode = choose_mode()
    print('Mode:', mode)
    sleep(1)

    name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move = get_player_stats(mode) 

    player = Player(name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move)

    print(player)

main()
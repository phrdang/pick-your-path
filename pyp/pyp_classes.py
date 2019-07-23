import random as r
from time import sleep

VERSION = 0.1

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


class Item(object):
    pass

class Gear(Item):
    pass

class Weapon(Item):
    pass

class Inventory(object):
    pass

class Zombie(object):
    pass
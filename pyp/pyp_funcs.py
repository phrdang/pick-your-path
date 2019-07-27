import random as r
from time import sleep
from getpass import getpass
from . import pyp_classes as c

VERSION = 0.1
RESERVED = ['$__exit__', '$__cancel__', '$__save__', '$__logout__', '$__inventory__', '$__map__', '$__guide__', '$__back__', '$__view__']

def print_header(mode, user=''):
    '''
    Prints different game headers that
    display different overall commands,
    depending on the mode.

    mode: str, the part of the game the
    user is currently using (see below)

    user: str, the username of the user

    mode args: 
    'li' = login
    'm' = choose your mode
    'crg' = create - create or generate
    'cris' = create - identity OR create - statistics
    'g' = guide
    'ch' = chapter
    'sim' = view player stats, invetory, OR map
    's' = save
    'lo' = logout

    Returns: None
    '''
    DIVIDER = '-' * 100
    PYP = 'PICK YOUR PATH'
    SPACES = 14 - len(user)

    # Login
    if mode == 'li':
        print(DIVIDER)
        print(PYP + ' ' * 74 + '(X) Exit', end='\n')
        print(DIVIDER)

        sleep(1)
        print('Welcome to Pick Your Path!')
        sleep(1)
        print('An interactive game where a combination of wise decision-making and a bit of luck will lead to success.', end='\n')
        sleep(1)

    # Choose Your Mode
    elif mode == 'm':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * (26-len(user)) + '(L) Logout', end='\n')
        print(DIVIDER)

    # Create Your Player - Create or Generate
    elif mode == 'crg':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout', end='\n')
        print(DIVIDER)
    
    # Create Your Player - Identity or Create Your Player - Statistics
    elif mode == 'cris':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 88 + '(G) Guide')
        print(DIVIDER)

    # Guide
    elif mode == 'g':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 76 + '(B) Back' + ' ' * 4 + '(X) Exit')
        print(DIVIDER)

    # Chapter
    elif mode == 'ch':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 28 + '(V) View player stats' + ' ' * 7 + '(I) Inventory' + ' ' * 7 + '(M) Map' + ' ' * 5 + '(G) Guide')
        print(DIVIDER)

    # View Player Stats or Inventory or Map 
    elif mode == 'sim':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 88 + '(X) Exit')
        print(DIVIDER)
    
    # Save
    elif mode == 's':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(L) Logout' + ' ' * 2 + '(X) Exit', end='\n')
        print(DIVIDER)

    # Logout
    elif mode == 'lo':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(X) Exit', end='\n')
        print(DIVIDER)

    else:
        raise ValueError('''Invalid mode argument. Valid mode arguments: 
    'li' = login
    'm' = choose your mode
    'crg' = create - create or generate
    'cris' = create - identity OR create - statistics
    'g' = guide
    'ch' = chapter
    'sim' = view player stats, invetory, OR map
    's' = save
    'lo' = logout''')

def get_command(valid_input):
    '''
    Continuously prompts user to 
    enter a command and validates 
    input.

    valid_input: list of lowercase str, 
    valid user input for that prompt

    Returns: command, lowercase str
    '''
    # Checks if valid_input is an empty list
    if len(valid_input) == 0:
        raise ValueError('valid_input cannot be an empty list')
    
    # Initialize as empty str
    # The valid var will be printed if
    # user enters invalid input
    valid = ''

    # Iterate through valid_input list and
    # add each type of valid input to the 
    # valid str so that it is readable by user
    for i in valid_input:
        # If the current valid input is also
        # the last item on the valid_input list,
        # don't concatenate a comma
        if i == valid_input[-1]:
            valid += i
        # If the current valid input is also
        # the second to last item on the
        # valid_input list... 
        elif i == valid_input[-2]:
            # Add a comma and 'or' if there
            # are at least 3 valid options
            if len(valid_input) > 2:
                valid += i + ', or '
            # Add only an 'or' if there are
            # only 2 valid options
            else:
                valid += i + ' or '
        # Otherwise, add a comma after each valid option
        else:
            valid += i + ', '

    # Continuously ask user for valid input
    while True:
        try:
            command = input('Command: ').lower()
            assert command in valid_input
        # Display error message if invalid
        except AssertionError:
            print('Error, please enter ' + valid + '.')
        else:
            break
    
    return command

def login():
    '''
    docstr
    '''
    print_header('li')

    logging_in = True
    while logging_in:
        print('LOGIN')
        print('Do you already have an account?')
        print('\t(Y) Yes')
        print('\t(N) No')

        command = get_command(['y', 'n', 'x'])

        if command == 'y':
            print()
            print('NOTE: When typing your password, the characters will not display\non the screen for security purposes.', end='\n')

            login_info = load_login_info()

            counter = 0
            while True:
                username = input('Username: ').lower()
                password = getpass('Password: ')

                print()
                print('Authenticating...', end='\n')
                sleep(1)

                if username not in login_info:
                    print('Invalid username.')
                    counter += 1
                elif login_info[username] != password:
                    print('Invalid password.')
                    counter += 1
                else:
                    print('Login successful.')
                    logging_in = False
                    break

                if counter > 5:
                    print("It seems like you're having some trouble logging in.")
                    sleep(0.5)
                    print("(F) I forgot my password and want to reset it")
                    print("(C) I want to continue logging in")
                    print("(N) I want to create new account")

                    command = get_command(['f', 'c', 'n'])

                    # Forgot password
                    if command == 'f':
                        print('You chose forgot your password.')
                        print('To reset your password, please enter your username.')
                        
                        while True:
                            username = input('Username: ').lower()
                            if username not in login_info:
                                print('Username not found.')
                            else:
                                break
                        
                        new_pw = set_password()

                        # Reset password
                        reset_password(username, new_pw)

                        print("Type in 'y' for the next command prompt and enter your new login info.")
                        break

                    # Continue logging in
                    elif command == 'c':
                        print('You chose to continue logging in.')
                        counter = 0

                    # Create new account
                    elif command == 'n':
                        print('You chose to create a new account.')
                        print("Type in 'n' for the next command prompt.")
                        break

            ### STILL NEEDS TO BE CODED ###
            # Load save files of user 
            load_save_file('file.txt') # needs file name as arg

            return username

        elif command == 'n':
            print()
            print('You are now creating a new account.', end='\n')

            username = create_new_account()

            if username != '$__cancel__':
                return username
                break
            
        elif command == 'x':
            return '$__exit__'
            break
            
def create_new_account():
    '''
    docstr
    '''
    # Set username
    print('Usernames are case insensitive and CANNOT contain spaces or backslashes.')
    print('They must also contain 1-13 characters and be unique.')
    print("Enter 'c' to cancel.", end='\n')

    while True:
        username = input('Username: ').lower()
        if not username:
            print('Usernames must contain at least 1 character.')
        elif username.find(' ') != -1:
            print('Usernames cannot contain spaces.')
        elif username.find('\\') != -1:
            print('Usernames cannot contain backslashes.')
        elif username in load_login_info():
            print('Username already exists.')
        elif len(username) > 13:
            print('Usernames cannot be longer than 13 characters.')
        elif username in RESERVED:
            print('Reserved, please choose a different username.')
        elif username == 'c':
            print('Canceling...', end='\n')
            return '$__cancel__'
            break
        else:
            break
    
    # Set password
    print()
    password = set_password()

    # Save new login info
    save_login_info(username, password)

    # Confirmation message
    print('New account created successfully.') 
    print('Username: ' + username)
    print('Password: ' + '*' * len(password))

    return username

def set_password():
    '''
    docstr
    '''
    print('Passwords are CASE SENSITIVE and CANNOT contain backslashes or spaces.')
    print('They must also contain at least 1 character.')
    print('NOTE: When typing your password, the characters will not display\non the screen for security purposes.')

    entering_new_pw = True

    while entering_new_pw:
        new_pw = getpass('Password: ')
        if not new_pw:
            print('Passwords must be at least 1 character long.')
        elif new_pw.find(' ') != -1:
            print('Passwords cannot contain spaces.')
        elif new_pw.find('\\') != -1:
            print('Passwords cannot contain backslashes.')
        else:
            counter = 0
            while True:
                confirm_pw = getpass('Confirm password: ')
                if confirm_pw == new_pw:
                    entering_new_pw = False
                    break
                else:
                    counter += 1
                    if counter < 4:
                        print('Passwords do not match, please try confirming them again.')
                    else:
                        print('Passwords still do not match, please enter a new password and confirm that password instead.')
                        break

    return new_pw

def reset_password(user, new_pw):
    '''
    Updates the .login.txt file with
    new login info for specified user.

    user: str, username of the account 
    the user wants to change the password of

    new_pw: str, new password

    Returns: None
    '''
    # Open file in read mode
    file = open('.login.txt', 'r')

    # Save each line in the file in a list
    login_info = file.readlines()

    # Find the line in the text file with the
    # matching username, then update that line
    # with the new password
    for i in range(0, len(login_info)-1):
        if login_info[i].startswith(user):
            login_info[i] = user + ' ' + new_pw + '\n'
    
    # Close the file
    file.close()
    
    # Write the updated login info to the file
    file = open('.login.txt', 'w')
    file.writelines(login_info)
    file.close()
    
    # Confirmation message
    print('Password reset successful.')
    print('Username: ' + user)
    print('Password: ' + '*' * len(new_pw))

def save_login_info(user, pw):
    '''
    docstr
    '''
    file = open('.login.txt', 'a')
    file.write(user + ' ' + pw + '\n')
    file.close()

def load_login_info():
    '''
    docstr
    '''
    login_info = {}

    file = open('.login.txt', 'r')

    for line in file:
        # Username and password are separated
        # by a space, so strip \n and split
        info = line.rstrip().split()
        user = info[0]
        pw = info[1]

        # Add username and password pair to the dict
        login_info[user] = pw

    file.close()
    
    return login_info

def load_save_file(file_name):
    '''
    docstr
    '''
    pass

def choose_mode(user):
    '''
    docstr
    '''
    print_header('m', user)
    print('CHOOSE YOUR MODE', end='\n')
    print('''Choose a mode:

    (1) Zombie Apocalypse
    (2) Medieval Fantasy
    (3) Natural Disaster

''')
    
    mode = get_command(['1', '2', '3', 'l'])
    
    if mode == '1':
        mode = 'Zombie Apocalypse'
        print('Mode:', mode)
    elif mode == '2':
        mode = 'Medieval Fantasy'
        print('Mode:', mode)
    elif mode == '3':
        mode = 'Natural Disaster'
        print('Mode:', mode)
    elif mode == 'l':
        return 'logout'

def create_player(mode, user):
    '''
    docstr
    '''
    print_header('crg', user)
    print('CREATE YOUR PLAYER - CREATE OR GENERATE')

    print('Create your own player or generate random player?', end='\n')
    print('\t(1) Create my own player')
    print('\t(2) Generate random player', end='\n')

    command = get_command(['1', '2', 's', 'l'])

    if command == '1':
        print('You chose to create your own player.')
        player = user_creates_player(mode, user)

        ### Edit to make it more aesthetic later
        print()
        print(player, end='\n')
        
        return player
    elif command == '2':
        print('You chose to generate a random player.')
        player = generate_player(mode)

        ### Edit to make it more aesthetic later
        print()
        print(player, end='\n')
        return player
    elif command == 's':
        return '$__save__'
    elif command == 'l':
        return '$__logout__'
    else:
        raise ValueError
    
def user_creates_player(mode, user):
    '''
    docstr
    '''
    ZOMBIE_JOBS = []
    FANTASY_JOBS = []
    DISASTER_JOBS = []

    if mode == 'Zombie Apocalypse':
        JOBS = ZOMBIE_JOBS
    elif mode == 'Medieval Fantasy':
        # Jobs list is picked later (see below)
        pass
    elif mode == 'Natural Disaster':
        JOBS = DISASTER_JOBS
    else:
        raise ValueError("Invalid mode argument. Valid modes: 'Zombie Apocalypse', 'Medieval Fantasy', 'Natural Disaster'")

    print_header('cris', user)
    print('CREATE YOUR PLAYER - IDENTITY', end='\n')
    print("*** Once you press 'Enter', the input you give cannot be undone. ***", end='\n')

    while True:
        first_name = input('First name: ').capitalize()
        if first_name:
            break
        else:
            print('Please enter a first name.')
    
    while True:
        last_name = input('Last name: ').capitalize()
        if last_name:
            break
        else:
            print('Please enter a last name.')

    name = first_name + ' ' + last_name
    
    while True:
        try:
            age = int(input('Age (from 20-65): '))
            assert age >= 20 and age <= 65
        except ValueError:
            print('Please enter an integer.')
        except AssertionError:
            print('Please enter an age from 20-65.')
        else:
            break

    if mode == 'Medieval Fantasy':
        while True:
            try:
                gender = input("Gender (m, f, or o): ").lower()
                assert gender in ['m', 'f', 'o']
            except AssertionError:
                print('Please enter m, f, or o for male, female, or other, respectively.')
            else:
                break
        if gender == 'm':
            JOBS = ['court jester', 'knight', 'serf', 'king', 'prince', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']
        elif gender == 'f':
            JOBS = ['court jester', 'knight', 'serf', 'queen', 'princess', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']
        else:
            JOBS = ['court jester', 'knight', 'serf', 'king', 'queen', 'prince', 'princess', 'blacksmith', 'wizard', 'dragon rider', 'priest', 'thief']

    counter = 1
    pick_job = {}
    for job in JOBS:
        print('(%d) %s' % counter, job.capitalize())
        pick_job[counter] = job
        counter += 1

    while True:
        try:
            job = int(input('Job (enter a number): '))
            assert job >= 1 and job <= len(pick_job)
        except ValueError:
            print('Please enter a number (see above).')
        except AssertionError:
            print('Please enter a number (see above).')
        else:
            break

    job = pick_job[job]

    print('You chose to be a ' + job + '.', end='\n')



def generate_player(mode):
    '''
    docstr
    '''
    # Get player stats randomly
    name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move = get_player_stats(mode)
    # Create new Player object using those stats
    player = c.Player(name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move)
    return player

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
    FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/first_names.txt'
    LN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/last_names.txt'

    # Fantasy first and last names
    FANTASY_MALE_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_m_fn.txt'
    FANTASY_FEMALE_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_f_fn.txt'
    FANTASY_MIXED_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_o_fn.txt'
    FANTASY_LN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_ln.txt'

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
        raise ValueError("Invalid mode. Valid modes: 'Zombie Apocalypse', 'Medieval Fantasy', 'Natural Disaster'")

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

def load_names(file_name, purpose):
    '''
    docstr
    '''
    names = []
    # counter = 0

    file = open(file_name, 'r')

    for name in file:
        names.append(name.rstrip())
        # counter += 1
    
    # Names counter
    # if purpose == 'f':
    #     print(counter, 'first names loaded.')
    # else:
    #     print(counter, 'last names loaded.')
    
    file.close()

    return names

def print_credits():
    '''
    Prints credits for the program.

    Returns: None
    '''
    # Ask user if they want to view the credits
    print('''Would you like to view the credits? 
    (Y) Yes
    (N) No''')

    wants_credits = get_command(['y', 'n'])
    if wants_credits == 'y':
        wants_credits = True
    else:
        wants_credits = False

    # Prints credits if user said yes, otherwise skip to exit
    if wants_credits:
        sleep(1)

        print('Author: Rebecca Dang')
        print('Version: ' + str(VERSION), end='\n')
        sleep(1)

        print('Language: Python 3')
        print('Text Editor: Visual Studio Code', end='\n')
        sleep(1)

        print('SPECIAL THANKS')
        print('Name databases:')
        print('English names: https://github.com/smashew/NameDatabases')
        print('Fantasy names: https://www.mithrilandmages.com/utilities/MedievalBrowse.php?letter=A&fms=F')
        sleep(1)
        print('People:')
        print('My family and CS teachers')
    
    sleep(1)
    print()
    print('Thank you for using Pick Your Path!')
    print('You have succesfully exited the program.')
from getpass import getpass
import random as r
from time import sleep

import pyp_classes as c

VERSION = 0.1

EXIT = '$__exit__'
CANCEL = '$__cancel__'
SAVE = '$__save__'
LOGOUT = '$__logout__'
INVENTORY = '$__inventory__'
MAP = '$__map__'
GUIDE = '$__guide__'
BACK = '$__back__'
VIEW = '$__view__'
RESERVED = [EXIT, CANCEL, SAVE, LOGOUT, INVENTORY, MAP, GUIDE, BACK, VIEW]


def print_header(interface, user=''):
    '''
    Prints different game headers that
    display different overall commands,
    depending on the mode.
    
    Arguments:
        interface {str} -- the interface the user is currently using
        
        Valid interface args:
        'li' = login,
        'm' = choose your mode,
        'crg' = create - create or generate,
        'cris' = create - identity OR create - statistics,
        'g' = guide,
        'ch' = chapter,
        'sim' = view player stats, invetory, OR map,
        's' = save,
        'lo' = logout
    
    Keyword Arguments:
        user {str} -- username of the current user (default: '')
    
    Raises:
        ValueError: If interface argument is invalid
    
    Returns:
        {NoneType}
    '''
    DIVIDER = '-' * 100
    PYP = 'PICK YOUR PATH'
    SPACES = 14 - len(user)

    # Login
    if interface == 'li':
        print(DIVIDER)
        print(PYP + ' ' * 74 + '(X) Exit', end='\n\n')
        print(DIVIDER)

        sleep(1)
        print('Welcome to Pick Your Path!')
        sleep(1)
        print('An interactive game where a combination of wise decision-making and a bit of luck will lead to success.', end='\n\n')
        sleep(1)

    # Choose Your Mode
    elif interface == 'm':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * (26-len(user)) + '(L) Logout', end='\n\n')
        print(DIVIDER)

    # Create Your Player - Create or Generate
    elif interface == 'crg':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout', end='\n\n')
        print(DIVIDER)
    
    # Create Your Player - Identity or Create Your Player - Statistics
    elif interface == 'cris':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 88 + '(G) Guide')
        print(DIVIDER)

    # Guide
    elif interface == 'g':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 76 + '(B) Back' + ' ' * 4 + '(X) Exit')
        print(DIVIDER)

    # Chapter
    elif interface == 'ch':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 28 + '(V) View player stats' + ' ' * 7 + '(I) Inventory' + ' ' * 7 + '(M) Map' + ' ' * 5 + '(G) Guide')
        print(DIVIDER)

    # View Player Stats or Inventory or Map 
    elif interface == 'sim':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(L) Logout')
        print(' ' * 88 + '(X) Exit')
        print(DIVIDER)
    
    # Save
    elif interface == 's':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(L) Logout' + ' ' * 2 + '(X) Exit', end='\n\n')
        print(DIVIDER)

    # Logout
    elif interface == 'lo':
        print(DIVIDER)
        print(PYP + ' ' * 42 + 'User: ' + user + ' ' * SPACES + '(S) Save' + ' ' * 4 + '(X) Exit', end='\n\n')
        print(DIVIDER)

    else:
        raise ValueError('''Invalid interface argument. Valid interface arguments: 
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
    
    Arguments:
        valid_input {list} -- valid user input for that prompt, 
        elements are lowercase strings
    
    Raises:
        ValueError: If valid_input is an empty list
    
    Returns:
        command {str} -- lowercase, the user's valid command
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
    Login interface. Lets user login to their
    existing account or create a new account, 
    as well as exit the program. If they login,
    they will also have the option to start a new
    game or continue an existing one from save
    file(s).
    
    Returns:
        username {str} -- username of the current user 
        or exit reserved string
    '''
    # Print login header
    print_header('li')

    # Logging in while loop
    logging_in = True
    while logging_in:
        # Ask user whether they have an account
        print('LOGIN')
        print('Do you already have an account?')
        print('\t(Y) Yes')
        print('\t(N) No')

        command = get_command(['y', 'n', 'x'])

        # Enter login credentials
        if command == 'y':
            print()
            print('NOTE: When typing your password, the characters will not display\non the screen for security purposes.', end='\n\n')

            # Load valid usernames/passwords onto login_info dict
            login_info = load_login_info()

            # Keep track of login attempts
            counter = 0
            while True:
                username = input('Username: ').lower()
                password = getpass('Password: ')

                print()
                print('Authenticating...', end='\n\n')
                sleep(1)

                # If username doesn't exist, try again
                if username not in login_info:
                    print('Invalid username.')
                    counter += 1
                # If password doesn't match username, try again
                elif login_info[username] != password:
                    print('Invalid password.')
                    counter += 1
                # If credentials valid, stop logging in
                else:
                    print('Login successful.')
                    logging_in = False
                    break

                # If user has attempted to login more than 5 times,
                # prompt user to reset password, keep trying  to login,
                # or create a new account
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
                        
                        # Ask user for account's username
                        while True:
                            username = input('Username: ').lower()
                            if username not in login_info:
                                print('Username not found.')
                            else:
                                break
                        
                        # User resets password
                        new_pw = set_password()

                        # Replace old username/password pair on the
                        # .login.txt file with the new one
                        reset_password(username, new_pw)

                        print("Type in 'y' for the next command prompt and enter your new login info.")
                        break

                    # Continue logging in
                    elif command == 'c':
                        print('You chose to continue logging in.')
                        # Reset login attempts counter
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

        # Create a new account
        elif command == 'n':
            print()
            print('You are now creating a new account.', end='\n\n')

            username = create_new_account()

            # If username is not a reserved command, stop
            # logging in (else, continue loop)
            if username != CANCEL:
                return username
                break

        # Exit program  
        elif command == 'x':
            return EXIT
            break
            
def create_new_account():
    '''
    Creates a new account. Ensures username and password 
    meet all requirements and saves the login info onto 
    the .login.txt file. 
    
    Returns:
        username {str} -- username of the new account or cancel reserved string
    '''
    # Set username
    print('Usernames are case insensitive and CANNOT contain spaces or backslashes.')
    print('They must also contain 1-13 characters and be unique.')
    print("Enter 'c' to cancel.", end='\n\n')

    # Validate username
    while True:
        username = input('Username: ').strip().lower()
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
            print('Canceling...', end='\n\n')
            return CANCEL
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
    Set the password of a given account. Ensures that
    password meets all requirements. 
    
    Returns:
        new_pw {str} -- new password
    '''
    print('Passwords are CASE SENSITIVE and CANNOT contain backslashes or spaces.')
    print('They must also contain at least 1 character.')
    print('NOTE: When typing your password, the characters will not display\non the screen for security purposes.')

    entering_new_pw = True
    # Password input validation
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
            # If password meets all requirements, ask
            # user to confirm it
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
    
    Arguments:
        user {str} -- username of account which 
        password has changed,
        new_pw {str} -- new password to save
    
    Returns:
        {NoneType}
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
    Saves new account login info onto
    the .login.txt file.
    
    Arguments:
        user {str} -- username,
        pw {str} -- password
    
    Returns:
        {NoneType}
    '''
    file = open('.login.txt', 'a')
    # Write user/pw pair on a new line, 
    # separated by a space
    file.write(user + ' ' + pw + '\n')
    file.close()

def load_login_info():
    '''
    Reads the .login.txt file and creates 
    a dict with username/password pairs.
    
    Returns:
        login_info {dict} -- key: username {str}, value: password {str}
    '''
    login_info = {}

    file = open('.login.txt', 'r')

    for line in file:
        # Username and password are separated
        # by a space, so strip '\n' and split
        user, pw = line.rstrip().split()

        # Add username and password pair to the dict
        login_info[user] = pw

    file.close()
    
    return login_info

def load_save_file(file_name):
    '''
    [summary]
    
    Arguments:
        file_name {str} -- name of save file (.txt) to load
    
    Raises:
    
    Returns:

    '''
    pass

def choose_mode(user):
    '''
    Choose your mode interface. Asks user to choose
    between 3 game modes.
    
    Arguments:
        user {str} -- username of current user
    
    Returns:
        mode {str} -- game mode the user chose or 
        logout reserved string
    '''
    print_header('m', user)
    print('CHOOSE YOUR MODE', end='\n\n')
    print('Choose a mode:', end='\n\n')
    print('\t(1) Zombie Apocalypse')
    print('\t(2) Medieval Fantasy')
    print('\t(3) Natural Disaster', end='\n\n')
    
    # Ask user to choose a mode
    mode = get_command(['1', '2', '3', 'l'])
    
    # Return mode that they chose, or logout
    if mode == '1':
        mode = 'Zombie Apocalypse'
        print('Mode:', mode)
        return 'Zombie Apocalypse'
    elif mode == '2':
        mode = 'Medieval Fantasy'
        print('Mode:', mode)
        return 'Medieval Fantasy'
    elif mode == '3':
        mode = 'Natural Disaster'
        print('Mode:', mode)
        return 'Natural Disaster'
    elif mode == 'l':
        return LOGOUT

def create_player(mode, user):
    '''
    Create your player interface. Lets user
    either create their own player or
    generate a player with random stats.
    
    Arguments:
        mode {str} -- game mode,
        user {str} -- username of current user
    
    Returns:
        player {Player} or {str} -- player object, or
        logout or save reserved string
    '''
    print_header('crg', user)
    print('CREATE YOUR PLAYER - CREATE OR GENERATE')

    print('Create your own player or generate random player?', end='\n\n')
    print('\t(1) Create my own player')
    print('\t(2) Generate random player', end='\n\n')

    # Ask user if they want to create their own or 
    # randomly generate a player
    command = get_command(['1', '2', 's', 'l'])

    # Create own player
    if command == '1':
        print('You chose to create your own player.')
        player = enter_player_stats(mode, user)

        ### Edit to make it more aesthetic later
        # Print player info
        print()
        print(player, end='\n\n')
        
        return player
    
    # Generate random player
    elif command == '2':
        print('You chose to generate a random player.')
        player = generate_player(mode)

        ### Edit to make it more aesthetic later
        # Print player info
        print()
        print(player, end='\n\n')
        
        return player
    
    # Save
    elif command == 's':
        return SAVE
    
    # Logout
    elif command == 'l':
        return LOGOUT
    
def enter_player_stats(mode, user):
    '''
    Allows user to create their own player
    by entering data to create a Player
    object. Returns Player object created
    using given stats.
    
    Arguments:
        mode {str} -- game mode,
        user {str} -- username of current user
    
    Raises:
        ValueError: If invalid mode argument given
    
    Returns:
        player {Player} -- player object with entered stats, or
        save or logout reserved strings
    '''
    ### IDENTITY ###
    ZOMBIE_JOBS = ['unemployed', 'CEO', 'chef', 'police officer', 'fire fighter', 'doctor', 'sales representative', 'waiter', 'teacher', 'fast food worker']
    DISASTER_JOBS = ['job1'] # add later

    # Assign JOBS to different jobs list 
    # depending on game mode
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
    print('CREATE YOUR PLAYER - IDENTITY', end='\n\n')
    print("*** Once you press 'Enter', the input you give cannot be undone. ***", end='\n\n')

    # Input validation for first name
    while True:
        first_name = input('First name: ').strip().capitalize()
        if first_name:
            break
        else:
            print('Please enter a first name.')
    
    # Input validation for last name
    while True:
        last_name = input('Last name: ').strip().capitalize()
        if last_name:
            break
        else:
            print('Please enter a last name.')

    # Concatenate first and last names 
    # with a space between them
    name = first_name + ' ' + last_name
    
    # Input validation for age
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

    # If mode is Medieval Fantasy, choose jobs list
    # based on user's gender
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

    # Print all job options
    counter = 1
    pick_job = {}
    for job in JOBS:
        # Keep letter case for CEO, capitalize everything else
        if job != 'CEO':
            print('\t(%d) %s' % (counter, job.capitalize()))
        else:
            print('\t(%d) %s' % (counter, job))
        # Add number and corresponding job to
        # pick_job dict so that user can pick a job
        # based on its number
        pick_job[counter] = job
        counter += 1
    
    # Ask user to pick a job and do input validation
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

    # Assign string job to job variable
    job = pick_job[job]

    print('You chose to be a ' + job + '.', end='\n\n')

    ### ASK IF USER WANTS GUIDE ###
    print('You have 60 points to distribute as you wish between 7 types of statistics.', end='\n\n')
    print('Before distributing points, it is recommended that you view the guide to understand')
    print('what each statistic affects during gameplay.', end='\n\n')
    print('Would you like to view the guide?')
    print('\t(Y) Yes')
    print('\t(N) No')
    
    command = get_command(['y', 'n', 'g', 's', 'l'])

    # View guide if user wants to read it
    if command == 'y' or command == 'g':
        guide(user)
    # Don't display guide if user doesn't want it
    elif command == 'n':
        pass
    # Save
    elif command == 's':
        return SAVE
    # Logout
    elif command == 'l':
        return LOGOUT

    ### STATISTICS ###
    print_header('cris', user)
    print('CREATE YOUR PLAYER - STATISTICS')
    print('You have 60 points to distribute as you wish between 7 types of statistics.')
    print("Enter the number of points you'd like to give for each statistic.")
    print('They must be between 5 and 10.', end='\n\n')
    print("*** Once you press 'Enter', the input you give cannot be undone. ***", end='\n\n')
    
    points_left = 60

    # Stat input while loop
    while True:
        # Strength input validation
        while True:
            try:
                strength = int(input('Strength: '))
                assert strength >= 5 and strength <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break
        
        # Display points left
        points_left -= strength
        print('You have %d points left.' % (points_left))
        
        # Skill input validation
        while True:
            try:
                skill = int(input('Skill: '))
                assert skill >= 5 and skill <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break
        
        # Display points left
        points_left -= skill
        print('You have %d points left.' % (points_left))
        
        # Speed input validation
        while True:
            try:
                speed = int(input('Speed: '))
                assert speed >= 5 and speed <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break

        # Display points left
        points_left -= speed
        print('You have %d points left.' % (points_left))
        
        # Defense input validation
        while True:
            try:
                defense = int(input('Defense: '))
                assert defense >= 5 and defense <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break
        
        # Display points left
        points_left -= defense
        print('You have %d points left.' % (points_left))
        
        # Intellect input validation
        while True:
            try:
                intellect = int(input('Intellect: '))
                assert intellect >= 5 and intellect <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break
        
        # Display points left
        points_left -= intellect
        print('You have %d points left.' % (points_left))
        
        # People Skills input validation
        while True:
            try:
                ppl = int(input('People Skills: '))
                assert ppl >= 5 and ppl <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break

        # Display points left
        points_left -= ppl
        print('You have %d points left.' % (points_left))
        
        # Luck input validation
        while True:
            try:
                luck = int(input('Luck: '))
                assert luck >= 5 and luck <= 10
            except ValueError:
                print('Please enter an integer.')
            except AssertionError:
                print('Please enter an integer from 5-10.')
            else:
                break
        
        # Calculate points left
        points_left -= luck

        # Keep asking user to distribute points
        # if not exactly 60 pts used
        if points_left < 0:
            print('You spent more than 60 pts, please try again.')
            print('Resetting statsitics...')
            sleep(1)
            points_left = 60
        elif points_left > 0:
            print('You still have %d points to spend. Please try again.' % points_left)
            print('Resetting statsitics...')
            sleep(1)
            points_left = 60
        # If exactly 60 points used, break
        elif points_left == 0:
            break

    # Randomly assign move and display the stat
    move = r.randint(1, 5)
    print()
    print('Move has been randomly set to %d.' % move)

    # Create Player object based on stats

    ### GIVE JOB BONUSES/HANDICAPS

    player = c.Player(name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move)
    return player

def generate_player(mode):
    '''
    Generates a player randomly based
    on the game mode.
    
    Arguments:
        mode {str} -- game mode
    
    Returns:
        player {Player} -- player object
    '''
    # Get player stats randomly
    name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move = get_player_stats(mode)
    # Create new Player object using those stats
    player = c.Player(name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move)
    return player

def get_player_stats(mode):
    '''
    Generates random statistics to create a 
    Player object.
    
    Arguments:
        mode {str} -- game mode
    
    Raises:
        ValueError: If invalid mode is given
    
    Returns:

        name {str} -- name, 
        age {int} -- age from 20-65, 
        job {str} -- job, based on game mode, 
        stats[0] {int} -- strength from 2-13, 
        stats[1] {int} -- skill from 2-13, 
        stats[2] {int} -- speed from 2-13, 
        stats[3] {int} -- defense from 2-13, 
        stats[4] {int} -- intellect from 2-13, 
        stats[5] {int} -- people skills from 2-13, 
        stats[6] {int} -- luck from 2-13, 
        move {int} -- move from 1-5
    '''
    # Stat caps after bonuses/handicaps added
    BONUS_MAX_STAT = 13
    HANDICAP_MIN_STAT = 2

    # Stat caps for original random number generation
    MAX_STAT = 10
    MIN_STAT = 5

    # English first and last names
    FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/first_names.txt'
    LN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/last_names.txt'

    # Fantasy first and last names
    FANTASY_MALE_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_m_fn.txt'
    FANTASY_FEMALE_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_f_fn.txt'
    FANTASY_MIXED_FN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_o_fn.txt'
    FANTASY_LN_FILE_NAME = '/Users/rebeccadang/Desktop/Visual Studio Code/pick-your-path/names/fantasy_ln.txt'

    # Generate job if mode is Zombie Apocalypse or Natural Disaster
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
    # Generate job if mode is Medieval Fantasy
    elif mode == 'Medieval Fantasy':
        # Load names and pick jobs list based on gender
        while True:
            # Ask user for their gender
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
    # If they are, set the values to the min or max
    for i in range(0, len(stats)):
        if stats[i] < HANDICAP_MIN_STAT:
            stats[i] = HANDICAP_MIN_STAT
        if stats[i] > BONUS_MAX_STAT:
            stats[i] = BONUS_MAX_STAT

    return name, age, job, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], move

def load_names(file_name, purpose):
    '''
    Loads names from a .txt file and
    returns a list of those names
    
    Arguments:
        file_name {str} -- .txt file with each name on its own line
        purpose {str} -- either 'f' or 'l'
    
    Raises:
        ValueError: If invalid purpose given or 
        file_name is not a text file
    
    Returns:
        names {list} -- elements are strings (names)
    '''
    if not file_name.endswith('.txt'):
        raise ValueError('Error, file must be a text file')

    names = []
    counter = 0
    
    file = open(file_name, 'r')

    # Add each name to the names list
    for name in file:
        names.append(name.rstrip())
        counter += 1
    
    # Names counter
    if purpose == 'f':
        print(counter, 'first names loaded.')
    elif purpose == 'l':
        print(counter, 'last names loaded.')
    else:
        raise ValueError("Invalid purpose argument. Valid purpose arguments: 'f', 'l'")
    
    file.close()

    return names

def guide(user):
    '''
    Opens the game's guide.

    Returns:
        {NoneType}
    '''
    print_header('g', user)
    print('GUIDE')

    guide = True
    while guide:
        print('Choose a section of the guide to read:')
        print('\t(1) Gameplay')
        print('\t(2) Player Information')
        
        command = get_command(['1', '2', 's', 'l', 'b', 'x'])

        if command == '1':
            gameplay = True
        elif command == '2':
            player_info = True
        elif command == 's':
            return SAVE
        elif command == 'l':
            return LOGOUT
        elif command == 'b' or command == 'x':
            break
        
        while gameplay:
            pass
            break
        
        while player_info:
            print()
            print('[Guide / Player Information]')
            print('Choose a section of PLAYER INFORMATION to read:')
            print('\t(1) Identity')
            print('\t(2) Statistics')
            print('\t(3) Status')
            print('\t(4) Other')

            command = get_command(['1', '2', '3', '4', 's', 'l', 'b', 'x'])

            # Player Info/Identity
            if command == '1':
                player_info_identity = True
                while player_info_identity:
                    break
            # Player Info/Statistics
            elif command == '2':
                player_info_stats = True
                while player_info_stats:
                    print()
                    print('[Guide / Player Information / Statistics')
                    print('Every player (character inside of the game) has 7 player statistics that range from 0 to 20:', end='\n\n')
                    
                    print('1. [str] Strength - The physical strength of the player, which affects damage output. Each point in strength gives ______.')
                    print('2. [skl] Skill - The skill of the player, which affects accuracy rates when using weapons. Each point in skill gives _____.')
                    print('3. [spd] Speed - The speed of the player, which affects the amount of times the player can strike an opponent. Each point in speed gives _____.')
                    print('4. [def] Defense - The defense of the player, which reduces damage taken from enemy attacks. Each point in defense reduces damage taken by 0.5 HP.')
                    print('5. [int] Intellect - The intellect of the player, which affects intelligence-related tasks. Each point in intellect gives ______.')
                    print('6. [ppl] People Skills - The people skills of the player, which affects interactions with other characters in the game. Each point in people skills gives _____.')
                    print('7. [luk] Luck - The luck of the player, which boosts all of the other stats. Each point in luck gives _____.', end='\n\n')

                    print("Statistics may be affected positively or negatively by the player's job or status.")

                    command = get_command(['s', 'l', 'b', 'x'])

                    if command == 's':
                        return SAVE
                    elif command == 'l':
                        return LOGOUT
                    elif command == 'b':
                        break
                    elif command == 'x':
                        player_info = False
                        guide = False
                        break
            # Player Info/Status
            elif command == '3':
                player_info_status = True
                while player_info_status:
                    break
            # Player Info/Other
            elif command == '4':
                player_info_other = True
                while player_info_other:
                    break
            elif command == 's':
                return SAVE
            elif command == 'l':
                return LOGOUT
            elif command == 'b':
                guide = False
                break




def print_credits():
    '''
    Prints the program's credits if the
    user wants to view them.

    Returns:
        {NoneType}
    '''
    # Ask user if they want to view the credits
    print('Would you like to view the credits?')
    print('\t(Y) Yes')
    print('\t(N) No')

    wants_credits = get_command(['y', 'n'])
    if wants_credits == 'y':
        wants_credits = True
    else:
        wants_credits = False

    # Prints credits if user said yes, otherwise skip to exit
    if wants_credits:
        sleep(1)

        print('Author: Rebecca Dang')
        print('Version: ' + str(VERSION), end='\n\n')
        sleep(1)

        print('Language: Python 3')
        print('Text Editor: Visual Studio Code', end='\n\n')
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

def save(player, user):
    pass

def view_map(player, user):
    pass

def view_player_stats(player, user):
    pass

def view_inventory(player, user):
    pass
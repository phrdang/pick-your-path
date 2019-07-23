import random as r
from time import sleep
from getpass import getpass

import 'pyp-classes' as c
import 'pyp-funcs' as f

### NAME DATABASE CREDITS ###
'''
ENGLISH NAMES:
https://github.com/smashew/NameDatabases 

FANTASY NAMES:
https://www.mithrilandmages.com/utilities/MedievalBrowse.php?letter=A&fms=F 
'''

VERSION = 0.1

def main():
    '''
    docstr
    '''
    while True:
        logging_in = True
        while logging_in:
            user = f.login()
            if user == '$__exit__':
                print('Exiting program... ')
                f.print_credits()
                break
            else:
                logging_in = False
        if user == '$__exit__':
            break

        # Allow player to choose from different modes
        mode = f.choose_mode(user)
        if mode == 'logout':
            print('Logging out...')
        else:
            break
        
    
    # sleep(1)

    # name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move = get_player_stats(mode) 

    # player = Player(name, age, job, strength, skill, speed, defense, intellect, ppl, luck, move)

    # print(player)

    # FOR TESTING ONLY
    # save_login_info('ph.rdang', 'Hello123')
    # save_login_info('rebecca', '12345')
    # save_login_info('sasha', 'cit20')
    # reset_password('rebecca', '789')
    # user: test-user, pass: password
    # hi, 12345

main()
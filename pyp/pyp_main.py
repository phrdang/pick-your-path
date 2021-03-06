import pyp_classes as c
import pyp_funcs as f

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
        if mode == '$__logout__':
            print('Logging out...')
        else:
            player = f.create_player(mode, user)
            if player == '$__save__':
                pass # CODE THIS
            elif player == '$__logout__':
                pass # CODE THIS
            elif isinstance(player, c.Player):
                pass # CODE THIS


    # LOGIN INFO
    # save_login_info('ph.rdang', 'Hello123')
    # save_login_info('rebecca', '12345')
    # save_login_info('sasha', 'cit20')
    # reset_password('rebecca', '789')
    # test-user, password
    # hi, 12345

    # turn into functions:
    # save(), guide(), map(), view_player_stats(), inventory()

main()
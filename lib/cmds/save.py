from termcolor import colored;
class Command:
    def __init__(self,player):
        print(colored('Saving...','white'))
        player.save();
        print(colored('Saved !','grey','on_white'))
        input(colored('Press Enter to Quit.','grey'))

description = 'Saves your character.';
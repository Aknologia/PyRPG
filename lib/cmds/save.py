from termcolor import colored;
class Command:
    def __init__(self,player):
        print(colored('Saving...'+(" "*16),'grey','on_white'))
        player.save();
        print(colored('Saved !'+(' '*18),'grey','on_white'))
        input(colored('Press Enter to Quit.','grey'))

description = 'Saves your character.';
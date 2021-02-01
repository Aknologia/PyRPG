from termcolor import colored;
class Command:
    def __init__(self,player):
        player = player.get();
        print(f"""\033[1;34;40m\033[4mName:\033[0m \033[1;37;40m{player["name"]}\033[0;37;40m""")
        input(colored('Press Enter to Quit.','grey'))

description = 'Shows informations about your character.';
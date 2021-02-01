from termcolor import colored;
imported = True
class Command:
    def __init__(self,player):
        self.config();
        player = player.get();
        print(f"""\033[1;34;40m\033[4mName:\033[0m \033[1;37;40m{player["name"]}\033[0;37;40m""")
        input(colored('Press Enter to Quit.','grey'))

    def config(self):
        self.description = 'Shows informations about your character.';
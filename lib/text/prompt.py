from termcolor import colored
message = colored("Type 'help' to see all available commands.",'cyan');
import os
from importlib import import_module

class prompt:
    def __init__(self,player):
        while True:
            os.system('cls');
            self.show();
            _in = input(colored('>>> ','grey')+'\033[1;37;40m');
            print('\033[0;37;40m',end='')
            try:
                os.system('cls');
                if(_in=="help"): Help(player);
                else: commands[_in].Command(player);
            except: pass;

    
    def show(self):
        print(message);

class Help:
    def __init__(self,player):
        print(colored(("="*30) + ' HELP '+ ("="*30), "grey", "on_white")+"\n");
        for command in commands:
            print(colored(command,'green') + f' - \033[1;37;40m{commands[command].description}\033[0;37;40m')
        input(colored('Press Enter to Quit.','grey'))
commands = {}

for file in os.listdir('./lib/cmds/'):
    name = file.replace('.py','');
    mod = import_module(f'lib.cmds.{name}')
    commands[name] = mod
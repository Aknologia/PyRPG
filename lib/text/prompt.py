from termcolor import colored
message = colored("Type 'help' to see all available commands.",'cyan');
import os
from importlib import import_module
from .. import utils

class prompt:
    def __init__(self,player):
        while True:
            utils.clear()
            self.show();
            _in = input(colored('>>> ','grey')+'\033[1;37;40m');
            print('\033[0;37;40m',end='')
            try:
                utils.clear();
                if(_in=="help"): Help(player);
                else: commands[_in].Command(player);
            except KeyError: 
                input(colored(f"Unknown Command '{_in}'.",'red'))

    
    def show(self):
        print(message);

class Help:
    def __init__(self,player):
        print(colored(("="*30) + ' HELP '+ ("="*30), "grey", "on_white")+"\n");
        for command in commands:
            print(colored(command,'green') + f' - \033[1;37;40m{commands[command].description}\033[0;37;40m')
        input(colored('Press Enter to Quit.','grey'))
commands = {}
try:
    for file in os.listdir('./lib/cmds/'):
        name = file.replace('.py','');
        mod = import_module(f'lib.cmds.{name}')
        commands[name] = mod
except: pass
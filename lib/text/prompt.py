from termcolor import colored
message = colored("Type 'help' to see all available commands.",'cyan');
import os
import shutil
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
                commands[_in](player);
            except: pass;

    
    def show(self):
        print(message);
commands = {}

for file in os.listdir('./lib/cmds/'):
    name = file.replace('.py','');
    mod = import_module(f'lib.cmds.{name}')
    try:
        mod.imported
        commands[name] = mod.Command
    except:
        try:
            shutil.rmtree('./lib/cmds/__pycache__')
            mod = import_module(f'lib.cmds.{name}')
            commands[name] = mod.Command
        except: pass
    
    
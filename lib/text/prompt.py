#Import Lib
from termcolor import colored
import os
from importlib import import_module
from .. import utils
#Constants
message = "Type 'help' to see all available commands.";

wasShown = False;
#Main Class
class prompt:
    def __init__(self,player):
        global wasShown;
        while True:
            if not wasShown:
              utils.clear()
              self.show();
            _in = input('>>> ');
            try:
                if(not _in or _in.isspace()): wasShown = True;
                elif(_in=="help"):
                  utils.clear();
                  Help(player); 
                  wasShown = False;
                else:
                  utils.clear();
                  commands[_in].Command(player);
                  wasShown = False;
            except KeyError: 
                input(f"\033[31mUnknown Command '{_in}'.\033[0m")

    
    def show(self):
        print(message);

#Subclass
class Help:
    def __init__(self,player):
        print(("="*30) + ' HELP '+ ("="*30) + "\n");
        for command in commands:
            print(command + f' - {commands[command].description}')
        input('\nPress Enter to Quit.')

#Load Commands
commands = {}
for file in os.listdir('./lib/cmds/'):
    name = file.replace('.py','');
    mod = import_module(f'lib.cmds.{name}')
    commands[name] = mod
from .. import info
from termcolor import colored, cprint
from .. import utils
from ..player import init
import os

class TitleScreen:
        def __init__(self):
                answer = None
                while not answer:
                        self.show();
                        try:
                                _in = int(input(">>> "))
                                if(_in<=4 and _in>0 if utils.isSaved() else _in>1): answer = _in
                                else: os.system('cls');
                        except:
                                os.system('cls');
                if(answer==4): exit();
                elif(answer==2): self.returns = init.Player();
                elif(answer==1): self.returns = utils.loadPlayer();
                os.system('cls');
        def show(self):
                self.header()
                self.menu(utils.isSaved())
        def header(self):
                _list = logo.split('\n')
                for i in range(len(_list)):
                        if not i+1==len(_list): cprint("\033[01m"+_list[i],"grey",'on_white');
                        else: print("\033[01m"+colored(_list[i],"grey","on_white")+colored(f"v{info.version}","white","on_red"))
        def menu(self, isSaved):
                print(f"""\n{colored('  [1] Continue',None if isSaved else "grey")}
  [2] New Game
  [3] Settings
  [4] Quit\n""")


logo="""                  _____       _____  _____   _____                 
                 |  __ \     |  __ \|  __ \ / ____|                
                 | |__) |   _| |__) | |__) | |  __                 
                 |  ___/ | | |  _  /|  ___/| | |_ |                
                 | |   | |_| | | \ \| |    | |__| |                
                 |_|    \__, |_|  \_\_|     \_____|                
                         __/ |                                     
                        |___/                                """

player = TitleScreen().returns;
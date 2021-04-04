from .. import info
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
                                else: utils.clear();
                        except:
                                utils.clear();
                if(answer==4): exit();
                elif(answer==2): self.returns = init.Player();
                elif(answer==1): self.returns = utils.loadPlayer();
                utils.clear();
        def show(self):
                self.header()
                self.menu(utils.isSaved())
        def header(self):
                _list = logo.split('\n')
                for i in range(len(_list)):
                        if not i+1==len(_list): print(_list[i]);
                        else: print(_list[i]+f"v{info.version}")
        def menu(self, isSaved):
                print(f"""\n{"  [1] Continue" if utils.isSaved() else ""}
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
from os import path
def isSaved():
    if path.exists('./lib/player/save.save') and not open('./lib/player/save.save','r').read().isspace():
        return True
    return False

from .player import init
def loadPlayer():
    _in = open('./lib/player/save.save','r').read();
    _in = _in.split('\n');
    return init.Player({
        "name": _in[0]
    });

#Delete __pycache__
import shutil
folders = ['./lib/cmds/__pycache__','./lib/text/__pycache__','./lib/player/__pycache__','./lib/__pycache__']
def delPycache():
    for folder in folders:
        if(path.isdir(folder)):
            try:
                shutil.rmtree(folder);
            except: pass
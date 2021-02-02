from os import path
def isSaved():
    if path.exists('./lib/player/save.save') and not open('./lib/player/save.save','r').read().isspace():
        return True
    return False

from .player import init
import base64; import json
def loadPlayer():
    _in = base64.b64decode(open('./lib/player/save.save','r').read().encode('ascii')).decode('ascii');
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

import subprocess
def clear():
    try:
        subprocess.run(['cls'], check=True, shell=True)
    except subprocess.CalledProcessError:
        subprocess.run(['clear'])

def encode(obj):
    return base64.b64encode(str(obj).encode('ascii')).decode('ascii');
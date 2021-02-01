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

def savePlayer(player):
    out = open('./lib/player/save.save','w');
    out.write(f"""{player['name']}""")
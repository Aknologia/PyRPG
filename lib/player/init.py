import os
import json
from .. import utils

class Player:
  def __init__(self, obj=None):
    if(not obj):
      os.system('cls');
      #Input Player Variables
      while True:
        name = input('Name: ');
        if(len(name) > 25): input("Player Names can't be longer than 25 characters.")
        else: break
        os.system('cls');
        file = open('lib/player/blank.json');
      self.obj = json.load(file);
    else:
      self.obj = obj;
  
  def get(self):
    return self.obj;
  
  def save(self):
    player = self.get();
    out = open('./lib/player/save.save','w');
    out.write(utils.encode(json.dumps(player)));

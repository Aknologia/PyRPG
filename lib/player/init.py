import os
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
      
      #Add them to self
      self.name = name
    else:
      self.name = obj['name']
  
  def get(self):
    return {
      "name": self.name,
    }
  
  def save(self):
    player = self.get();
    out = open('./lib/player/save.save','w');
    out.write(f"""{player['name']}""")

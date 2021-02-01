class Player:
  def __init__(self):
    #Input Player Variables
    while True:
      name = input('Name: ');
      if(len(name) > 25): input("Player Names can't be longer than 25 characters.")
      else: break
    
    #Add them to self
    self.name = name
  
  def get(self):
    return {
      "name": self.name,
    }

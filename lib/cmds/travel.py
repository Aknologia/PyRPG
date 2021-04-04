class Command:
  def __init__(self,player):
      player = player.get();
      print(f"you are at {player['location']}")
      def canTravel() :
        if player['city'] == 1:
          return True
      if canTravel :
        w = input("Do you want to travel to next world ?\n")
        if w == "yes" :
          player['location']['world'] += 1
          player['location']['city'] = 1
          print(player['location'])
      else :
        c = input("Do you want to travel to the next city ?")

description = "Travel to an already discovered zone"
from termcolor import colored;
class Command:
    def __init__(self,player):
        player = player.get();
        try:
            player['inv']
            if not len(player['inv'])>0: raise KeyError;
        except KeyError:
            print(colored(("="*28) + ' INVENTORY '+ ("="*28), "grey", "on_white")+"\n");
            print(colored('-  Empty\n','cyan'))
            input(colored('Press Enter to Quit.','grey'))

description = 'Shows your current inventory.';
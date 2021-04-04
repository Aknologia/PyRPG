def stats(obj):
    _list = [];
    for i in obj['stats']:
        val = obj['stats'][i];
        _list.append(f"- {val['name']+':'} {val['value']}")
    return '\n'.join(_list);


class Command:
    def __init__(self,player):
        player = player.get();
        print(f"""Name: {player["name"]}
Level: {player['level']}
XP: {f"{player['xp']['current']}/{player['xp']['required']}"}
Gold: {player['gold']}
Location: world {player['location']['world']}
          city {player['location']['city']}
Stats:
{stats(player)}""");
        input('Press Enter to Quit.')

description = 'Shows informations about your character.';
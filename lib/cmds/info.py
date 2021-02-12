from termcolor import colored;

def sub(strs):
    return f"\033[1;34;40m\033[4m{strs}\033[0m";
def val(strs):
    return f"\033[1;37;40m{strs}\033[0;37;40m";
def stats(obj):
    _list = [];
    for i in obj['stats']:
        val = obj['stats'][i];
        _list.append(f"\033[1;37;40m-\033[0;37;40m {colored(val['name']+':','green')} {colored(val['value'],'blue')}")
    return '\n'.join(_list);


class Command:
    def __init__(self,player):
        player = player.get();
        print(f"""{sub('Name:')} {val(player["name"])}
{sub('Level:')} {val(player['level'])}
{sub('XP:')} {val(f"{player['xp']['current']}/{player['xp']['required']}")}
{sub('Gold:')} {val(player['gold'])}
{sub('Stats:')}
{stats(player)}""");
        input(colored('Press Enter to Quit.','grey'))

description = 'Shows informations about your character.';
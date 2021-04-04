"""
MIT License
Copyright (c) 2021 Aknologia

@git https://github.com/Aknologia/PyRPG
@issues https://github.com/Aknologia/PyRPG/issues
"""

#Import Modules
import lib.utils as utils

#Clear pycache
utils.delPycache();

#Title Screen & Character Initialization
from lib.text.title import player
#Load Worlds
import lib.world.load
#Start Command Prompt
import lib.text.prompt as mod_prompt
player = mod_prompt.prompt(player);
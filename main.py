"""
MIT License
Copyright (c) 2021 Aknologia

@git https://github.com/Aknologia/PyRPG
@issues https://github.com/Aknologia/PyRPG/issues
"""

#Import Modules
from termcolor import colored
import lib.info as info
import lib.utils as utils

#Title Screen & Character Initialization
from lib.text.title import player
#Start Command Prompt
import lib.text.prompt as mod_prompt
player = mod_prompt.prompt(player);


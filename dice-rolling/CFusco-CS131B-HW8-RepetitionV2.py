"""
Author: Chad Fusco
Description: A program that simulates throwing a 9-sided die and a 9000-sided die, 100 times each, and indicates how many times the sum of the results was a multiple of three.
As a bonus feature, the program allows the user to optionally pass the number of desired dice rolls as a command line argument. The program defaults to 100 rolls.
Last updated: 2022-04-02
"""

import random, sys

# OPTIONAL: Script can accept a user-supplied number of rolls. Otherwise, defaults to 100.
dieRolls = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 100

print("A 9-sided die and a 9000-sided die was each thrown", "{:,}".format(dieRolls),\
    "times.\nThe sum of the roll pairs was a multiple of three",\
    "{:,}".format(list(map(lambda x,y:(x+y)%3,\
    # Roll a 9-sided die 100 times and keep the results in a list
    random.choices(list(range(1,10)),k=dieRolls),\
    # Roll a 9000-sided die 100 times and keep the results in a list
    random.choices(list(range(1,9001)),k=dieRolls)\
    )).count(0)),"times")

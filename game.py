# this file should run a riddle guessing game

from helpers import *

all_trivias = get_all_riddles()   

for trivia in all_trivias:
    print(f"--Trivia #{trivia['id']}")



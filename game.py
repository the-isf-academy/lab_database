import sqlite3
from helpers import *

all_trivias = get_all_trivia()   

for trivia in all_trivias:
    print(f"--Trivia #{trivia['id']}")



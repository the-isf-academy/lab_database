# this function creates the database file 
# and inserts 100 riddles

import sqlite3
import json
import random

# connect to database
connection = sqlite3.connect('database.db')

# open songs.sql 
with open('riddles.sql') as file:
    connection.executescript(file.read())

# create connection to database
conn = connection.cursor()

# create new questions in the database
# Open and read the JSON file
with open('riddles.json', 'r') as file:
    riddles = json.load(file)
    
for riddle in riddles:
    total_guesses = random.randint(10,50)
    correct_guesses = random.randint(0,total_guesses)
    conn.execute(
        """
        INSERT INTO riddles (question, answer, total_guesses, correct_guesses)
        VALUES (?, ?, ?, ?)
        """,
        (riddle['question'], riddle['answer'], total_guesses, correct_guesses)
    )

# save new questions to database
connection.commit()

# close database
connection.close()

print("-- database initalized --")
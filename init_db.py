# this function creates the database file 
# and inserts 100 riddles

import sqlite3
import json

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
    conn.execute(
        """
        INSERT INTO riddles (question, answer)
        VALUES (?, ?)
        """,
        (riddle['question'], riddle['answer'])
    )

# save new questions to database
connection.commit()

# close database
connection.close()

print("-- database initalized --")
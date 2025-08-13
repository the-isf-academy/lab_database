# this file has helper functions 
# each function connects to the database and runs sql commands

import sqlite3

def get_all_riddles():
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    # get all Questions from database
    all_riddles = conn.execute(
        """
        SELECT *
        FROM riddles
        """).fetchall()  
    
    conn.close()

    return all_riddles

def increment_riddle_column(column, id):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    conn.execute(
        f"""UPDATE riddles 
        SET {column} = {column} + 1 
        WHERE id = ?""",(id,)
    )

    conn.commit()
    conn.close()


if __name__=="__main__":
    # -- run python helpers.py to test your helper functions
    # use comments to test section by section 

    # gets all Riddles from db and prints each ID and question
    all_riddles = get_all_riddles()
    for riddle in all_riddles:
        print(riddle['id'], riddle['question'])

    # increments the total_guesses for Riddle #3 (experiment with changing the number)
    increment_row_value('total_guesses', 3)


    

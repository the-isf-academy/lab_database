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

def increment_row_value(column, id):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    conn.execute(
            f"""
            UPDATE songs 
            SET {column} = {column} + 1 
            WHERE id = {id}"""
        )
    
    conn.commit()
    conn.close()

def get_random_riddles(num_riddles):
    conn = sqlite3.connect('database.db') # connect to database
    conn.row_factory = sqlite3.Row  #converts row to dictionary object

    ranodm_riddles = conn.execute(
            f"""
            SELECT *
            from riddles
            ORDER BY random()
            limit {num_riddles}"""
        ).fetchall() 
    
    conn.close()

    return ranodm_riddles


if __name__=="__main__":
    # -- testing helper SQL functions

    all_riddles = get_all_riddles()
    for riddle in all_riddles:
        print(riddle['id'], riddle['question'])

    

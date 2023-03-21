import sqlite3

conn = sqlite3.connect('F1-2023.db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS bets
          ([question_id] INTEGER, [player_id] TEXT, [grand_prix_id] INT, [answer] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS players
          ([player_id] INTEGER PRIMARY KEY, [name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS grand_prix
          ([grand_prix_id] INTEGER PRIMARY KEY, [name] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS questions
          ([question_id] INTEGER PRIMARY KEY, [text] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS ground_truth
          ([grand_prix_id] INTEGER , [question_id] TEXT, [correct_ans] TEXT)
          ''')
                    
conn.commit()
conn.close()


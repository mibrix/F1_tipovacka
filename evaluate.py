import pandas as pd
import sqlite3

player_names = ["Wonde", "Tome", "Hrici", "Kajlo", "Sasu", "OG"]
file_name = r'Tipovačka F1 - Australia (odpovede)'
grand_prix_id = 3
#Bahrain
#ground_truth = ["VER", "PER", "ALO", "ZHO", "NOR", ["OCO", "LEC", "PIA"], "Nie", "Nie", "Ano", "Nie", "Ano", "Nie", "Redbull", "VER", "Redbull"]
#Jedah
#ground_truth = ["PER", "VER", "ALO", "VER", "BOT", ["STR", "ALB"], "Nie", "Ano", "Nie", "Nie", "Ano", "Nie", "Ano-Redbull", "VER", "Redbull"]
#Australia
ground_truth = ['Verstappen','Hamilton','Alonso','Perez','Sainz',['Galsy','Ocon','de Vries','Sargeant','Magnussen','Russell','Albon','Leclerc'],'Áno','Áno', 'Áno', 'Áno', 'Áno', 'Nie', 'nie','Verstappen','Red Bull']


df = pd.read_csv(f'{file_name}.csv')

conn = sqlite3.connect('F1-2023.db')
c = conn.cursor()

#insert players' answers into DB
for i in range(len(df['Meno'])):
    for n,ans in enumerate(df.loc[i][2:]):
        if type(ans) == str:
            #print(f'''{n+1}, {player_names.index(df.loc[i][1].strip())+1}, {grand_prix_id}, {ans.strip()}''')
             c.execute(f'''
                      INSERT INTO bets (question_id, player_id, grand_prix_id, answer) 
                      VALUES ({n+1}, {player_names.index(df.loc[i][1].strip())+1}, {grand_prix_id}, '{ans.strip()}')
                      ''')

#insert ground_truth into DB
for n,ans in enumerate(ground_truth):
    if type(ans) == str:
        c.execute(f'''
              INSERT INTO ground_truth (grand_prix_id, question_id, correct_ans) 
              VALUES ({grand_prix_id}, {n+1}, '{ans}')
              ''')
    elif type(ans) == list:
        for ans1 in ans:
            c.execute(f'''
              INSERT INTO ground_truth (grand_prix_id, question_id, correct_ans) 
              VALUES ({grand_prix_id}, {n+1}, '{ans1}')
              ''')

conn.commit()
conn.close()

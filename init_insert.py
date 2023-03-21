import sqlite3

conn = sqlite3.connect('F1-2023.db')
c = conn.cursor()
                   
c.execute('''
          INSERT INTO players (player_id, name)

                VALUES
                (1,'Wonde'),
                (2,'Tome'),
                (3,'Hrici'),
                (4,'Kajlo'),
                (5,'Sasu'),
                (6,'OG')
          ''')

c.execute('''
          INSERT INTO grand_prix (grand_prix_id, name)

                VALUES
                (1,'Bahrain Grand Prix'),
                (2,'Saudi Arabian Grand Prix'),
                (3,'Australian Grand Prix'),
                (4,'Azerbaijan Grand Prix'),
                (5,'Miami Grand Prix'),
                (6,'Emilia Romagna Grand Prix'),
                (7,'Monaco Grand Prix'),
                (8,'Spanish Grand Prix'),
                (9,'Canadian Grand Prix'),
                (10,'Austrian Grand Prix'),
                (11,'British Grand Prix'),
                (12,'Hungarian Grand Prix'),
                (13,'Belgian Grand Prix'),
                (14,'Dutch Grand Prix'),
                (15,'Italian Grand Prix'),
                (16,'Singapore Grand Prix'),
                (17,'Japanese Grand Prix'),
                (18,'Qatar Grand Prix'),
                (19,'United States Grand Prix'),
                (20,'Mexico City Grand Prix'),
                (21,'São Paulo Grand Prix'),
                (22,'Las Vegas Grand Prix'),
                (23,'Abu Dhabi Grand Prix')               
          ''')

c.execute('''
          INSERT INTO questions (question_id, text)

                VALUES
                (1,'Víťaz veľkej ceny (1. miesto)'),
                (2,'Runner up veľkej ceny (2. miesto)'),
                (3,'Kto skončí na treťom mieste?'),
                (4,'Najrýchlejšie kolo'),
                (5,'Posledné miesto zo všetkých ktorí dokončili veľkú cenu'),
                (6,'jazdec ktorí skončí ako DNF'),
                (7,'V závode bude červená vlajka '),
                (8,'V závode bude safety car'),
                (9,'V zavode bude VSC?'),
                (10,'V závode bude havária 2 a viacerých jazdcov'),
                (11,'Závod vyhrá ten kto štartoval z pole position (1. miesto)'),
                (12,'Bude havária na štarte'),
                (13,'Dvaja jazdci rovnakého tímu budú na pódiu (meno tímu)'),
                (14,'Jazdec s najviac bodmi po poslednom závode (meno jazdca)'),
                (15,'Tím s najviac bodmi po poslednom závode (meno tímu)')         
          ''')

conn.commit()
conn.close()

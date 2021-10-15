import sqlite3


conn = sqlite3.connect('primes')
c = conn.cursor()

# recreate tables
c.execute('DROP TABLE IF EXISTS known_phrases')
conn.commit()
c.execute('CREATE TABLE IF NOT EXISTS known_phrases ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [created] DATETIME DEFAULT CURRENT_TIMESTAMP, [description] TINYTEXT, [videoId] INTEGER)')
conn.commit()
c.execute('DROP TABLE IF EXISTS incoming_phrases')
conn.commit()
c.execute('CREATE TABLE IF NOT EXISTS incoming_phrases ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [created] DATETIME DEFAULT CURRENT_TIMESTAMP, [description] TINYTEXT, [pending] INTEGER, [videoId] INTEGER)')
conn.commit()
c.execute('DROP TABLE IF EXISTS videos')
conn.commit()
c.execute('CREATE TABLE IF NOT EXISTS videos ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [created] DATETIME DEFAULT CURRENT_TIMESTAMP, [path] TINYTEXT, [duration] INTEGER)')
conn.commit()

# populate known phrases
c.execute('''
INSERT INTO known_phrases (description, videoId) VALUES
('Γεια σας',16),
('Καλημέρα',16),
('Καλησπέρα',16),
('Καληνύχτα',19),
('Πως είσαι ;',20),
('Πως σε λένε',21),
('Που μένεις;',22),
('Τι ώρα είναι;',7),
('Δεν ξέρω',8),
('Ευχαριστώ πολύ',9),
('Παρακαλώ',10),
('Τι νέα ;',11),
('Χάρηκα για την γνωριμία',12),
('Τα λέμε',13),
('Τι θα ήθελες ;',14),
('Πότε γεννήθηκες ;',15),
('Υπάρχει φαρμακείο εδώ γύρω ;',24),
('Που πήγες ;',25),
('Τι σου αρέσει ;',26),
('Εργάζεσαι ;',27),
('Συγνώμη',28),
('Δεν υπάρχει πρόβλημα',29),
('Δώσε μου ένα λεπτό',30),
('Χρειάζομαι βοήθεια',31),
('Όχι',32),
('Ναι',33),
('Χρειάζομαι ένα γιατρό',34),
('Τι μέρα είναι ;',35),
('Μπορώ να παρκάρω εδώ ;',36),
('Που είναι ένα πρατήριο βενζίνης ;',37),
('Τι δουλειά κάνεις ;',38),
('Πόσο κοστίζει αυτό;',39),
('Θέλω να πάω στο κέντρο της πόλης.',40),
('Πότε είναι ;',41),
('Μπορώ να ανοίξω το παράθυρο ;',42),
('Δεν καταλαβαίνω',43),
('Είναι μακριά από εδώ ;',44),
('Σε πόση ώρα θα φτάσω εκεί με τα πόδια ;',45),
('Κάνει ζέστη',46),
('Κάνει κρύο',47),
('Έχω πυρετό',48),
('Έχεις αδέρφια ;',49),
('Ποιο είναι το επώνυμο σου ;',50),
('Είναι εντάξει',51),
('Είμαι καλά',2),
('Τι φύλο είσαι ;',1),
('Πεινάω και διψάω',3),
('Έχω μια ερώτηση',4),
('Δεν είμαι σίγουρος',5),
('Τι χόμπι έχεις',6)
''')
conn.commit()

# populate known phrases
c.execute('''
INSERT INTO videos (path, duration) VALUES
('1.mp4', 4),('2.mp4', 1),('3.mp4', 3),('4.mp4', 2),('5.mp4', 3),('6.mp4', 2),('7.mp4', 2),('8.mp4', 2),('9.mp4', 2),('10.mp4', 2),('11.mp4', 2),('12.mp4', 3),('13.mp4', 2),('14.mp4', 2),('15.mp4', 4),('16.mp4', 1),('17.mp4', 2),('18.mp4', 2),('19.mp4', 3),('20.mp4', 2),('21.mp4', 3),('22.mp4', 3),('23.mp4', 3),('24.mp4', 6),('25.mp4', 2),('26.mp4', 2),('27.mp4', 2),('28.mp4', 3),('29.mp4', 3),('30.mp4', 4),('31.mp4', 4),('32.mp4', 2),('33.mp4', 2),('34.mp4', 3),('35.mp4', 2),('36.mp4', 4),('37.mp4', 4),('38.mp4', 2),('39.mp4', 2),('40.mp4', 5),('41.mp4', 1),('42.mp4', 3),('43.mp4', 2),('44.mp4', 3),('45.mp4', 4),('46.mp4', 2),('47.mp4', 2),('48.mp4', 2),('49.mp4', 3),('50.mp4', 3),('51.mp4', 2)
''')
conn.commit()


c.execute('SELECT * FROM known_phrases')
data = c.fetchall()

for row in data:
    print(row)

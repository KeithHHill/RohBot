import random
import sqlite3


def nickname_check(author):
    if str(author.nick) == "None":
        name_split = str(author).split('#')
        return name_split[0]
    else:
        return author.nick


def get_gamble_modifier():
    outcome = random.randint(1, 100)
    if outcome <= 50:
        modifier = 0
    elif 50 < outcome <= 70:
        modifier = 1.5
    elif 70 < outcome <= 85:
        modifier = 2
    elif 85 < outcome <= 95:
        modifier = 2.5
    else:
        modifier = 3
    return modifier


def sqlite_setup():
    db = 'RohBotDB.db'
    conn = sqlite3.connect(db)
    print('Connected to {}.'.format(db))

    conn.execute('CREATE TABLE tbl_user(user_id TEXT PRIMARY KEY NOT NULL, user_rohcoins INT NOT NULL);')
    print("Table created.")
    conn.close()

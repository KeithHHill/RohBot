import random
import sqlite3
import requests
import time


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


def check_for_max_permissions(member, server):
    max_role = server.role_hierarchy[0]
    member_max_role = member.top_role
    if max_role == member_max_role:
        return True
    else:
        return False


def get_json(url):
    response = requests.get(url)
    json = response.json()
    return json


def get_seconds_time():
    return int(time.time())


def sqlite_setup():
    db = 'RohBotDB.db'
    conn = sqlite3.connect(db)
    print('Connected to {}.'.format(db))

    conn.execute('CREATE TABLE tbl_user_coins(user_id TEXT NOT NULL, server_id TEXT NOT NULL, user_rohcoins INT NOT NULL, PRIMARY KEY (user_id, server_id))')
    print("Table created.")
    conn.close()

import random
import sqlite3
import UtilityFunctions as UF
from collections import defaultdict

group_drink_pool_dict = defaultdict(set)


def flip_coin(author):
    side = random.randint(0, 1)
    side = 'heads' if side == 0 else 'tails'
    outcome = '{}\'s coin landed on {}.'.format(UF.nickname_check(author), side)
    print(outcome)
    return outcome


def roll_die(author):
    side = random.randint(1, 6)
    outcome = '{} rolls a {}.'.format(UF.nickname_check(author), side)
    print(outcome)
    return outcome


def in_there_dog(author):
    message = '{} is in there dog!'.format(UF.nickname_check(author))
    print(message)
    return message


def drink(author):
    if random.randint(1, 100) <= 20:
        message = '{} must drink!'.format(UF.nickname_check(author))
        print(message)
        return message
    else:
        message = '{} lucked out this time!'.format(UF.nickname_check(author))
        print(message)
        return message


def three_minutes(author):
    message = '{} has you for three minutes!'.format(UF.nickname_check(author))
    print(message)
    return message


def join_group_drink(author, message):
    channel = str(message.channel.id)
    group_drink_pool_dict[channel].add(author.id)
    message = '{} has joined the drinking pool!'.format(UF.nickname_check(author))
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def leave_group_drink(author, message):
    channel = str(message.channel.id)
    try:
        group_drink_pool_dict[channel].remove(author.id)
        message = '{} has left the drinking pool!'.format(UF.nickname_check(author))
    except Exception:
        message = '{} is not in the drinking pool!'.format(UF.nickname_check(author))
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def clear_group_drink(message):
    channel = str(message.channel.id)
    group_drink_pool_dict[channel].clear()
    message = 'The drinking pool has been cleared!'
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def group_drink(message):
    losers = []
    channel = str(message.channel.id)

    if len(group_drink_pool_dict[channel]) == 0:
        result = "There is no one in the drinking pool!"
        print(result)
        return result

    for i in group_drink_pool_dict[channel]:
        outcome = random.randint(1, 100)
        if outcome <= 20:
            losers.append(i)

    if len(losers) == 2:
        result = '{} and {} are the big losers and have to drink!' \
            .format(UF.nickname_check(message.server.get_member(losers[0])),
                    UF.nickname_check(message.server.get_member(losers[1])))
    elif len(losers) == 1:
        result = '{} is the big loser and has to drink!'.format(UF.nickname_check(message.server.get_member(losers[0])))
    elif len(losers) == 0:
        result = 'You lucky fuckers, sobriety wins again.'
    else:
        names = str()
        for i in range(len(losers)):
            if i < len(losers):
                names += UF.nickname_check(message.server.get_member(losers[i]))
                if len(losers) - 1 == i:
                    names += " "
                else:
                    names += ", "
            else:
                names = names + ", and " + UF.nickname_check(message.server.get_member(losers[0]))
        result = names + "are the big losers and have to drink!"

    print(result[:-1] + ' in {}.'.format(channel))
    return result


def get_rohcoins(author):
    author_id = author.id
    conn = sqlite3.connect('RohBotDB.db')

    args = (author_id,)
    cursor = conn.execute('SELECT exists(SELECT * FROM tbl_user WHERE user_id = ?)', args)
    user_check = cursor.fetchone()[0]
    if user_check == 0:
        starter_coins = 20
        args = (author_id, starter_coins)
        cursor = conn.execute('INSERT INTO tbl_user(user_id, user_rohcoins) VALUES (?, ?)', args)
        conn.commit()
        conn.close()
        print('New user, {}, added to database.'.format(author))
        return '{} has {} RohCoins.'.format(UF.nickname_check(author), starter_coins)
    else:
        args = (author_id,)
        cursor = conn.execute('SELECT user_rohcoins FROM tbl_user WHERE user_id = ?', args)
        coins = cursor.fetchone()[0]
        conn.close()
        print('{} has {} RohCoins.'.format(author, coins))
        return '{} has {} RohCoins.'.format(UF.nickname_check(author), coins)


def gamble(author, message):
    author_id = author.id
    conn = sqlite3.connect('RohBotDB.db')

    args = (author_id,)
    cursor = conn.execute('SELECT exists(SELECT * FROM tbl_user WHERE user_id = ?)', args)
    user_check = cursor.fetchone()[0]
    if user_check == 0:
        conn.close()
        return '{}, use the !coins command to get your starter pack of 10 RohCoins, then try again!' \
            .format(UF.nickname_check(author))
    else:
        try:
            bet = message.content.split()[1]
        except Exception:
            return 'Please put a space between gamble and your bet!'
        try:
            int(bet)
        except Exception:
            return 'You must enter an integer!'
        args = (author_id, bet)
        cursor = conn.execute('SELECT exists(SELECT * FROM tbl_user WHERE user_id = ? AND user_rohcoins >= ?)', args)
        coins_check = cursor.fetchone()[0]
        if coins_check == 0:
            conn.close()
            return '{}, you don\'t have enough RohCoins for that bet!'.format(UF.nickname_check(author))
        else:
            mod = UF.get_gamble_modifier()
            payout = int(int(bet) * mod)
            outcome = payout - int(bet)
            if payout == 0:
                args = (bet, author_id)
                cursor = conn.execute('UPDATE tbl_user SET user_rohcoins = user_rohcoins - ? WHERE user_id = ?', args)
                conn.commit()
                conn.close()
                print('{} lost {} RohCoins.'.format(author, bet))
                return '{} lost {} RohCoins!'.format(UF.nickname_check(author), bet)
            else:
                args = (outcome, author_id)
                cursor = conn.execute('UPDATE tbl_user SET user_rohcoins = user_rohcoins + ? WHERE user_id = ?', args)
                conn.commit()
                conn.close()
                print('{} gained {} RohCoins.'.format(author, outcome))
                return '{} gained {} RohCoins!'.format(UF.nickname_check(author), outcome)


def add_coins(author, message):
    conn = sqlite3.connect('RohBotDB.db')
    if UF.check_for_max_permissions(author, message.server):
        content = message.content.split()
        target = message.server.get_member_named(content[1])
        amount = int(content[2])
        args = (amount, target.id)
        cursor = conn.execute('UPDATE tbl_user SET user_rohcoins = user_rohcoins + ? WHERE user_id = ?', args)
        conn.commit()
        conn.close()
        print('{} coins have been added to {}.'.format(amount, target))
        return '{} coins have been added to {}.'.format(amount, UF.nickname_check(target))
    else:
        return 'You do not have the correct permissions for this action.'


def help_command(message):
    result = 'Commands:\n' \
             '-------------------------\n' \
             '!flip                  flips a coin\n' \
             '!roll                  rolls a 6-sided die\n' \
             '!inthere           says you\'re in there dog\n' \
             '!3min               RohBot has you for 3 minutes\n' \
             '!drink               20% chance you have to drink\n' \
             '!joinpool          adds you to the pool for group drinking\n' \
             '!leavepool       removes you from the group drinking pool\n' \
             '!clearpool        clears everyone out of the group drinking pool\n' \
             '!gdrink             everyone in the group drinking pool has 20% to drink\n' \
             '!nsfw                links random nsfw reddit thread\n' \
             '!coins               shows how many RohCoins you have\n' \
             '!gamble X       gamble X of your RohCoins'
    print('Printed !help on {}'.format(message.channel.id))
    return result

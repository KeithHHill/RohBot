import random
from collections import defaultdict

group_drink_pool_dict = defaultdict(set)


def flip_coin(author):
    side = random.randint(0, 1)
    side = 'heads' if side == 0 else 'tails'
    outcome = '{}\'s coin landed on {}.'.format(nickname_check(author), side)
    print(outcome)
    return outcome


def roll_die(author):
    side = random.randint(1, 6)
    outcome = '{} rolls a {}.'.format(nickname_check(author), side)
    print(outcome)
    return outcome


def in_there_dog(author):
    message = '{} is in there dog!'.format(nickname_check(author))
    print(message)
    return message


def drink(author):
    if random.randint(1, 100) <= 20:
        message = '{} must drink!'.format(nickname_check(author))
        print(message)
        return message
    else:
        message = '{} lucked out this time!'.format(nickname_check(author))
        print(message)
        return message


def three_minutes(author):
    message = '{} has you for three minutes!'.format(nickname_check(author))
    print(message)
    return message


def join_group_drink(author, message):
    channel = str(message.channel.id)
    group_drink_pool_dict[channel].add(author.id)
    message = '{} has joined the drinking pool!'.format(nickname_check(author))
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def leave_group_drink(author, message):
    channel = str(message.channel.id)
    try:
        group_drink_pool_dict[channel].remove(author.id)
        message = '{} has left the drinking pool!'.format(nickname_check(author))
    except Exception:
        message = '{} is not in the drinking pool!'.format(nickname_check(author))
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
            .format(nickname_check(message.server.get_member(losers[0])),
                    nickname_check(message.server.get_member(losers[1])))
    elif len(losers) == 1:
        result = '{} is the big loser and has to drink!'.format(nickname_check(message.server.get_member(losers[0])))
    elif len(losers) == 0:
        result = 'You lucky fuckers, sobriety wins again.'
    else:
        names = str()
        for i in range(len(losers)):
            if i < len(losers):
                names += nickname_check(message.server.get_member(losers[i]))
                if len(losers) - 1 == i:
                    names += " "
                else:
                    names += ", "
            else:
                names = names + ", and " + nickname_check(message.server.get_member(losers[0]))
        result = names + "are the big losers and have to drink!"

    print(result[:-1] + ' in {}.'.format(channel))
    return result


def help_command():
    result = '\n' \
             'Commands:\n' \
             '-------------------------\n' \
             '!flip                  flips a coin\n' \
             '!roll                  rolls a 6-sided die\n' \
             '!inthere           says you\'re in there dog\n' \
             '!3min               RohBot has you for 3 minutes\n' \
             '!drink               20% chance you have to drink\n' \
             '!joinpool          adds you to the pool for group drinking\n' \
             '!leavepool       removes you from the group drinking pool\n' \
             '!clearpool        clears everyone out of the group drinking pool\n' \
             '!gdrink             everyone in the group drinking pool has 20% to drink\n'
    return result


def nickname_check(author):
    if str(author.nick) == "None":
        name_split = str(author).split('#')
        return name_split[0]
    else:
        return author.nick

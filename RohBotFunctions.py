
import random
from collections import defaultdict

group_drink_pool_dict = defaultdict(set)


def flip_coin(author):
    side = random.randint(0, 1)
    side = 'heads' if side == 0 else 'tails'
    outcome = '{}\'s coin landed on {}.'.format(author.nick, side)
    print(outcome)
    return outcome


def roll_die(author):
    side = random.randint(1, 6)
    outcome = '{} rolls a {}.'.format(author.nick, side)
    print(outcome)
    return outcome


def in_there_dog(author):
    message = '{} is in there dog!'.format(author.nick)
    print(message)
    return message


def drink(author):
    if random.randint(1, 5) == 3:
        message = '{} must drink!'.format(author.nick)
        print(message)
        return message
    else:
        message = '{} lucked out this time!'.format(author.nick)
        print(message)
        return message


def three_minutes(author):
    message = '{} has you for three minutes!'.format(author.nick)
    print(message)
    return message


def join_group_drink(author, message):
    channel = str(message.channel)
    group_drink_pool_dict[channel].add(author)
    message = '{} has joined the drinking pool!'.format(author)
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def leave_group_drink(author, message):
    channel = str(message.channel)
    group_drink_pool_dict[channel].remove(author)
    message = '{} has left the drinking pool!'.format(author)
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def clear_group_drink(message):
    channel = str(message.channel)
    group_drink_pool_dict[channel].clear()
    message = 'The drinking pool has been cleared!'
    print(message[:-1] + ' in {}.'.format(channel))
    return message


def group_drink(message):
    losers = []
    channel = str(message.channel)
    if len(group_drink_pool_dict[channel]) == 0:
        result = "There is no one in the drinking pool!"
        print(result)
        return result
    for i in group_drink_pool_dict[channel]:
        outcome = random.randint(1, 5)
        if outcome == 3:
            losers.append(str(i))
    if len(losers) == 0:
        result = 'You lucky fuckers, sobriety wins again.'
        print(result)
        return result
    names = str()
    for i in range(len(losers)):
        if len(losers) == 1:
            names = str(losers[i])
        elif i < len(losers):
            names += str(losers[i])
            if len(losers) - 1 == i:
                names += " "
            else:
                names += ", "
        else:
            names = names + "and " + str(losers[i])
    result = names + "are the big losers and have to drink!"
    if len(losers) == 1:
        result = names + " is the big loser and has to drink!"
    print(result)
    return result

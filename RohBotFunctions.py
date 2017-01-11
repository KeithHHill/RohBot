import random

drink_rigged = set()
group_drink_pool = set()


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
    if str(author) in drink_rigged:
        message = '{} must drink!'.format(author.nick)
        print(message)
        return message
    elif random.randint(1, 5) == 3:
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


def add_drink_rigged(author, message):
    temp_roles = [x.name for x in author.roles]
    if 'Super Admin' in temp_roles:
        message = message.content.split()
        drink_rigged.add(message[1])
        print('Added {} to the rigged list.'.format(message[1]))


def remove_drink_rigged(author, message):
    temp_roles = [x.name for x in author.roles]
    if 'Super Admin' in temp_roles:
        message = message.content.split()
        drink_rigged.remove(message[1])
        print('Removed {} from the rigged list.'.format(message[1]))


def join_group_drink(author):
    group_drink_pool.add(author)
    message = '{} has joined the drinking pool!'.format(author)
    print(message)
    return message


def leave_group_drink(author):
    message = '{} has left the drinking pool!'.format(author)
    print(message)
    return message


def clear_group_drink():
    message = 'The drinking pool has been cleared'
    print(message)
    return message


def group_drink():
    losers = []
    for i in group_drink_pool:
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

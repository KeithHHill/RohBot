import discord
import RohBotConstants
import RohBotFunctions as RBF
import UtilityFunctions as UF

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    # UF.sqlite_setup()  # only run this on first startup


@client.event
async def on_message(message):
    author = message.author

    if message.content.startswith('!help'):
        await client.send_message(message.channel, RBF.help_command(message))
    elif message.content.startswith('!flip'):
        await client.send_message(message.channel, RBF.flip_coin(author))
    elif message.content.startswith('!roll'):
        await client.send_message(message.channel, RBF.roll_die(author))
    elif message.content.startswith('!inthere'):
        await client.send_message(message.channel, RBF.in_there_dog(author))
    elif message.content.startswith('!drink'):
        await client.send_message(message.channel, RBF.drink(author))
    elif message.content.startswith('!3min'):
        await client.send_message(message.channel, RBF.three_minutes(author))
    elif message.content.startswith('!joinpool'):
        await client.send_message(message.channel, RBF.join_group_drink(author, message))
    elif message.content.startswith('!leavepool'):
        await client.send_message(message.channel, RBF.leave_group_drink(author, message))
    elif message.content.startswith('!clearpool'):
        await client.send_message(message.channel, RBF.clear_group_drink(message))
    elif message.content.startswith('!gdrink'):
        await client.send_message(message.channel, RBF.group_drink(message))
    elif message.content.startswith('!nsfw'):
        await client.send_message(message.channel, '<https://www.reddit.com/r/randnsfw>')
    elif message.content.startswith('!coins'):
        await client.send_message(message.channel, RBF.get_rohcoins(author, message))
    elif message.content.startswith('!gamble'):
        await client.send_message(message.channel, RBF.gamble(author, message))
    elif message.content.startswith('!addcoin'):
        await client.send_message(message.channel, RBF.add_coins(author, message))


client.run(RohBotConstants.PRODUCTION_SECRET_KEY)

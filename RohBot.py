import discord

import DiscordBotKey
import RohBotFunctions as RBF

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------')


@client.event
async def on_message(message):
    author = message.author

    if message.content.startswith('!help'):
        await client.send_message(message.channel, RBF.help_command())
    elif message.content.startswith('!flip'):
        await client.send_message(message.channel, RBF.flip_coin(author))
    elif message.content.startswith('!roll'):
        await client.send_message(message.channel, RBF.roll_die(author))
    elif message.content.startswith('!inthere'):
        await client.send_message(message.channel, RBF.in_there_dog(author), tts=True)
    elif message.content.startswith('!drink'):
        await client.send_message(message.channel, RBF.drink(author), tts=True)
    elif message.content.startswith('!3min'):
        await client.send_message(message.channel, RBF.three_minutes(author), tts=True)
    elif message.content.startswith('!joinpool'):
        await client.send_message(message.channel, RBF.join_group_drink(author, message))
    elif message.content.startswith('!leavepool'):
        await client.send_message(message.channel, RBF.leave_group_drink(author, message))
    elif message.content.startswith('!clearpool'):
        await client.send_message(message.channel, RBF.clear_group_drink(message))
    elif message.content.startswith('!gdrink'):
        await client.send_message(message.channel, RBF.group_drink(message), tts=True)


client.run(DiscordBotKey.KEY)

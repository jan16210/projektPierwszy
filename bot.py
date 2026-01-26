import discord
import random
from discord.ext import commands
animals = ["Dog", "Cat", "Mouse", "Fish", "Bird", "Lizard", "Hamster"]




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command(commands.has_permissions(administrator=True))
async def hello(ctx):
    await ctx.send('Hello!') 
@bot.command()
async def who(ctx):
    await ctx.send('Hi')
@bot.command()
async def animals(ctx):
    await ctx.send(f'Available animals: {", ".join(animals)}')
@bot.command()
async def random_animal(ctx, chosen_animal):
    computer_animal = random.choice(animals)
    print(f"Computer chose: {computer_animal}")
    await ctx.send(f'Your random animal is: {chosen_animal}, computer chose: {computer_animal}')
@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return
    print(message.content)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("who"):
        await message.channel.send("Hi")

    if message.content.startswith("animals"):
        print(animals)
        await message.channel.send(f'Available animals: {", ".join(animals)}')
    if message.content.startswith("random animal"):

        chosen_animal = message.content.split(" ")[2]
        computer_animal = random.choice(animals)
        print(f"Computer chose: {computer_animal}")
        await message.channel.send(f'Your random animal is: {chosen_animal + ", computer chose: " + computer_animal}')

bot.run("MTQ2Mjg0NzMxODIwOTQ2MjQxNg.GTr-s_.QozUt4QQQ0jMZFNWVeD0UkbWBjEMfoBCEC-CKA")
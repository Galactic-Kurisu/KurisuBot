#pip install discord.py (make sure to do that)

import wikipedia
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def greet(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@client.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Invalid format. Please use the format `XdY`.')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@client.command()
async def flip(ctx):
    coin = ['Heads', 'Tails']
    await ctx.send(f'{ctx.author.mention} flipped a coin and got {random.choice(coin)}!')

@client.command()
async def choose(ctx, *choices: str):
    await ctx.send(f'{ctx.author.mention} chose {random.choice(choices)}!')

@client.command()
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send(data['file'])

@client.command()
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.send(data['message'])

@client.command()
async def weather(ctx, *, city: str):
    api_key = 'your_api_key_here'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city

@client.command()
async def urban(ctx, *, word: str):
    url = f'https://api.urbandictionary.com/v0/define?term={word}'
    response = requests.get(url)
    data = response.json()
    if len(data['list']) == 0:
        await ctx.send(f'Sorry, I could not find a definition for {word}.')
    else:
        definition = data['list'][0]['definition']
        example = data['list'][0]['example']
        await ctx.send(f'**{word}:**
{definition}

**Example:**
{example}')

@client.command()
async def joke(ctx):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    await ctx.send(f'{data["setup"]}

{data["punchline"]}')

@client.command()
async def quote(ctx):
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    await ctx.send(f'"{data["content"]}" - {data["author"]}')

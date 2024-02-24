import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
items = ('стекло', 'бумага', 'пластик')
items_time = ('1000 лет', '1,5 месяца', '200 лет')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!\n Я умею рассказывать, сколько разлагается тот или иной бытовой предмет.')

@bot.command()
async def list(ctx):
    items_str = ''
    for i in items:
        items_str += i
        items_str += '\n'
    await ctx.send(f'Список бытовых предметов, которые я знаю:\n{items_str}')

@bot.command()
async def time(ctx, item: str):
    if items.count(item):
       time_str = items_time[items.index(item)]
    else:
        await ctx.send(f'Элемент отсутствует в списке!')
    await ctx.send(f'Вот сколько разлагается этот бытовой предмет:\n{time_str}')

@bot.command()
async def helper(ctx):
    await ctx.send(f'Вот какие команды я умею выполнять:\n!hello - приветствие \n!helper - помощь - то, что ты сейчас читаешь \n!list - список бытовых предметов, которые я знаю \n!time (название предмета) - выводит время разложения введённого бытового предмета')

bot.run("MTIwMjYyNzk4MzA0NzkyMTY4NQ.GanG4s.YKals6v7a2RBwphPUXt5MLofzBxXMkT9u9gxsA") 
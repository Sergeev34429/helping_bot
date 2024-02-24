import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
items = ('стекло', 'бумага', 'пластик', 'пищевые отходы', 'картон', 'дерево', 'окурки', 'резиновые покрышки', 'алюминий', 'фольга')
items_time = ('1000 лет!!', '1,5 месяца', '200 лет', 'от 2 недель', '2 месяца', 'до 3 лет', 'до 5 лет', '40 лет', 'до 500 лет', '100 лет')

@bot.event
async def on_ready():
    print(f'Мы вошли в систему к {bot.user}.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!\nЯ умею рассказывать, сколько разлагается тот или иной бытовой предмет.\n(я не хочу это делать)')

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

bot.run("1MTIwMjYyNzk4MzA0NzkyMTY4NQ.G79K-T.jWalv-qtFehWmlNq1SqaPVHFs4m11mwC9p65PM") 
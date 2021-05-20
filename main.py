import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from keep_alive import keep_alive
import os, asyncio
from random import choice

presence= [
  discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
  discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'ch! '")),
  discord.Activity(type=discord.ActivityType.playing, name=("with Luminette")),
  discord.Activity(type=discord.ActivityType.competing, name=("with Paidoru >:(")),
  discord.Activity(type=discord.ActivityType.watching, name=("Luminette ❤️")),
  discord.Activity(type=discord.ActivityType.playing, name=("minet bucin sm mayo")),
  discord.Activity(type=discord.ActivityType.watching, name=("Primordial World"))
]

PREFIX = [
  "Ch! ",
  "Ch!",
  "ch! ",
  "ch!",
  "+ ",
  "+"
]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="__*Childe's commands:*__", description="Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n🧡 Develop by: `Luminette#9466`, `Potatish#0666`\n<:PaimonHehe:843373207130079232> The next generation of __Paidoru__ (`Paimon#7192`) by `Nawaytes~#2470`\n‎‎‎", colour=discord.Color.orange())
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
    embed.add_field(name="<:Chchibi:843379361138737182>__Bot's invitation link:__<:Chchibi:843379361138737182>", value="https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot\n*as Administrator*\n\n***List of Commands:***", inline=False)
    embed.add_field(name='__Help Commands__', value="on development, teehee", inline=False)
    embed.add_field(name='__Support us ❤️__', value="<https://ko-fi.com/childe_bot>", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ownerhelp(ctx):
    embed=discord.Embed(title="__Hello, Luminette 🧡__", description="My Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨", colour=discord.Color.orange())
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
    embed.add_field(name="__Your to do list on me:__", value="Fix the help command: add those `fun` command, fix the TUI\nAdd `1 piece tiara sets`\nFix weapons.json\n\n", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    channel = bot.get_channel(841614719562285086)
    await channel.send('Rebooting')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
    print('Childe is online.')
@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send(f'Command not found! Use `+help` for the list of commands!')
            return
        if isinstance(error, commands.CheckFailure):
            return
        if isinstance(error, commands.ChannelNotFound):
            await ctx.send(f'Channel not found!', delete_after=7)
            return
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Member not found!', delete_after=7)
            return
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'Error :(', delete_after=7)
            return
        raise error
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"Looks like you don't have the permission 👀")
@bot.event
async def on_member_join(member):
    if member.guild.id == 786492151058923520:
      channel = bot.get_channel(794844425956229120)
      await channel.send("Welcome, {} :heart:".format (member.mention))
    elif member.guild.id == 271215379311886336:
      channel = bot.get_channel(834013759516573707)
      await channel.send("Welcome, {} :heart:".format (member.mention)) 
    else:
      return
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hi, {0.author.mention} !'.format(message))
        await bot.process_commands(message)
    if message.content.lower().startswith('childe?'):
        await message.channel.send('Hey girlie, hold still')
        await bot.process_commands(message)
@bot.event
async def on_command(ctx):
    channel = bot.get_channel(841906846389764146)
    await channel.send(f"\n{ctx.author.name} used a command!\n`{ctx.message.content}`")

@bot.command()
async def servers(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
        await ctx.send("__**Childe's active servers:**__")
        activeservers = bot.guilds
        for guild in activeservers:
            await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\n ––––––––––––––––––––––––––––––')

@bot.command()
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@tasks.loop(minutes=5)
async def presence_change():
    await asyncio.sleep(10)
    await bot.change_presence(activity=choice(presence))
    channel = bot.get_channel(841614719562285086)
    await channel.send('Changing Presence')
    print("Changing Presence")
@presence_change.before_loop
async def presence_change_before():
    await bot.wait_until_ready()
@bot.command()
async def pstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.start()
    await ctx.send("Auto presence-changing started.")
  else:
    await ctx.send("You are not allowed to use this command!")
@bot.command()
async def pstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.cancel()
    await ctx.send("Auto presence-changing has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")

extensions = ['cogs.genshin', 
              'cogs.miscellaneous', 
              'cogs.mod', 
              'cogs.reminder', 
              'cogs.voice', 
              'cogs.info', 
              'cogs.fun'
]
if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
keep_alive()
bot.run(os.getenv('TOKEN'))
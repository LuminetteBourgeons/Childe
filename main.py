import discord
from discord.ext import commands
import os, asyncio

#status         =841614719562285086
#commands       =841906846389764146
#commands-error =854589548864340009
#warn-log       =855287882965188628
#dm-reports     =857821888230064178

orange=discord.Color.orange()

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

@bot.event
async def on_ready():
  members_set = set()
  for guild in bot.guilds:
    for member in guild.members:
      members_set.add(member)
  members = len(members_set)
  channel = bot.get_channel(841614719562285086)
  await channel.send('Rebooting')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity
  (type=discord.ActivityType.watching, name=(f"{members} Travelers!")))
  print('Childe is online.')


extensions = [
  'childe.childe',
  'childe.commands',
  'childe.help',
  'childe.presence',
  'cogs.fun',
  'cogs.info',
  'cogs.miscellaneous',
  'cogs.moderation',
  'cogs.owner',
  'cogs.reactions',
  'cogs.reminder',
  'cogs.voice',
  'genshin impact.general',
  'meme.pukul',
  'servers.boost',
  'servers.welcome',
  'tambahan.tompell'
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
bot.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands,tasks
import asyncio
from random import choice

orange=discord.Color.orange()

class Presence(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.presence= [
      discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
      discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'ch! '")),
      discord.Activity(type=discord.ActivityType.playing, name=("✨new prefix: '+ '✨")),
      discord.Activity(type=discord.ActivityType.playing, name=("with Luminette")),
      discord.Activity(type=discord.ActivityType.competing, name=("ᴛᴀʀ-ᴛᴀʀ-ᴛᴀɢʟɪᴀ👋ʟᴏᴠᴇʀ❤️ᴏғ🤾sɴᴇᴢʜɴᴀʏᴀɴ🌟ǫᴜᴇᴇɴ🌸")),
      discord.Activity(type=discord.ActivityType.competing, name=("ᴛʜᴇʀᴇ🥰ᴡᴀs🔥ᴀ🌝ᴄᴀᴛ🐈ᴛʜᴀᴛ🐸ʀᴇᴀʟʟʏ👑ᴡᴀs✨ɢᴏɴᴇᴇᴇ🌈")),
      discord.Activity(type=discord.ActivityType.watching, name=("Luminette ❤️")),
      discord.Activity(type=discord.ActivityType.listening, name=("Rasputin")),
      discord.Activity(type=discord.ActivityType.playing, name=("DM for Feedback!!")),
      discord.Activity(type=discord.ActivityType.listening, name=("Tartagalicious~"))
    ]

  @tasks.loop(minutes=5)
  async def presence_change(self):
    await asyncio.sleep(10)
    await self.bot.change_presence(activity=choice(self.presence))
    channel = self.bot.get_channel(841614719562285086)
    await channel.send('Changing Presence')
    print("Changing Presence")
  @presence_change.before_loop
  async def presence_change_before(self):
    await self.bot.wait_until_ready()
  @commands.command()
  async def pstart(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      self.presence_change.start()
      await ctx.send("Auto presence-changing started.")
    else:
      await ctx.send("You are not allowed to use this command!")
  @commands.command()
  async def pstop(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      self.presence_change.cancel()
      await ctx.send("Auto presence-changing has stopped.")
    else:
      await ctx.send("You are not allowed to use this command!")

def setup(bot):
  bot.add_cog(Presence(bot))

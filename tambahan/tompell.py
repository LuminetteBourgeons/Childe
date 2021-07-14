import discord
from discord.ext import commands,tasks
from random import choice

orange=discord.Color.orange()

class Tompell(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.colours = [
      discord.Colour(0x9b5de5), 
      discord.Colour(0xf15bb5), 
      discord.Colour(0xfee440), 
      discord.Colour(0x00bbf9), 
      discord.Colour(0x00f5d4)
      ]

  @tasks.loop(seconds=2)
  async def role_colour_change(self):
    await role_to_change.edit(colour=choice(self.colours))
    channel = self.bot.get_channel(841614719562285086)
    await channel.send('Changing Role Colour')
  @role_colour_change.before_loop
  async def colour_change_before(self):
    global role_to_change
    await self.bot.wait_until_ready()
    guild = self.bot.get_guild(775568951101882398)
    role_name = "🎀Bot Dev"
    role_to_change = discord.utils.get(guild.roles, name=role_name)
  @commands.command()
  async def rcstart(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      self.role_colour_change.start()
      await ctx.send("Auto role's colour changing has started.")
    else:
      await ctx.send("You are not allowed to use this command!")
  @commands.command()
  async def rcstop(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      self.role_colour_change.cancel()
      await ctx.send("Auto role's colour changing has stopped.")
    else:
      await ctx.send("You are not allowed to use this command!")

def setup(bot):
  bot.add_cog(Tompell(bot))

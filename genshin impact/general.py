import discord
from discord.ext import commands

class General(commands.Cog):   
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def exp(self, ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/637264326368952323/807527453303898152/exp.png")
  
  @commands.command(aliases=['talent'])
  async def weekly(self, ctx):
    await ctx.send("https://media.discordapp.net/attachments/840489159642841118/855088556836782120/Talent_eng.png")

  @commands.command()
  async def gi2021(self, ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/812186655783780352/865075703983898644/Frame_11.png")
  
def setup(bot):
    bot.add_cog(General(bot))

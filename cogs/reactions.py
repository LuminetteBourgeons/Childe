import discord
from discord.ext import commands

class Reactions(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  #expressions:
  @commands.command(aliases=['blushed'])
  async def blush(self, ctx, user: discord.Member = None):
    pass

  @commands.command(aliases=['confused'])
  async def confuse(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def cry(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def dab(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def dance(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def shrug(self, ctx, user: discord.Member = None):
    pass
  
  @commands.command()
  async def sleepy(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def triggered(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def wasted(self, ctx, user: discord.Member = None):
    pass
  
  #2 ppl required:  
  @commands.command()
  async def bang(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def bite(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def cuddle(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def greet(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def handhold(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def hug(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def insult(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def kill(self, ctx, user: discord.Member = None):
    pass
  
  @commands.command()
  async def kiss(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def lick(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def nom(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def pat(self, ctx, user: discord.Member = None):
    pass
  
  @commands.command()
  async def poke(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def punch(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def slap(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def stare(self, ctx, user: discord.Member = None):
    pass

  @commands.command()
  async def tickle(self, ctx, user: discord.Member = None):
    pass

def setup(bot):
  bot.add_cog(Reactions(bot))

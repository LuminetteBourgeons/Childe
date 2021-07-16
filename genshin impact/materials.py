import discord
from discord.ext import commands
import requests

class Materials(commands.Cog):   
  def __init__(self,bot):
    self.bot=bot

  @commands.group()
  async def m(self, ctx):
    pass

  @m.command(name="boss")
  async def m_boss(self, ctx):
    url = f"https://api.genshin.dev/materials/boss-material"
    stats = requests.get(url)
    mats = stats.json()
    mat = list(mats.values())
    embed= discord.Embed(title="Boss materials informations", description="", color=discord.Color.orange())
    for m in mat:
      embed.add_field(name="‎‎", value="```FIX\n[{}]\nSource: {}```\n".format(m['name'],m['source']), inline=False)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  
def setup(bot):
    bot.add_cog(Materials(bot))
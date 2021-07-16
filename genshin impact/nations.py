import discord
from discord.ext import commands
import requests

class Nations(commands.Cog):   
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def nation(self, ctx, *, nation: str):
    url = f"https://api.genshin.dev/nations/{nation}"
    stats = requests.get(url)
    json_stats = stats.json()
    name = json_stats["name"]
    element = json_stats["element"]
    archon = json_stats["archon"]
    govern = json_stats["controllingEntity"]
    embed = discord.Embed(title=name, description="*Nation Information*", color=discord.Color.orange())
    embed.add_field(name='Element', value=element, inline=True)
    embed.add_field(name='Archon', value=archon, inline=True)
    embed.add_field(name='Controlling Entity', value=govern, inline=False)
    ele = json_stats["element"].lower()
    embed.set_thumbnail(url=f"https://api.genshin.dev/elements/{ele}/icon.png")
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Nations(bot))
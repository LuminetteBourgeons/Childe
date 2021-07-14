import discord
from discord.ext import commands

orange=discord.Color.orange()

class Childe(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def about(self, ctx):
    members_set = set()
    for guild in self.bot.guilds:
      for member in guild.members:
        members_set.add(member)
    members = len(members_set)
    embed=discord.Embed(
      title="__*Childe's information:*__", 
      description=
      f"I'm No. 11 of the Fatui Harbingers, codename **Childe**, but I also go by Tartaglia. And you... Hmm, you too like to cause quite the stir, don't you? Something tells me we're going to get along splendidly. :)\n\n"
      "I'm on version 3.0\n"
      "For more information about my commands, use `+ help`\n"
      f"I'm now serving `{len(self.bot.guilds)}` servers, and `{members}` members!\n\n"
      "[Click here](https://github.com/LuminetteBourgeons/Childe) to see Luminette's github (don't forget the stars please 🧡🧡)\n"
      "[Click here](https://ko-fi.com/childe_bot) to treat me a coffee 🧡\n"
      "[Click here](https://discord.gg/TKDAb8DjT9) to join our support server 🧡\n\n"
      "‎ ‎ \nPrefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n"
      "<:Chchibi:843379361138737182> Develop by: Luminette\n‎ ‎ ", 
      color=orange
      )
    await ctx.send(embed=embed)

  @commands.command()
  async def invite (self, ctx):
    embed=discord.Embed(
      title="<:Chchibi:843379361138737182> __Invite me to your server!__ <:Chchibi:843379361138737182>",
      description="[Click here](https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot)\n*as Administrator*\n", 
      color=orange
      )
    await ctx.send(embed=embed)

  @commands.command()
  async def vote (self, ctx):
    embed=discord.Embed(
      title="<:Chchibi:843379361138737182> __Vote me on top.gg!__ <:Chchibi:843379361138737182>",
      description="[Click here](https://top.gg/bot/806793987876192268)",
      color=orange
    )
    await ctx.send (embed=embed)

def setup(bot):
  bot.add_cog(Childe(bot))

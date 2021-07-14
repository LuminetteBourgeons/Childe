import discord
from discord.ext import commands

orange=discord.Color.orange()

class Boost(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.type.name in ['premium_guild_subscription', 'premium_guild_tier_1', 'premium_guild_tier_2', 'premium_guild_tier_3']:
      if message.guild.id == 775568951101882398:
        embed = discord.Embed( colour=orange,description=f"**{message.author.name}**, Terimakasih telah boost server kami! <:02love:852123836366323712>")
        channel = self.bot.get_channel(775580161897660436)
        await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Boost(bot))
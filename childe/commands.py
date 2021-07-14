import discord
from discord.ext import commands

orange=discord.Color.orange()

class Bot(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.Cog.listener()
  async def on_command(self, ctx):
    channel = self.bot.get_channel(841906846389764146)
    embed = discord.Embed(title=f"<:Chchibi:843379361138737182> {ctx.author.name} used a command!", description=f"{ctx.message.content}",colour=discord.Color.orange())
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
  @commands.Cog.listener()
  async def on_command_completion(self, ctx):
    channel = self.bot.get_channel(841906846389764146)
    embed = discord.Embed(title=f"<:Chchibi:843379361138737182> Completed {ctx.author.name}'s command!", description=f"{ctx.message.content}",colour=discord.Color.gold())
    await channel.send(embed=embed)
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title="Error!", description="You are missing the permission `" + ", ".join(error.missing_perms) + "` to execute this command!", color=discord.Colour.red())
      await ctx.send(embed=embed, delete_after=7)
      channel = self.bot.get_channel(854589548864340009)
      embed = discord.Embed(title=f"ERROR -- commands.MissingPermissions", description=f"{ctx.message.content}",colour=discord.Color.red())
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title="Error!",description=str(error).capitalize(), color=discord.Colour.red())
      await ctx.send(embed=embed, delete_after=7)
      channel = self.bot.get_channel(854589548864340009)
      embed = discord.Embed(title=f"ERROR -- commands.MissingRequiredArgument", description=f"{ctx.message.content}",colour=discord.Color.red())
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
    elif isinstance(error, commands.ChannelNotFound):
      await ctx.send(f'Channel not found!', delete_after=7)
      channel = self.bot.get_channel(854589548864340009)
      embed = discord.Embed(title=f"ERROR -- commands.ChannelNotFound", description=f"{ctx.message.content}",colour=discord.Color.red())
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
      return
    elif isinstance(error, commands.MemberNotFound):
      await ctx.send(f'Member not found!', delete_after=7)
      channel = self.bot.get_channel(854589548864340009)
      embed = discord.Embed(title=f"ERROR -- commands.MemberNotFound", description=f"{ctx.message.content}",colour=discord.Color.red())
      embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
      await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
      return
    raise error

def setup(bot):
  bot.add_cog(Bot(bot))

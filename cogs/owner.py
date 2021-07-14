import discord
from discord.ext import commands
import aiohttp
from .utils import http

orange=discord.Color.orange()

class Owner(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.group()
  @commands.is_owner()
  async def change(self, ctx):
    pass

  @change.command(name="username")
  @commands.is_owner()
  async def change_username(self, ctx, *, name: str):
    try:
      await self.bot.user.edit(username=name)
      await ctx.send(f"Successfully changed username to **{name}**")
    except discord.HTTPException as err:
      await ctx.send(err)

  @change.command(name="nickname")
  @commands.is_owner()
  async def change_nickname(self, ctx, *, name: str = None):
    try:
      await ctx.guild.me.edit(nick=name)
      if name:
        await ctx.send(f"Successfully changed nickname to **{name}**")
      else:
        await ctx.send("Successfully removed nickname")
    except Exception as err:
      await ctx.send(err)

  @change.command(name="avatar")
  @commands.is_owner()
  async def change_avatar(self, ctx, url: str = None):
    if url is None and len(ctx.message.attachments) == 1:
      url = ctx.message.attachments[0].url
    else:
      url = url.strip("<>") if url else None
    try:
      bio = await http.get(url, res_method="read")
      await self.bot.user.edit(avatar=bio)
      await ctx.send(f"Successfully changed the avatar. Currently using:\n{url}")
    except aiohttp.InvalidURL:
      await ctx.send("The URL is invalid...")
    except discord.InvalidArgument:
      await ctx.send("This URL does not contain a useable image")
    except discord.HTTPException as err:
      await ctx.send(err)
    except TypeError:
      await ctx.send("You need to either provide an image URL or upload one with the command")

  @commands.command(aliases=['echo'])
  async def say(self, ctx, *, msg):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.message.delete()
      await ctx.send(msg)

  @commands.command()
  async def servers(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.send("<:Chchibi:843379361138737182>__**Childe's active servers:**__<:Chchibi:843379361138737182>")
      activeservers = self.bot.guilds
      for guild in activeservers:
        await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\nOwner ID :`{guild.owner.id}`\nMembers: `{guild.member_count}`')
        await ctx.send('––––––––––––––––––––––––––––––––––––––––––––––––')

  @commands.command()
  async def setonline(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(status=discord.Status.online)
      embed = discord.Embed(color=orange, title="Set Childe's status to",description='`Online`')
      await ctx.send(embed=embed)
  @commands.command()
  async def setidle(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(status=discord.Status.idle)
      embed = discord.Embed(color=orange, title="Set Childe's status to",description='`Idle`')
      await ctx.send(embed=embed)
  @commands.command()
  async def setdnd(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(status=discord.Status.dnd)
      embed = discord.Embed(color=orange, title="Set Childe's status to",description='`Do not disturb`')
      await ctx.send(embed=embed)
  @commands.command()
  async def setinv(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(status=discord.Status.invisible)
      embed = discord.Embed(color=orange, title="Set Childe's status to",description='`Invisible`')
      await ctx.send(embed=embed)

  @commands.command()
  async def actplaying(self, ctx, *, name):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=name))
      embed = discord.Embed(color=orange,title="Set Childe's activity to",description=f'`playing {name}`')
      await ctx.send(embed=embed)
  @commands.command()
  async def actlistening(self, ctx, *, name):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
      embed = discord.Embed(color=orange, title="Set Childe's activity to",description=f'`listening {name}`')
      await ctx.send(embed=embed)
  @commands.command()
  async def actwatching(self, ctx, *, name):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
      embed = discord.Embed(color=orange,title="Set Childe's activity to",description=f'`watching {name}`')
      await ctx.send(embed=embed)
  @commands.command()
  async def actcompeting(self, ctx, *, name):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=name))
      embed = discord.Embed(color=orange, title="Set Childe's activity to",description=f'`competing in {name}`')
      await ctx.send(embed=embed)

  @commands.command()
  async def shutdown(self, ctx):
    if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
      await ctx.send('shutting down... good night...')
      await self.bot.close()

def setup(bot):
    bot.add_cog(Owner(bot))

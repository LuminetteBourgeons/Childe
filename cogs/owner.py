import discord
from discord.ext import commands
import aiohttp
from .utils import http

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


def setup(bot):
    bot.add_cog(Owner(bot))

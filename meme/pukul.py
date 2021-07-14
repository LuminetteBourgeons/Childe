import discord
from discord.ext import commands
from PIL import Image
import requests, io

class Pukul(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  async def pukul(self, ctx, user1: discord.Member):
    await ctx.trigger_typing()
    user2 = ctx.author
    if user1.avatar:
      user1url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user1.id, user1.avatar,)
    else:
      user1url = "https://cdn.discordapp.com/embed/avatars/1.png"
    if user2.avatar:
      user2url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user2.id, user2.avatar,)
    else:
      user2url = "https://cdn.discordapp.com/embed/avatars/1.png"
    response1 = requests.get(user1url)
    image_bytes1 = io.BytesIO(response1.content)
    response2 = requests.get(user2url)
    image_bytes2 = io.BytesIO(response2.content)
    im1 = Image.open('meme/pukul.jpg')
    im2 = Image.open(image_bytes1)
    im3 = Image.open(image_bytes2)
    back_im = im1.copy()
    back_im.paste(im2, (215,425))
    back_im.paste(im3, (480,415))
    back_im.save(f"pukul/{ctx.author.name}{user1}.png")
    await ctx.send(file = discord.File(f"pukul/{ctx.author.name}{user1}.png"))

def setup(bot):
  bot.add_cog(Pukul(bot))
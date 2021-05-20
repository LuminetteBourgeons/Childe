import discord
from discord.ext import commands
import asyncio, random

class Fun(commands.Cog):
    def __init__(self,bot):
      self.bot=bot
      self.ball = ['It is certain', 
                  'It is decidedly so', 
                  'Without a doubt', 
                  'Yes definitely', 
                  'You may rely on it',
                  'As I see it, yes', 
                  'Most likely', 
                  'Outlook good', 
                  'Yes', 
                  'Signs point to yes',
                  'Reply hazy try again', 
                  'Try ask Zhongli about this', 
                  'Ask again later', 
                  'Better not tell you now', 
                  'Cannot predict now', 
                  'Oh, sorry... Please ask again, I lost myself in your eyes.',
                  'Don\'t count on it, comrade', 
                  'My reply is no', 
                  'My sources say no', 
                  'Outlook not so good', 
                  'Very doubtful']

    @commands.command(aliases=['roll'])
    async def dice(self, ctx):
      dice6=["1","2","3","4","5","6"]
      msg = await ctx.send("Rolling the dice~")
      await asyncio.sleep(3)
      await msg.delete()
      await ctx.send(f"It landed on {random.choice(dice6)}!")

    @commands.command(aliases=['flip'])
    async def coin(self, ctx):
      coin2=["head","tail"]
      childe=["Well, I'd choose head though...","Well, I'd choose tail though...","Do you believe on that?","","","","And you landed on my heart ;)"]
      msg = await ctx.send("Flipping the coin~")
      await asyncio.sleep(3)
      await msg.delete()
      await ctx.send(f"It landed on {random.choice(coin2)}. {random.choice(childe)}")

    @commands.command(aliases=['8ball'])
    async def ball8(self, ctx, *, msg: str):
            await ctx.send("Let ~~my~~ **8**ball decide your fate ;D")
            answer = random.randint(0, 19)
            em = discord.Embed(color=discord.Colour.orange())
            em.add_field(name='\u2753 Question', value=msg)
            em.add_field(name='\ud83c\udfb1 8ball', value=self.ball[answer], inline=False)
            await ctx.send(content=None, embed=em)
            await ctx.message.delete()

def setup(bot):
  bot.add_cog(Fun(bot))
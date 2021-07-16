import discord
from discord.ext import commands
import requests, json

with open('json/weapons.json') as json_file:
  f_weapons = json.load(json_file)
with open('json/artifacts.json') as json_file:
  f_artifacts = json.load(json_file)
  
class Equipment(commands.Cog):   
  def __init__(self,bot):
    self.bot=bot
  
  def embed_weapon(self, weapon):
    url = f"https://api.genshin.dev/weapons/{weapon}"
    stats = requests.get(url)
    weapons = stats.json()
    stars = ''
    for i in range(weapons['rarity']):
      stars += ' ⭐'
    embed = discord.Embed(title=weapons['name'], description=stars, color=discord.Color.orange())
    embed.set_thumbnail(url=f"https://api.genshin.dev/weapons/{weapon}/icon")
    embed.add_field(name='Type', value=weapons['type'], inline=True)
    embed.add_field(name='Base ATK', value=weapons['baseAttack'], inline=True)
    embed.add_field(name='SubStat', value=weapons['subStat'], inline=True)
    embed.add_field(name='Location', value=weapons['location'], inline=True)
    embed.add_field(name='Passive Name', value=weapons['passiveName'], inline=False)
    embed.add_field(name='Passive Description', value=weapons['passiveDesc'], inline=False)
    return embed

  @commands.command(aliases=['w'])
  async def weapon(self, ctx, *keyword):
    keyword = ' '.join(keyword).lower()
    count = 0
    find_list = []
    find_one = None
    for weap in f_weapons:
      name = weap['name'].lower()
      weapon = weap['id']
      if keyword.lower() == weap['name'].lower():
        embed = self.embed_weapon(weapon)
        embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
      elif len(keyword) >= 4:
        if name.find(keyword) >= 0:
          find_one = weapon
          find_list.append(weap)
          count += 1
    if count == 0:
      embed = discord.Embed(description="Weapon not found",colour=discord.Colour.red())
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    elif count == 1:
      embed = self.embed_weapon(find_one)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    else:
      weapon_list = ''
      for weap in find_list:
        weapon_list += f"{weap['name']}\n"
      embed = discord.Embed(color=discord.Color.orange())
      embed.set_author(name=f"{count} weapons found\nPlease choose one")
      embed.add_field(name="Syntax : `+ weapon {name}`", value=weapon_list, inline=False)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    if count != 0:
      return    

  @commands.command(aliases=['wlist'])
  async def weapons(self, ctx):
    url = f"https://api.genshin.dev/weapons/"
    stats = requests.get(url)
    weapons = stats.json()
    embed = discord.Embed(title="Weapon list", description="```"+"\n".join(weapons)+"```", color=discord.Color.orange())
    embed.set_footer(text="use `+weapon <weapon name>`")
    await ctx.author.send(embed=embed)
    await ctx.send("I sent you the weapon list on your DM!")
      
  def embed_artifact(self, artifact):
    url = f"https://api.genshin.dev/artifacts/{artifact}"
    stats = requests.get(url)
    artifacts = stats.json()
    embed = discord.Embed(title=artifacts['name'], description="*artifact details*", color=discord.Color.orange())
    print(url)
    embed.set_thumbnail(url=f"https://api.genshin.dev/artifacts/{artifact}/flower-of-life")
    embed.add_field(name='Max Rarity', value=artifacts['max_rarity'], inline=False)
    embed.add_field(name='2 Piece Bonus', value=artifacts['2-piece_bonus'], inline=False)
    embed.add_field(name='4 Piece Bonus', value=artifacts['4-piece_bonus'], inline=True)
    return embed

  @commands.command(aliases=['a'])
  async def artifact(self, ctx, *keyword):
    keyword = ' '.join(keyword).lower()
    count = 0
    find_list = []
    find_one = None
    for arte in f_artifacts:
      name = arte['name'].lower()
      artifact = arte['id']
      if keyword.lower() == arte['name'].lower():
        embed = self.embed_artifact(artifact)
        embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
      elif len(keyword) >= 4:
        if name.find(keyword) >= 0:
          find_one = artifact
          find_list.append(arte)
          count += 1
    if count == 0:
      embed = discord.Embed(description="Artifact not found",colour=discord.Colour.red())
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    elif count == 1:
      embed = self.embed_artifact(find_one)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    else:
      artifact_list = ''
      for arte in find_list:
        artifact_list += f"{arte['name']}\n"
      embed = discord.Embed(color=discord.Color.orange())
      embed.set_author(name=f"{count} artifacts found\nPlease choose one")
      embed.add_field(name="Syntax : `+ artifact {name}`", value=artifact_list, inline=False)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    if count != 0:
      return

  @commands.command(aliases=['alist'])
  async def artifacts(self, ctx):
    url = f"https://api.genshin.dev/artifacts"
    stats = requests.get(url)
    artifacts = stats.json()
    embed = discord.Embed(title="Artifact list", description="```"+"\n".join(artifacts)+"```", color=discord.Color.orange())
    embed.set_footer(text="use `+artifact <artifact name>`")
    await ctx.author.send(embed=embed)
    await ctx.send("I sent you the artifact list on your DM!")
  
def setup(bot):
    bot.add_cog(Equipment(bot))
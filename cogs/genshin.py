import discord
from discord.ext import commands
import json

with open('json/weapons.json') as json_file:
  f_weapons = json.load(json_file)
with open('json/artifacts.json') as json_file:
  f_artifacts = json.load(json_file)
with open('json/characters.json') as json_file:
  f_characters = json.load(json_file)

class Genshin(commands.Cog):   
  def embed_character(self,character):
    stars = ''
    for i in range(character['rarity']):
      stars += ' ⭐'
    embed = discord.Embed(title=character['name'], description=stars, color=discord.Colour.orange())
    embed.set_author(name='Character details')
    embed.set_image(url=character['img'])
    embed.add_field(name='Element', value=character['element'], inline=True)
    embed.add_field(name='Weapon', value=character['weapon'], inline=True)
    embed.add_field(name='Constellation', value=character['constellation'], inline=False)
    return embed
  def embed_character2(self,character):
    stars = ''
    for i in range(character['rarity']):
      stars += ' ⭐'
    embed = discord.Embed(title=character['name2'], description=stars, color=discord.Colour.orange())
    embed.add_field(name='Constellation', value=character['cons2'], inline=False)
    return embed
  @commands.command(name='chara')
  async def cmd_character(self, ctx, *keyword):
    keyword = ' '.join(keyword).lower()
    count = 0
    find_list = []
    find_one = None
    emoji = '⬇️'
    for character in f_characters:
      name = character['name'].lower()
      if keyword.lower() == character['name'].lower():
        embed = self.embed_character(character)
        embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji)
        while True:
          reaction = await ctx.bot.wait_for_reaction(emoji="⬇️", message=message, timeout=30)
          embed = self.embed_character2(character)
          embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
          await message.edit(content=embed)
        return
      elif len(keyword) >= 4:
        if name.find(keyword) >= 0:
          find_one = character
          find_list.append(character)
          count += 1
    if count == 0:
      embed = discord.Embed(description="Character not found",colour=discord.Colour.red())
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    elif count == 1:
      embed = self.embed_character(find_one)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      message = await ctx.send(embed=embed)
      await message.add_reaction(emoji)
      while True:
        reaction = await ctx.bot.wait_for_reaction(emoji="⬇️", message=message)
        embed = self.embed_character2(find_one)
        await message.edit(content=embed)
    else:
      character_list = ''
      for character in find_list:
        character_list += f"{character['name']}\n"
      embed = discord.Embed(color=discord.Colour.orange())
      embed.set_author(name=f"{count} characters found\nPlease choose one")
      embed.add_field(name="Syntax : `+ chara {name}`", value=character_list, inline=False)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    if count != 0:
      return
        
  def embed_weapon(self, weapon):
    stars = ''
    for i in range(weapon['rarity']):
      stars += ' ⭐'
    embed = discord.Embed(title=weapon['name'], description=stars, color=discord.Colour.orange())
    embed.set_author(name='Weapon details')
    embed.set_thumbnail(url=weapon['img'])
    embed.add_field(name='Type', value=weapon['type'], inline=True)
    embed.add_field(name='Rarity', value=weapon['rarity'], inline=True)
    embed.add_field(name='Secondary', value=weapon['secondary'], inline=True)
    embed.add_field(name='Passive', value=weapon['passive'], inline=True)
    embed.add_field(name='Base ATK', value=weapon['atk'], inline=True)
    embed.add_field(name='Location', value=weapon['location'], inline=True)
    embed.add_field(name='Bonus', value=weapon['bonus'], inline=False)
    return embed
  @commands.command(name='w')
  async def cmd_weapon(self, ctx, *keyword):
    keyword = ' '.join(keyword).lower()
    count = 0
    find_list = []
    find_one = None
    for weapon in f_weapons:
      name = weapon['name'].lower()
      if keyword.lower() == weapon['name'].lower():
        embed = self.embed_weapon(weapon)
        embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
      elif len(keyword) >= 4:
        if name.find(keyword) >= 0:
          find_one = weapon
          find_list.append(weapon)
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
      for weapon in find_list:
        weapon_list += f"{weapon['name']}\n"
      embed = discord.Embed(color=discord.Colour.orange())
      embed.set_author(name=f"{count} weapons found\nPlease choose one")
      embed.add_field(name="Syntax : `+ weapon {name}`", value=weapon_list, inline=False)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    if count != 0:
      return

  def embed_artifact(self, artifact):
    stars = ''
    embed = discord.Embed(title=artifact['set'], description=stars, color=discord.Colour.orange())
    embed.set_author(name='Artifact details')
    embed.set_thumbnail(url=artifact['img'])
    embed.add_field(name='Max Rarity', value=artifact['max-rarity'], inline=False)
    embed.add_field(name='2-Piece Bonus', value=artifact['2-set bonus'], inline=False)
    embed.add_field(name='4-Piece Bonus', value=artifact['4-set bonus'], inline=False)
    return embed
  @commands.command(name='a')
  async def cmd_artifact(self, ctx, *keyword):
    keyword = ' '.join(keyword).lower()
    count = 0
    find_list = []
    find_one = None
    for artifact in f_artifacts:
      name = artifact['set'].lower()
      if keyword.lower() == artifact['set'].lower():
        embed = self.embed_artifact(artifact)
        embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
      elif len(keyword) >= 4:
        if name.find(keyword) >= 0:
          find_one = artifact
          find_list.append(artifact)
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
      for artifact in find_list:
        artifact_list += f"{artifact['set']}\n"
      embed = discord.Embed(color=discord.Colour.orange())
      embed.set_author(name=f"{count} artifact found\nPlease choose one")
      embed.add_field(name="Syntax : `+ artifact {name}`", value=artifact_list, inline=False)
      embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
    if count != 0:
      return

    @commands.command()
    async def exp(self, ctx):
      await ctx.send("https://cdn.discordapp.com/attachments/637264326368952323/807527453303898152/exp.png")
      
def setup(bot):
    bot.add_cog(Genshin(bot))

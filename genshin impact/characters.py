import discord
from discord.ext import commands
import requests
import DiscordUtils

class Characters(commands.Cog):   
  def __init__(self,bot):
    self.bot=bot

  @commands.command(aliases=['c', 'chara'])
  async def character (self, ctx, *, character: str):
    character = character.replace("'", "-")
    character = character.replace(" ", "-")
    url = f"https://api.genshin.dev/characters/{character}"
    stats = requests.get(url)
    json_stats = stats.json()
    stars = ''
    for i in range(json_stats['rarity']):
      stars += ' ⭐'
    name = json_stats["name"]
    desc = json_stats["description"]
    rarity = stars
    vision = json_stats["vision"]
    weapon = json_stats["weapon"]
    nation = json_stats["nation"]
    affiliation = json_stats["affiliation"]
    constellation = json_stats["constellation"]
    birthday = json_stats["birthday"]
    cons = json_stats["constellations"]
    talent = json_stats["skillTalents"]
    passive = json_stats["passiveTalents"]
    embed1 = discord.Embed(title=name, description=desc, color=discord.Color.orange())
    element = json_stats["vision"].lower()
    embed1.set_thumbnail(url=f"https://api.genshin.dev/elements/{element}/icon")
    embed1.add_field(name='Rarity', value=rarity, inline=True)
    embed1.add_field(name='Vision', value=vision, inline=True)
    embed1.add_field(name='Weapon', value=weapon, inline=True)
    embed1.add_field(name='Nation', value=nation, inline=True)
    embed1.add_field(name='Affiliation', value=affiliation, inline=True)
    embed1.add_field(name='Constellation', value=constellation, inline=True)
    embed1.add_field(name='Birthday', value=f"(yyyy-mm-dd) {birthday}", inline=True)
    embed1.set_image(url=f"https://api.genshin.dev/characters/{character}/portrait")
    embed1.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed2 = discord.Embed(title=name, description=f"{desc}\n**Constellation**", color=discord.Color.orange())
    embed2.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")
    for constel in cons:
      embed2.add_field(name="‎\n‎", value="```CSS\n[{}]\n{}```\n```{}```\n".format(constel['name'],constel['unlock'],constel['description']), inline=False)
    embed2.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed3 = discord.Embed(title=name, description=f"{desc}\n**Talents**", color=discord.Color.orange())
    embed3.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")
    for skill in talent:
      embed3.add_field(name="‎\n‎", value="```FIX\n[{}]\n{}```\n```{}```\n".format(skill['name'],skill['unlock'],skill['description']), inline=False)
    embed3.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed4 = discord.Embed(title=name, description=f"{desc}\n**Passive**", color=discord.Color.orange())
    embed4.set_thumbnail(url=f"https://api.genshin.dev/characters/{character}/icon")
    for pasif in passive:
      embed4.add_field(name="‎\n‎", value="```FIX\n[{}]\n{}```\n```{}```\n".format(pasif['name'],pasif['unlock'],pasif['description']), inline=False)
    embed4.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    embeds = [embed1, embed2, embed3, embed4]
    await paginator.run(embeds)

  @commands.command(aliases=['charalist'])
  async def characters(self, ctx):
    url = f"https://api.genshin.dev/characters"
    stats = requests.get(url)
    charas = stats.json()
    embed = discord.Embed(title="Character list", description="```"+"\n".join(charas)+"```", color=discord.Color.orange())
    embed.set_footer(text="use `+character <chara name>`")
    await ctx.author.send(embed=embed)
    await ctx.send("I sent you the character list on your DM!")
    
def setup(bot):
    bot.add_cog(Characters(bot))
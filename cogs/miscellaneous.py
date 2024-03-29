import discord
from discord.ext import commands
import random, time
from .utils import chat_formatting
from urllib.parse import quote_plus
import aiohttp
import json
import requests

#dibawah ada ubah warna embed

class Misc(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.regionals = {
      'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 
      'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
      'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
      'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 
      'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
      'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
      'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 
      'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
      'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
      'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 
      'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
      'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
      'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 
      'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
      'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
      'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 
      'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
      'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
      's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 
      't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
      'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
      'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 
      'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
      'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
      'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 
      'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
      '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
      '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', 
      '8': '8⃣', '9': '9⃣', '!': '\u2757', '?': '\u2753'
      }
    
  @commands.command(aliases=['calc'])
  async def calculate(self, ctx, *, q):
    await ctx.send(f"{q}={eval(q)}")

  @commands.command(aliases=['pick'])
  async def choose(self, ctx, *, choices: str):
    await ctx.send('I choose: {}'.format(random.choice(choices.split("|"))))
  
  @commands.command()
  async def regional(self,ctx, *, msg):
    await ctx.message.delete()
    msg = list(msg)
    regional_list = [self.regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
    regional_output = '\u200b'.join(regional_list)
    await ctx.send(regional_output)
    
  @commands.command()
  async def ping(self, ctx):
    before = time.monotonic()
    message = await ctx.send("🏓 Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 Pong!  `{int(ping)}ms`")

  @commands.command()
  async def poll(self, ctx, *, title):
    embed = discord.Embed(title="A new poll has been created!", description=f"{title}", color=discord.Colour.orange())
    embed.set_footer(text=f"Poll created by: {ctx.message.author} • React to vote!")
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

  @commands.command()
  async def bitcoin(self, ctx):
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    async with aiohttp.ClientSession() as session:
      raw_response = await session.get(url)
      response = await raw_response.text()
      response = json.loads(response)
      embed = discord.Embed(title=":information_source: Info",description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}", color=discord.Colour.orange())
      await ctx.send(embed=embed)

  @commands.command()
  async def urban(self, ctx, *, search_terms: str, definition_number: int = 1):
    def encode(s):
      return quote_plus(s, encoding="utf-8", errors="replace")
    search_terms = search_terms.split(" ")
    try:
      if len(search_terms) > 1:
        pos = int(search_terms[-1]) - 1
        search_terms = search_terms[:-1]
      else:
        pos = 0
      if pos not in range(0, 11):
        pos = 0
    except ValueError:
      pos = 0
    search_terms = "+".join([encode(s) for s in search_terms])
    url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
    try:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
          result = await r.json()
      if result["list"]:
        definition = result['list'][pos]['definition']
        example = result['list'][pos]['example']
        defs = len(result['list'])
        msg = ("**Definition #{} out of {}:\n**{}\n**Example:\n**{}".format(pos + 1, defs, definition,example))
        msg = chat_formatting.pagify(msg, ["\n"])
        for page in msg:
          await ctx.send(page)
      else:
        await ctx.send("Your search terms gave no results.")
    except IndexError:
      await ctx.send("There is no definition #{}".format(pos + 1))

  @commands.command()
  async def weather(self, ctx, *, city: str):
    api_key = "d56ded016a1a4e4339037079e9f4794f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
      async with channel.typing():
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature_celsius = str(round(current_temperature - 273.15))
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        embed = discord.Embed(title=f"Weather in {city_name}", color=discord.Color.orange(),timestamp=ctx.message.created_at)
        embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
        embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsius}°C**", inline=False)
        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
        embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")

  @commands.command()
  async def covid(self, ctx, *, country: str):
    url = f"https://coronavirus-19-api.herokuapp.com/countries/{country}"
    stats = requests.get(url)
    json_stats = stats.json()
    country = json_stats["country"]
    totalCases = json_stats["cases"]
    todayCases = json_stats["todayCases"]
    totalDeaths = json_stats["deaths"]
    todayDeaths = json_stats["todayDeaths"]
    recovered = json_stats["recovered"]
    active = json_stats["active"]
    critical = json_stats["critical"]
    embed = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description=".", color=discord.Color.orange(), timestamp=ctx.message.created_at)
    embed.add_field(name="**Total Cases**", value=totalCases, inline=True)
    embed.add_field(name="**Today Cases**", value=todayCases, inline=True)
    embed.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
    embed.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
    embed.add_field(name="**Recovered**", value=recovered, inline=True)
    embed.add_field(name="**Active**", value=active, inline=True)
    embed.add_field(name="**Critical**", value=critical, inline=True)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Misc(bot))

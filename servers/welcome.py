import discord
from discord.ext import commands

orange=discord.Color.orange()

class Welcome(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == 271215379311886336:
      channel = self.bot.get_channel(834013759516573707)
      await channel.send("Welcome, {} :heart:".format (member.mention))
    elif member.guild.id == 738709993238560899:
      channel = self.bot.get_channel(765546060910166036)
      await channel.send("Met datang di Rumah Mine, {} :heart:".format (member.mention)) 
    elif member.guild.id == 747872613174608012:
      channel = self.bot.get_channel(747872613686181991)
      await channel.send("Selamat datang, {}! :D".format (member.mention))
    elif member.guild.id == 775568951101882398:
      channel = self.bot.get_channel(775568951412523010)
      embed=discord.Embed(
      title="<:paimonisfood:777925956630741043>",
      description=
        "__ ׂׂૢ་༘࿐\n"
        "┊ ⋆ ┊ . ┊ ┊\n"
        "┊ ┊⋆ ┊ .\n"
        "┊ ┊ ⋆˚ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭\n"
        "✧. ┊ ⁭ ⁭ ⁭ ⁭ \n"
        "⁭ ⁭ ⁭ ⁭ ⁭⋆ ★\n"
        "⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒\n"
        "‹·˚ 𝐓𝐨𝐦𝐩𝐞𝐥𝐋 𝐃𝐢𝐬𝐜𝐨𝐫𝐝 𝐒𝐞𝐫𝐯𝐞𝐫 〄⋆̩\n"
        "︶︶︶︶︶︶︶︶︶︶︶︶︶︶ ೄྀ࿐ ˊ\n"
        "<:paimonisfood:777925956630741043> \n"
        "╰┈➤ Silahkan untuk ambil role , ada di <#775634842247364619> untuk menunjukkan sedikit informasi tentang dirimu, jadi member lain bisa kenal kamu lebih dekat 😉\n"
        "<:loveu:777925956379607080> \n"
        "╰┈➤ Mohon untuk membaca <#831462974011080734> agar kamu memahami peraturan yang berlaku di server TompelL.\n\n"
        "────────────────────────────────────────\n"
        "<:yaws:777925956257972234> Terima kasih! <:yaws:777925956257972234>\n")
      await channel.send(
          "Selamat datang di **Server Discord TompelL**, {} :heart:. <:ooogitu:813675925287469096> Silahkan untuk baca text dibawah ini ⬎".format (member.mention),
          embed=embed
          )
    else:
      return

def setup(bot):
  bot.add_cog(Welcome(bot))
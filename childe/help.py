import discord
from discord.ext import commands
import DiscordUtils

orange=discord.Color.orange()

class Help(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def help(self, ctx):
    embed1=discord.Embed(
      title="__*Childe's commands:*__", 
      description=
        "Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n"
        "Use `+ about` for my informations!\n"
        "🧡 Develop by: `Luminette#9466` & `Luminette#0103` \n"
        "`For Admin Commands use `***`+modhelp`***\n", 
        color=orange
        )
    embed1.set_thumbnail(
      url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935'
      )
    embed1.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed1.set_image(
      url="https://i.imgur.com/gFEUGlR.jpeg"
      )
    embed2=discord.Embed(
      title="<:Chchibi:843379361138737182> __Invite me to your server!__ <:Chchibi:843379361138737182>", 
      description="[Click here](https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot)\n"
      "*as Administrator*\n\n", 
      color=orange
      )
    embed2.set_thumbnail(
      url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935'
      )
    embed2.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed2.set_image(
      url="https://i.imgur.com/gFEUGlR.jpeg"
      )
    embed3=discord.Embed(
      title='<:pai1:845141679102754836> __Genshin Impact:__', 
      description=
      "**For more information, use `+gihelp`**\n"
      "‎ ‎ ‎ ‎ ・**General information commands**\n"
      "‎ ‎ ‎ ‎ ・**Artifact commands**\n"
      "‎ ‎ ‎ ‎ ・**Weapon commands**\n"
      "‎ ‎ ‎ ‎ ・**Character commands**\n"
      "\nComming soon:\n"
      "‎ ‎ ‎ ‎ ・Food & Potion commands\n"
      "‎ ‎ ‎ ‎ ・Domains commands\n"
      "‎ ‎ ‎ ‎ ・Material commands\n"
      "‎ ‎ ‎ ‎ ・Enemies commands\n"
      ,color=orange
      )
    embed3.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed4=discord.Embed(
      title='<:pai2:845141694541332481> __Fun:__', 
      description=
      "‎ ‎ ‎ ‎ ・*Rolling a dice:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ roll` / `+ dice`\n"
      "‎ ‎ ‎ ‎ ・*Flipping a coin:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ flip` / `+ coin`\n"
      "‎ ‎ ‎ ‎ ・*Ask 8ball:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ 8ball <question>` / `+ ball8 <question>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > I will answer your yes/no question :)\n"
      "‎ ‎ ‎ ‎ ・*Rock, Paper, Scissors:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ rps`\n"
      "‎ ‎ ‎ ‎ ・*Tic Tac Toe:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ ttt <@user>`\n‎"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Using tictactoe commands:\n‎"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎`+ ttt @Luminette`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎`+ ttt place <number>` (after the game had begun)\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ex: `+ttt place 5`\n"
      "‎ ‎ ‎ ‎ ・*Dad Joke:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ dadjoke`\n‎"
      "‎ ‎ ‎ ‎ ・*Specialist dance 👀:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ specialist`\n‎"
      "‎ ‎ ‎ ‎ ・*Clap 👏👏👏:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ clap`\n‎"
      , 
      color=orange
      )
    embed4.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed5=discord.Embed(
      title='<:pai3:845141711373598741> __Informations:__', 
      description=
      "‎ ‎ ‎ ‎ ・*Userinfo:* shows you informations about a user\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ userinfo @user` / `+ userinfo`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n"
      "‎ ‎ ‎ ‎ ・*Avatar:* shows you informations about a user's avatar\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ avatar @user` / `+ avatar`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n"
      "‎ ‎ ‎ ‎ ・*Serverinfo:* shows you informations about the server\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ serverinfo`\n"
      "‎ ‎ ‎ ‎ ・*Servericon:* shows you the server icon\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ servericon`\n"
      "‎ ‎ ‎ ‎ ・*Permissions:* shows you the user's permissions in the server\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ perms` / `+ permissions`\n"
      "‎ ‎ ‎ ‎ ・*Botinfo:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ shows you informations about bot that verified on discord.bots.gg \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ botinfo <@bot>`", 
      color=orange
      )
    embed5.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed6=discord.Embed(
      title=' 🎨 __Miscellaneous:__', 
      description=
      "‎ ‎ ‎ ‎ ・*Help:* shows you this message\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ help`\n"
      "‎ ‎ ‎ ‎ ・*Calculate:* I'll count for you :3\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ calc <operation>` / `+ calculate <operation>`\n"
      "‎ ‎ ‎ ‎ ・*Picking out some choice:* I'll choose for you :3\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ choose <opt. 1>|<opt.2>|<opt.3>|<...>` /\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ pick <opt. 1>|<opt.2>|<opt.3>|<...>`\n"
      "‎ ‎ ‎ ‎ ・*Making regional texts:* simply turn `this` to 🇹 🇭 🇮 🇸\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ regional <text>`\n"
      "‎ ‎ ‎ ‎ ・*Reminder:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ reminder <time> <text>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example:`+ reminder 50m Cookies are ready!`\n"
      "‎ ‎ ‎ ‎ ・*Ping:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ ping`\n"
      "‎ ‎ ‎ ‎ ・*Bitcoin:* gives you the current price of bitcoin\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ bitcoin`\n"
      "‎ ‎ ‎ ‎ ・*Urban:* urban dictionary\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ urban <text>`\n"
      "‎ ‎ ‎ ‎ ・*Poll:* creates a poll where members can vote.\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ poll`\n"
      "‎ ‎ ‎ ‎ ・*Weather:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weather <city>`\n"
      "‎ ‎ ‎ ‎ ・*COVID-19:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ covid <country>`\n",
      color=orange
      )
    embed6.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed7=discord.Embed(
      title='🔈 __Voice Activity:__', 
      description=
      "‎ ‎ ‎ ‎ ・*Connect to a voice channel:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ join`\n"
      "‎ ‎ ‎ ‎ ・*Disconnect from a voice channel:*\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ leave`\n‎ ‎ ‎ ‎ ", 
      color=orange
      )
    embed7.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    embed8=discord.Embed(
      title='🧡__Support us 🧡__', 
      description="[Click here](https://ko-fi.com/childe_bot)", 
      color=orange
      )
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
    await paginator.run(embeds)

  @commands.command()
  async def gihelp(self, ctx):
    embed=discord.Embed(
      title="__Genshin Impact Commands:__", 
      description=
      "‎ ‎ ‎ ‎ ・*Artifact list:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ artifacts`\n"
      "‎ ‎ ‎ ‎ ・*Artifact info:* shows you informations about artifacts\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ artifact <art. name>` / `+ a <art. name>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example: `+a berserker`\n"
      "‎ ‎ ‎ ‎ ・*Weapon list:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weapons`\n"
      "‎ ‎ ‎ ‎ ・*Weapon info:* shows you informations about weapons\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weapon <weap. name>` / `+ w <weap. name>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example: `+w rust`\n"
      "‎ ‎ ‎ ‎ ・*Character list:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ characters`\n"
      "‎ ‎ ‎ ‎ ・*Character info:* shows you informations about characters\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ character <chara. name>` / `+ c <chara. name>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example: `+c tartaglia`\n"
      "‎ ‎ ‎ ‎ ・*Experience:* \n"
      "‎ ‎ ‎ ‎ ・*Nation info:* shows you informations about nations\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ nation <nation>`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example: `+nation mondstadt`\n"
      "‎ ‎ ‎ ‎ ・*Experience:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Info. about what you need for character's & weapon's exp\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ exp`\n"
      "‎ ‎ ‎ ‎ ・*Weekly Boss & Talent Books:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Weekly schedule for Character talent enhancement materials\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weekly` / `+ talent`\n"
      "‎ ‎ ‎ ‎ ・*Genshin Impact 2021 Calendar:* \n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ gi2021`\n", 
      color=orange
      )
    embed.set_thumbnail(
      url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935'
      )
    embed.set_footer(
      text=f"Serving: {ctx.author.name}", 
      icon_url=ctx.author.avatar_url
      )
    await ctx.send(embed=embed)

  @commands.command()
  async def modhelp(self, ctx):
    embed=discord.Embed(
      title="__Admins commands:__", 
      description=
      "‎ ‎ ‎ ‎ ***Moderations:***\n"
      "・warn @user\n"
      "・kick @user\n"
      "・ban @user\n"
      "・mute @user\n"
      "・unmute @user\n"
      "・nick @user <new nickname>\n\n"
      "‎ ‎ ‎ ‎ ***Making Embed:***\n"
      "・embed\n"
      "‎ ‎ ‎ ‎ `uses JSON`\n"
      "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <https://discohook.org/> \n\n"
      "‎ ‎ ‎ ‎ ***DM***\n"
      "・dm @user <value>\n\n"
      "‎ ‎ ‎ ‎ ***Delete Messages***\n"
      "・delete <# of messages>\n"
      "・delete <# of messages> @user\n"
      "‎ ‎ ‎ ‎ has a limit of 500 messages"
      , 
      color=orange
      )
    embed.set_thumbnail(
      url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935'
      )
    await ctx.send(embed=embed)

@commands.command()
async def ownerhelp(self, ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    embed=discord.Embed(
      title="__Hello, Luminette 🧡__", 
      description="My Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨", 
      color=orange)
    embed.set_thumbnail(
      url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935'
      )
    #on development
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Help(bot))

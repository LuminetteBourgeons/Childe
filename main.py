import discord
from discord.ext import commands, tasks
import DiscordUtils
from discord.ext.commands import CommandNotFound
import os, asyncio
from random import choice

#status         =841614719562285086
#commands       =841906846389764146
#commands-error =854589548864340009
#warn-log       =855287882965188628

orange=discord.Color.orange()

presence= [
  discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
  discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'ch! '")),
  discord.Activity(type=discord.ActivityType.playing, name=("✨new prefix: '+ '✨")),
  discord.Activity(type=discord.ActivityType.playing, name=("with Luminette")),
  discord.Activity(type=discord.ActivityType.competing, name=("ᴛᴀʀ-ᴛᴀʀ-ᴛᴀɢʟɪᴀ👋ʟᴏᴠᴇʀ❤️ᴏғ🤾sɴᴇᴢʜɴᴀʏᴀɴ🌟ǫᴜᴇᴇɴ🌸")),
  discord.Activity(type=discord.ActivityType.competing, name=("ᴛʜᴇʀᴇ🥰ᴡᴀs🔥ᴀ🌝ᴄᴀᴛ🐈ᴛʜᴀᴛ🐸ʀᴇᴀʟʟʏ👑ᴡᴀs✨ɢᴏɴᴇᴇᴇ🌈")),
  discord.Activity(type=discord.ActivityType.watching, name=("Luminette ❤️")),
  discord.Activity(type=discord.ActivityType.watching, name=("Minet bucin sm Mayo >:(")),
  discord.Activity(type=discord.ActivityType.watching, name=("Primordial World")),
  discord.Activity(type=discord.ActivityType.watching, name=("TompelL Official")),
  discord.Activity(type=discord.ActivityType.watching, name=("Ruko R0ixy")),
  discord.Activity(type=discord.ActivityType.listening, name=("Rasputin")),
  discord.Activity(type=discord.ActivityType.listening, name=("Tartagalicious~"))
]

colours = [
  discord.Colour(0x9b5de5), 
  discord.Colour(0xf15bb5), 
  discord.Colour(0xfee440), 
  discord.Colour(0x00bbf9), 
  discord.Colour(0x00f5d4)
  ]

PREFIX = [
  "Ch! ",
  "Ch!",
  "ch! ",
  "ch!",
  "+ ",
  "+"
]

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
  embed1=discord.Embed(title="__*Childe's commands:*__", description="Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n Use `+ about` for my informations!\n🧡 Develop by: <@743042741461712897> & <@809244553768861706>\n<:Chchibi:843379361138737182> With special helps from: <@421686337779793931>, <@236823518233362442>, & <@433919554004058112>\n<:PaimonHehe:843373207130079232> The next generation of __Paidoru__ (`Paimon#7192`) by <@533685396404568104>\n‎ ‎ ", color=orange)
  embed1.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
  embed1.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed2=discord.Embed(title="<:Chchibi:843379361138737182> __Invite me to your server!__ <:Chchibi:843379361138737182>", description="[Click here](https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot)\n*as Administrator*\n\n", color=orange)
  embed2.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
  embed2.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed3=discord.Embed(title='<:pai1:845141679102754836> __Genshin Impact:__', description="‎ ‎ ‎ ‎ ・*Artifact info:* shows you informations about artifacts\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ artifact <art. name>` / `+ a <art. name>`\n‎ ‎ ‎ ‎ ・*Weapon info:* shows you informations about weapons\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weapon <weap. name>` / `+ w <weap. name>`\n‎ ‎ ‎ ‎ ・*Experience:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Info. about what you need for character's & weapon's exp\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ exp`\n‎ ‎ ‎ ‎ ・*Weekly Boss & Talent Books:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Weekly schedule for Character talent enhancement materials\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ weekly` / `+ talent`", color=orange)
  embed3.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed4=discord.Embed(title='<:pai2:845141694541332481> __Fun:__', description="‎ ‎ ‎ ‎ ・*Rolling a dice:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ roll` / `+ dice`\n‎ ‎ ‎ ‎ ・*Flipping a coin:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ flip` / `+ coin`\n‎ ‎ ‎ ‎ ・*Ask 8ball:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ 8ball <question>` / `+ ball8 <question>`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > I will answer your yes/no question :)\n‎ ‎ ‎ ‎ ・*Rock, Paper, Scissors:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ rps`\n‎ ‎ ‎ ‎ ・*Tic Tac Toe:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ ttt`‎", color=orange)
  embed4.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed5=discord.Embed(title='<:pai3:845141711373598741> __Informations:__', description="‎ ‎ ‎ ‎ ・*Userinfo:* shows you informations about a user\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ userinfo @user` / `+ userinfo`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Avatar:* shows you informations about a user's avatar\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ avatar @user` / `+ avatar`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ > @user is optional\n‎ ‎ ‎ ‎ ・*Serverinfo:* shows you informations about the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ serverinfo`\n‎ ‎ ‎ ‎ ・*Servericon:* shows you the server icon\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ servericon`\n‎ ‎ ‎ ‎ ・*Permissions:* shows you the user's permissions in the server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ perms` / `+ permissions`", color=orange)
  embed5.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed6=discord.Embed(title=' 🎨 __Miscellaneous:__', description="‎ ‎ ‎ ‎ ・*Help:* shows you this message\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ help`\n‎ ‎ ‎ ‎ ・*Calculate:* I'll count for you :3\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ calc <operation>` / `+ calculate <operation>`\n‎ ‎ ‎ ‎ ・*Picking out some choice:* I'll choose for you :3\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ choose <opt. 1>|<opt.2>|<opt.3>|<...>` /\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ pick <opt. 1>|<opt.2>|<opt.3>|<...>`\n‎ ‎ ‎ ‎ ・*Making regional texts:* simply turn `this` to 🇹 🇭 🇮 🇸\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ regional <text>`\n‎ ‎ ‎ ‎ ・*Reminder:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ reminder <time> <text>`\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Example:`+ reminder 50m Cookies are ready!`\n‎ ‎ ‎ ‎ ・*Ping:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ ping`\n‎ ‎ ‎ ‎ ・*Bitcoin:* gives you the current price of bitcoin\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ bitcoin`\n‎ ‎ ‎ ‎ ・*Poll:* creates a poll where members can vote.\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ poll`", color=orange)
  embed6.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed7=discord.Embed(title='🔈 __Voice Activity:__', description="‎ ‎ ‎ ‎ ・*Connect to a voice channel:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ join`\n‎ ‎ ‎ ‎ ・*Disconnect from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `+ leave`\n‎ ‎ ‎ ‎ ", color=orange)
  embed7.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
  embed8=discord.Embed(title='🧡__Support us 🧡__', description="[Click here](https://ko-fi.com/childe_bot)", color=orange)
  paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
  paginator.add_reaction('⏮️', "first")
  paginator.add_reaction('⏪', "back")
  paginator.add_reaction('⏩', "next")
  paginator.add_reaction('⏭️', "last")
  embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
  await paginator.run(embeds)

@bot.command()
async def ownerhelp(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    embed=discord.Embed(title="__Hello, Luminette 🧡__", description="My Prefix: `Ch! `, `ch! `, ✨new prefix: `+`✨", color=orange)
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/gensin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/smart/width/250/height/250?cb=20210213163935')
    embed.add_field(name="__Your commands:__", value="Shows my active servers: `+servers`\nAuto presence changing: `+pstart` & `+pstop`\n", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def about(ctx):
  members_set = set()
  for guild in ctx.bot.guilds:
    for member in guild.members:
      members_set.add(member)
  members = len(members_set)
  embed=discord.Embed(title="__*Childe's information:*__", description=f"I'm No. 11 of the Fatui Harbingers, codename **Childe**, but I also go by Tartaglia. And you... Hmm, you too like to cause quite the stir, don't you? Something tells me we're going to get along splendidly. :)\n\nI'm on version 2.5\nFor more information about my commands, use `+ help`\nI'm now serving `{len(ctx.bot.guilds)}` servers, and `{members}` members!\n\n[Click here](https://github.com/LuminetteBourgeons/Childe) to see Luminette's github (don't forget the stars please 🧡🧡)\n[Click here](https://ko-fi.com/childe_bot) to treat me a coffee 🧡\n\n‎ ‎ \nPrefix: `Ch! `, `ch! `, ✨new prefix: `+`✨\n<:Chchibi:843379361138737182> Develop by: `Luminette#9566`, `Luminette#0103`\n<:Chchibi:843379361138737182> With special helps from: `Rin#5535`\n<:PaimonHehe:843373207130079232> The next generation of __Paidoru__ (`Paimon#7192`) by `Nawaytes~#2470`\n‎ ‎ ", color=orange)
  await ctx.send(embed=embed)

@bot.command()
async def invite (ctx):
  embed=discord.Embed(title="<:Chchibi:843379361138737182> __Invite me to your server!__ <:Chchibi:843379361138737182>", description="[Click here](https://discord.com/api/oauth2/authorize?client_id=806793987876192268&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1&scope=bot)\n*as Administrator*\n", color=orange)
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
  channel = bot.get_channel(841614719562285086)
  await channel.send('Rebooting')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=("Luminette")))
  print('Childe is online.')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.send(f'Command not found! Use `+help` for the list of commands!', delete_after=3)
    channel = bot.get_channel(854589548864340009)
    embed = discord.Embed(title=f"ERROR -- CommandNotFound", description=f"{ctx.message.content}",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
    return
  elif isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(title="Error!", description="You are missing the permission `" + ", ".join(error.missing_perms) + "` to execute this command!", color=discord.Colour.red())
    await ctx.send(embed=embed, delete_after=7)
    channel = bot.get_channel(854589548864340009)
    embed = discord.Embed(title=f"ERROR -- commands.MissingPermissions", description=f"{ctx.message.content}",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
  elif isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="Error!",description=str(error).capitalize(), color=discord.Colour.red())
    await ctx.send(embed=embed, delete_after=7)
    channel = bot.get_channel(854589548864340009)
    embed = discord.Embed(title=f"ERROR -- commands.MissingRequiredArgument", description=f"{ctx.message.content}",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
  elif isinstance(error, commands.ChannelNotFound):
    await ctx.send(f'Channel not found!', delete_after=7)
    channel = bot.get_channel(854589548864340009)
    embed = discord.Embed(title=f"ERROR -- commands.ChannelNotFound", description=f"{ctx.message.content}",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
    return
  elif isinstance(error, commands.MemberNotFound):
    await ctx.send(f'Member not found!', delete_after=7)
    channel = bot.get_channel(854589548864340009)
    embed = discord.Embed(title=f"ERROR -- commands.MemberNotFound", description=f"{ctx.message.content}",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
    return
  raise error

@bot.event
async def on_member_join(member):
    if member.guild.id == 786492151058923520:
      channel = bot.get_channel(845166313134882866)
      await channel.send("Welcome, {} :heart:".format (member.mention))
    elif member.guild.id == 271215379311886336:
      channel = bot.get_channel(834013759516573707)
      await channel.send("Welcome, {} :heart:".format (member.mention))
    elif member.guild.id == 738709993238560899:
      channel = bot.get_channel(765546060910166036)
      await channel.send("Met datang di Rumah Mine, {} :heart:".format (member.mention)) 
    elif member.guild.id == 747872613174608012:
      channel = bot.get_channel(747872613686181991)
      await channel.send("Selamat datang, {}! :D".format (member.mention))
    elif member.guild.id == 775568951101882398:
      channel = bot.get_channel(775568951412523010)
      embed=discord.Embed(title="<:paimonisfood:777925956630741043>",description="__ ׂׂૢ་༘࿐\n┊ ⋆ ┊ . ┊ ┊\n┊ ┊⋆ ┊ .\n┊ ┊ ⋆˚ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭\n✧. ┊ ⁭ ⁭ ⁭ ⁭ \n⁭ ⁭ ⁭ ⁭ ⁭⋆ ★\n⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒\n‹·˚ 𝐓𝐨𝐦𝐩𝐞𝐥𝐋 𝐃𝐢𝐬𝐜𝐨𝐫𝐝 𝐒𝐞𝐫𝐯𝐞𝐫 〄⋆̩\n︶︶︶︶︶︶︶︶︶︶︶︶︶︶ ೄྀ࿐ ˊ\n<:paimonisfood:777925956630741043> \n╰┈➤ Silahkan untuk ambil role , ada di <#775634842247364619> untuk menunjukkan sedikit informasi tentang dirimu, jadi member lain bisa kenal kamu lebih dekat 😉\n<:loveu:777925956379607080> \n╰┈➤ Mohon untuk membaca <#831462974011080734> agar kamu memahami peraturan yang berlaku di server TompelL.\n\n────────────────────────────────────────\n<:yaws:777925956257972234> Terima kasih! <:yaws:777925956257972234>\n")
      await channel.send("Selamat datang di **Server Discord TompelL**, {} :heart:. <:ooogitu:813675925287469096> Silahkan untuk baca text dibawah ini ⬎".format (member.mention), embed=embed)
    else:
      return

@bot.event
async def on_message(message):
    if message.author == bot.user:
      return
    await bot.process_commands(message)
    if message.content.lower().startswith('childe?'):
      await message.channel.send('Hey girlie, hold still')
      await bot.process_commands(message)
    if message.type.name in ['premium_guild_subscription', 'premium_guild_tier_1', 'premium_guild_tier_2', 'premium_guild_tier_3']:
      if message.guild.id == 775568951101882398:
        embed = discord.Embed( colour=orange,description=f"**{message.author.name}**, Terimakasih telah boost server kami! <:02love:852123836366323712>")
        channel = bot.get_channel(775580161897660436)
        await channel.send(embed=embed)
        await bot.process_commands(message)

@bot.event
async def on_command(ctx):
  channel = bot.get_channel(841906846389764146)
  embed = discord.Embed(title=f"<:Chchibi:843379361138737182> {ctx.author.name} used a command!", description=f"{ctx.message.content}",colour=discord.Color.orange())
  await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
@bot.event
async def on_command_completion(ctx):
  channel = bot.get_channel(841906846389764146)
  embed = discord.Embed(title=f"<:Chchibi:843379361138737182> Completed {ctx.author.name}'s command!", description=f"{ctx.message.content}",colour=discord.Color.gold())
  await channel.send(embed=embed)

@bot.command()
async def specialist (ctx):
  await ctx.send("https://imgur.com/CDfXufV")

@bot.command(aliases=['echo'])
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def servers(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.send("<:Chchibi:843379361138737182>__**Childe's active servers:**__<:Chchibi:843379361138737182>")
    activeservers = bot.guilds
    for guild in activeservers:
      await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\nOwner ID :`{guild.owner.id}`\nMembers: `{guild.member_count}`')
      await ctx.send('––––––––––––––––––––––––––––––––––––––––––––––––')

@tasks.loop(minutes=5)
async def presence_change():
  await asyncio.sleep(10)
  await bot.change_presence(activity=choice(presence))
  channel = bot.get_channel(841614719562285086)
  await channel.send('Changing Presence')
  print("Changing Presence")
@presence_change.before_loop
async def presence_change_before():
  await bot.wait_until_ready()
@bot.command()
async def pstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.start()
    await ctx.send("Auto presence-changing started.")
  else:
    await ctx.send("You are not allowed to use this command!")
@bot.command()
async def pstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.cancel()
    await ctx.send("Auto presence-changing has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")

@tasks.loop(seconds=2)
async def role_colour_change():
  await role_to_change.edit(colour=choice(colours))
  channel = bot.get_channel(841614719562285086)
  await channel.send('Changing Role Colour')
@role_colour_change.before_loop
async def colour_change_before():
  global role_to_change
  await bot.wait_until_ready()
  guild = bot.get_guild(775568951101882398)
  role_name = "🎀Bot Dev"
  role_to_change = discord.utils.get(guild.roles, name=role_name)
@bot.command()
async def rcstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    role_colour_change.start()
    await ctx.send("Auto role's colour changing has started.")
  else:
    await ctx.send("You are not allowed to use this command!")
@bot.command()
async def rcstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    role_colour_change.cancel()
    await ctx.send("Auto role's colour changing has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")


extensions = [
  'cogs.genshin', 
  'cogs.miscellaneous', 
  'cogs.mod', 
  'cogs.reminder', 
  'cogs.voice', 
  'cogs.info', 
  'cogs.fun',    
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
bot.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands
import json, asyncio

orange=discord.Color.orange()

class Mod(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def embed(self, ctx):
    await ctx.message.delete()
    await ctx.send('Waiting for your JSON embed... `timeout in 60 seconds.`', delete_after=5)
    message = await self.bot.wait_for('message', timeout=60)
    try:
      f = json.loads(str(message.content))
      embed = discord.Embed.from_dict(f)
      await asyncio.sleep(2)
      await message.delete()
      await ctx.send(embed=embed)
    except json.JSONDecodeError:
      await message.delete()
      await ctx.send('JSON ERROR', delete_after=1)
      return

  @commands.command(aliases=['purge'])
  @commands.has_permissions(manage_messages=True, manage_channels=True)
  async def delete(self, ctx, limit=500, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
      limit = int(limit)
    except:
      await ctx.send("Please pass in an integer as limit")
      return
    if limit < 1:
      ctx.send("Please specify how much messages you want to purge!", delete_after=4)
      return
    if not member:
      await ctx.channel.purge(limit=limit)
      return await ctx.send(f"Deleted {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
      if len(msg) == limit:
          break
      if m.author == member:
          msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Deleted {limit} messages of {member.mention}", delete_after=3)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def dm(self,ctx, user: discord.User, *, value):
    await user.send(f"**{value}**")
    await user.send(f"||Sent by {ctx.author.name}||")
    await ctx.send("DM sent!")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def warn(self, ctx, member: discord.Member, *, reason="Not specified"):
    embed = discord.Embed(title="User Warned!", description=f"**{member}** was warned by **{ctx.message.author}**!", color=orange)
    embed.add_field(name="Reason:",value=reason)
    await ctx.send(embed=embed)
    try:
      await member.send(f"You were warned by **{ctx.message.author}**!\nReason: {reason}")
    except:
      pass
    channel = ctx.bot.get_channel(855287882965188628)
    embed = discord.Embed(title=f"WARNED", description=f"{member}\nReason: {reason}\nBy:",colour=discord.Color.red())
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="Not specified"):
    if member.guild_permissions.administrator:
      embed = discord.Embed(title="Error!",description="User is an Admin", color=discord.Colour.red())
      await ctx.send(embed=embed)
    else:
      try:
        await member.kick(reason=reason)
        embed = discord.Embed(title="User Kicked!",description=f"**{member}** was kicked by **{ctx.message.author}**!",color=orange)
        embed.add_field(name="Reason:", value=reason)
        await ctx.send(embed=embed)
        try:
          await member.send(f"You were kicked by **{ctx.message.author}**!\nReason: {reason}")
        except:
          pass
      except:
        embed = discord.Embed(title="Error!", description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",color=discord.Colour.red())
        await ctx.message.channel.send(embed=embed)
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="Not specified"):
    if member.guild_permissions.administrator:
      embed = discord.Embed(title="Error!",description="User is an Admin", color=discord.Colour.red())
      await ctx.send(embed=embed)
    else:
      try:
        await member.ban(reason=reason)
        embed = discord.Embed(title="User Banned!",description=f"**{member}** was banned by **{ctx.message.author}**!",color=orange)
        embed.add_field(name="Reason:", value=reason)
        await ctx.send(embed=embed)
        try:
          await member.send(f"You were banned by **{ctx.message.author}**!\nReason: {reason}")
        except:
          pass
      except:
        embed = discord.Embed(title="Error!", description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to kick.",color=discord.Colour.red())
        await ctx.message.channel.send(embed=embed)
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member: discord.Member):
    if member.guild.id == 775568951101882398:
      role = discord.utils.get(ctx.guild.roles, name="🤫 Shh, MUTED!")
      await member.add_roles(role)
      await ctx.send(f"Muted {member} >:D")
    else:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"Muted {member} >:D")
      else:
        await member.add_roles(role) 
        await ctx.send(f"Muted {member} >:D")
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unmute(self, ctx, member: discord.Member):
    if member.guild.id == 775568951101882398:
      role = discord.utils.get(ctx.guild.roles, name="🤫 Shh, MUTED!")
      await member.remove_roles(role)
      await ctx.send(f"Unmuted {member}")
    else:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.remove_roles(role)
        await ctx.send(f"Unmuted {member}")
      else:
        await member.remove_roles(role) 
        await ctx.send(f"Unmuted {member}")

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  async def nick(self, ctx, member: discord.Member, *, nickname=None):
    try:
      await member.edit(nick=nickname)
      embed = discord.Embed(title="Changed Nickname!", description=f"**{member}'s** new nickname is **{nickname}**!", color=orange)
      await ctx.send(embed=embed)
    except:
      embed = discord.Embed(title="Error!", description="An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.", color=orange)
      await ctx.message.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Mod(bot))

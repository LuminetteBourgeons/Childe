import discord
from discord.ext import commands
import random, asyncio

orange=discord.Color.orange()

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

class Fun(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.ball = [
        'It is certain', 
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
        'Very doubtful'
        ]

  @commands.command(aliases=['roll'])
  async def dice(self, ctx):
    dice6=["1","2","3","4","5","6"]
    await ctx.send("Rolling the dice~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"<:Chchibi:843379361138737182> Rolled a dice! 🎲", description=f"It landed on {random.choice(dice6)}!",colour=orange)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['flip'])
  async def coin(self, ctx):
    coin2=["head","tail"]
    childe=[
      "Well, I'd choose head though...",
      "Well, I'd choose tail though...",
      "Do you believe on that?",
      "",
      "",
      "",
      "And you landed on my heart ;)"
      ]
    await ctx.send("Flipping the coin~", delete_after=3)
    await asyncio.sleep(3)
    embed = discord.Embed(title=f"<:Chchibi:843379361138737182> Flipped a coin! 🪙", description=f"It landed on {random.choice(coin2)}. {random.choice(childe)}",colour=orange)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['8ball'])
  async def ball8(self, ctx, *, msg: str):
    await ctx.send("Let ~~my~~ **8**ball decide your fate ;D")
    answer = random.randint(0, 19)
    embed = discord.Embed(color=orange)
    embed.add_field(name='\u2753 Question', value=msg)
    embed.add_field(name='\ud83c\udfb1 8ball', value=self.ball[answer], inline=False)
    embed.set_footer(text=f"Serving: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def rps(self, ctx):
    rps = ['rock', 'paper', 'scissors']
    await ctx.send(f"Let's play rock, paper, scissors with me 🧡\nSo rock, paper, or scissors? Choose wisely...")
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rps
    user_choice = (await self.bot.wait_for('message', check=check)).content.lower()
    comp_choice = random.choice(rps)
    if user_choice == 'rock':
      if comp_choice == 'rock':
        await ctx.send(f'Well, that was weird. We tied...\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Nice try, comrade ;)\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Aw, you beat me. It won't happen again!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    elif user_choice == 'paper':
      if comp_choice == 'rock':
        await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Aw man, you actually managed to beat me.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    elif user_choice == 'scissors':
      if comp_choice == 'rock':
        await ctx.send(f'HAHA!! I JUST CRUSHED YOU!!\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'paper':
        await ctx.send(f'Hmph, nice one girlie.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`')
      elif comp_choice == 'scissors':
        await ctx.send(f"Oh well, we tied.\n> Your choice: `{user_choice}`\n> My choice: `{comp_choice}`")
    else:
      await ctx.send(f"Uh, I told you to choose rock, paper, or scissors...")

  @commands.command(aliases=['ttt'])
  async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
      global count
      global player1
      global player2
      global turn
      global gameOver
      if gameOver:
          global board
          board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:", ":white_large_square:", ":white_large_square:"]
          turn = ""
          gameOver = False
          count = 0
          player1 = p1
          player2 = p2
          # print the board
          line = ""
          for x in range(len(board)):
              if x == 2 or x == 5 or x == 8:
                  line += " " + board[x]
                  await ctx.send(line)
                  line = ""
              else:
                  line += " " + board[x]
          # determine who goes first
          num = random.randint(1, 2)
          if num == 1:
              turn = player1
              await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
          elif num == 2:
              turn = player2
              await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
      else:
          await ctx.send("A game is already in progress! Finish it before starting a new one.")
  def checkWinner(winningConditions, mark):
      global gameOver
      for condition in winningConditions:
          if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
              gameOver = True
  @commands.command()
  async def place(self, ctx, pos: int):
      global turn
      global player1
      global player2
      global board
      global count
      global gameOver
      if not gameOver:
          mark = ""
          if turn == ctx.author:
              if turn == player1:
                  mark = ":regional_indicator_x:"
              elif turn == player2:
                  mark = ":o2:"
              if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                  board[pos - 1] = mark
                  count += 1
                  # print the board
                  line = ""
                  for x in range(len(board)):
                      if x == 2 or x == 5 or x == 8:
                          line += " " + board[x]
                          await ctx.send(line)
                          line = ""
                      else:
                          line += " " + board[x]
                  def checkWinner(winningConditions, mark):
                    global gameOver
                    for condition in winningConditions:
                        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                            gameOver = True
                  checkWinner(winningConditions, mark)
                  print(count)
                  if gameOver == True:
                      await ctx.send(mark + " wins!")
                  elif count >= 9:
                      gameOver = True
                      await ctx.send("It's a tie!")
                  # switch turns
                  if turn == player1:
                      turn = player2
                  elif turn == player2:
                      turn = player1
              else:
                  await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
          else:
              await ctx.send("It is not your turn.")
      else:
          await ctx.send("Please start a new game using the !tictactoe command.")
  @tictactoe.error
  async def tictactoe_error(self, ctx, error):
      print(error)
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please mention 2 players for this command.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send("Please make sure to mention/ping players")
  @place.error
  async def place_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("Please enter a position you would like to mark.")
      elif isinstance(error, commands.BadArgument):
          await ctx.send("Please make sure to enter an integer.")

def setup(bot):
  bot.add_cog(Fun(bot))

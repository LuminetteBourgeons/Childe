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

    @commands.command()
    async def rps(self, ctx):
      rpsGame = ['rock', 'paper', 'scissors']
      await ctx.send(f"Let's play rock, paper, scissors with me 🧡 :D. So rock, paper, or scissors? Choose wisely...")
      def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
      user_choice = (await self.bot.wait_for('message', check=check)).content
      comp_choice = random.choice(rpsGame)
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

'''
    @commands.command()
    async def ttt(self, ctx, move=""):
      """ Tic Tac Toe """
      await self.ttt_new(ctx.message.author, ctx.message.channel)

    async def ttt_new(self, user, channel):
      self.ttt_games[user.id] = [" "]*9
      response = self.ttt_make_board(user)
      response += "Your move:"
      msg = await self.bot.send_message(channel, response)
      await self.makeButtons(msg)
    
    async def ttt_move(self, user, message, move):
      print("ttt_move:{0}".format(user.id))
      # Check user currently playing
      uid = user.id
      if uid not in self.ttt_games:
        print("New game")
        return await self.ttt_new(user, message.channel)
      
      # Check spot is empty
      if self.ttt_games[uid][move] == " ":
        self.ttt_games[uid][move] = "x"
        print("Moved to {0}".format(move))
      else:
        print("Invalid move: {0}".format(move))
        return None
      
      # Check winner
      check = self.tttDoChecks(self.ttt_games[uid])
      if check is not None:
        msgAppend = "It's a draw!" if check == "draw" else "{0} wins!".format(check[-1])
        print(msgAppend)
        await self.bot.edit_message(message, new_content="{0}{1}".format(self.ttt_make_board(user), msgAppend))
        return None
      print("Check passed")
      
      # AI move
      mv = self.tttAIThink(self.tttMatrix(self.ttt_games[uid]))
      self.ttt_games[uid][self.tttCoordsToIndex(mv)] = "o"
      print("AI moved")
      
      # Update board
      await self.bot.edit_message(message, new_content=self.ttt_make_board(user))
      print("Board updated")
      
      # Check winner again
      check = self.tttDoChecks(self.ttt_games[uid])
      if check is not None:
        msgAppend = "It's a draw!" if check == "draw" else "{0} wins!".format(check[-1])
        print(msgAppend)
        await self.bot.edit_message(message, new_content="{0}{1}".format(self.ttt_make_board(user), msgAppend))
      print("Check passed")
    
    def ttt_make_board(self, author):
      return "{0}\n{1}\n".format(author.mention, self.tttTable(self.ttt_games[author.id]))
    
    async def makeButtons(self, msg):
      await self.bot.add_reaction(msg, u"\u2196") # 0 tl
      await self.bot.add_reaction(msg, u"\u2B06") # 1 t
      await self.bot.add_reaction(msg, u"\u2197") # 2 tr
      await self.bot.add_reaction(msg, u"\u2B05") # 3 l
      await self.bot.add_reaction(msg, u"\u23FA") # 4 mid
      await self.bot.add_reaction(msg, u"\u27A1") # 5 r
      await self.bot.add_reaction(msg, u"\u2199") # 6 bl
      await self.bot.add_reaction(msg, u"\u2B07") # 7 b
      await self.bot.add_reaction(msg, u"\u2198") # 8 br
    
    async def on_reaction_add(self, reaction, user):
      if reaction.message.author.id == self.bot.user.id and not user.id == self.bot.user.id:
        move = self.decodeMove(str(reaction.emoji))
        if move is not None:
          await self.ttt_move(user, reaction.message, move)
    
    def decodeMove(self, emoji):
      dict = {
        u"\u2196": 0,
        u"\u2B06": 1,
        u"\u2197": 2,
        u"\u2B05": 3,
        u"\u23FA": 4,
        u"\u27A1": 5,
        u"\u2199": 6,
        u"\u2B07": 7,
        u"\u2198": 8
      }
      return dict[emoji] if emoji in dict else None

    # Utility Functions
    def tttTable(self, xo):
      return (("%s%s%s\n"*3) % tuple(xo)).replace("o", ":o2:").replace("x", ":regional_indicator_x:").replace(" ", ":white_large_square:")
    
    def tttMatrix(self, b):
      return [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]]
      ]
    def tttCoordsToIndex(self, coords):
      # it's midnight, can't think. will improve later
      map = {
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 2,
        (1, 0): 3,
        (1, 1): 4,
        (1, 2): 5,
        (2, 0): 6,
        (2, 1): 7,
        (2, 2): 8
      }
      return map[coords]
    
    def tttDoChecks(self, b):
      m = self.tttMatrix(b)
      if self.tttCheckWin(m, "x"):
        return "win X"
      if self.tttCheckWin(m, "o"):
        return "win O"
      if self.tttCheckDraw(b):
        return "draw"
      return None
    
    # The following comes from an old project
    # https://gist.github.com/HizkiFW/0aadefb73e71794fb4a2802708db5bcf
    # <snippet>
    def tttFindStreaks(self, m, xo):
      row = [0, 0, 0]
      col = [0, 0, 0]
      dia = [0, 0]
      
      # Check rows and columns for X streaks
      for y in range(3):
        for x in range(3):
          if m[y][x] == xo:
            row[y] += 1
            col[x] += 1
      
      # Check diagonals
      if m[0][0] == xo:
        dia[0] += 1
      if m[1][1] == xo:
        dia[0] += 1
        dia[1] += 1
      if m[2][2] == xo:
        dia[0] += 1
      if m[2][0] == xo:
        dia[1] += 1
      if m[0][2] == xo:
        dia[1] += 1
        
      return (row, col, dia)
    
    def tttFindEmpty(self, matrix, rcd, n):
      # Rows
      if rcd == "r":
        for x in range(3):
          if matrix[n][x] == " ":
            return x
      # Columns
      if rcd == "c":
        for x in range(3):
          if matrix[x][n] == " ":
            return x
      # Diagonals
      if rcd == "d":
        if n == 0:
          for x in range(3):
            if matrix[x][x] == " ":
              return x
        else:
          for x in range(3):
            if matrix[x][2-x] == " ":
              return x
      
      return False
    
    def tttCheckWin(self, m, xo):
      row, col, dia = self.tttFindStreaks(m, xo)
      dia.append(0)
      
      for i in range(3):
        if row[i] == 3 or col[i] == 3 or dia[i] == 3:
          return True
      
      return False
    
    def tttCheckDraw(self, board):
      return not " " in board
    
    # Don't touch anything here. I forgot how it worked, it just does.
    def tttAIThink(self, m):
      rx, cx, dx = self.tttFindStreaks(m, "x")
      ro, co, do = self.tttFindStreaks(m, "o")
      
      mv = self.tttAIMove(2, m, ro, co, do)
      if mv is not False:
        return mv
      mv = self.tttAIMove(2, m, rx, cx, dx)
      if mv is not False:
        return mv
      mv = self.tttAIMove(1, m, ro, co, do)
      if mv is not False:
        return mv
      return self.tttAIMove(1, m, rx, cx, dx)
    
    def tttAIMove(self, n, m, row, col, dia):
      for r in range(3):
        if row[r] == n:
          x = self.tttFindEmpty(m, "r", r)
          if x is not False:
            return (r, x)
        if col[r] == n:
          y = self.tttFindEmpty(m, "c", r)
          if y is not False:
            return (y, r)
      
      if dia[0] == n:
        y = self.tttFindEmpty(m, "d", 0)
        if y is not False:
          return (y, y)
      if dia[1] == n:
        y = self.tttFindEmpty(m, "d", 1)
        if y is not False:
          return (y, 2-y)
      return False
'''

def setup(bot):
  bot.add_cog(Fun(bot))

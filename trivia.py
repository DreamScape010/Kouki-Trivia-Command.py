class Trivia(View):
  def __init__(self, ctx, correct, msg):
    super().__init__(timeout=30)
    self.correct = correct
    self.ctx = ctx
    self.message = msg
  @nextcord.ui.button(label="A", style=ButtonStyle.blurple, custom_id="A")
  async def a_callback(self, button, interaction):
    if interaction.user != self.ctx.author:
      await interaction.response.send_message("It's not your trivia session.")
      return
    button = [x for x in self.children if button.custom_id == "A"][0]
    if button.custom_id == self.correct:
      users = await get_bank_data()
      users[str(interaction.user.id)]['wallet'] += 10000
      with open('bank_data.json','w') as f:
        users = json.dump(users,f)
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.success
      await interaction.response.edit_message(content = f"Correct! You got 10000{emoji}", view=self)
    else:
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.danger
      await interaction.response.edit_message(content = f"You lost! The correct answer was {self.correct} option", view=self)
      
  @nextcord.ui.button(label="B", style=ButtonStyle.blurple, custom_id="B")
  async def b_callback(self, button, interaction):
    if interaction.user != self.ctx.author:
      await interaction.response.send_message("It's not your trivia session.")
      return
    button = [x for x in self.children if button.custom_id == "B"][1]
    if button.custom_id == self.correct:
      users = await get_bank_data()
      users[str(interaction.user.id)]['wallet'] += 10000
      with open('bank_data.json','w') as f:
        users = json.dump(users,f)
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.success
      await interaction.response.edit_message(content = f"Correct! You got 10000{emoji}", view=self)
    else:
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.danger
      await interaction.response.edit_message(content = f"You lost! The correct answer was {self.correct} option", view=self)
  
  @nextcord.ui.button(label="C", style=ButtonStyle.blurple, custom_id="C")
  async def c_callback(self, button, interaction):
    if interaction.user != self.ctx.author:
      await interaction.response.send_message("It's not your trivia session.")
      return
    button = [x for x in self.children if button.custom_id == "C"][2]
    if button.custom_id == self.correct:
      users = await get_bank_data()
      users[str(interaction.user.id)]['wallet'] += 10000
      with open('bank_data.json','w') as f:
        users = json.dump(users,f)
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.success
      await interaction.response.edit_message(content = f"Correct! You got 10000{emoji}", view=self)
    else:
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.danger
      await interaction.response.edit_message(content = f"You lost! The correct answer was {self.correct} option", view=self)

  @nextcord.ui.button(label="D", style=ButtonStyle.blurple, custom_id="D")
  async def d_callback(self, button, interaction):
    if interaction.user != self.ctx.author:
      await interaction.response.send_message("It's not your trivia session.")
      return
    button = [x for x in self.children if button.custom_id == "D"][3]
    if button.custom_id == self.correct:
      users = await get_bank_data()
      users[str(interaction.user.id)]['wallet'] += 10000
      with open('bank_data.json','w') as f:
        users = json.dump(users,f)
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.success
      await interaction.response.edit_message(content = f"Correct! You got 10000{emoji}", view=self)
    else:
      for children in self.children:
        children.disabled = True
        children.style = ButtonStyle.grey
      button.style = ButtonStyle.danger
      await interaction.response.edit_message(content = f"You lost! The correct answer was {self.correct} option", view=self)
  async def on_timeout(self):
    for children in self.children:
      children.disabled = True
      children.style = ButtonStyle.grey
    await self.message.edit(view=self)
    self.stop()
      
@client.command(aliases=['tr','triv','tri','quiz'])
async def trivia(ctx):
  #Pulling request from trivia api
  url = requests.get('https://the-trivia-api.com/api/questions')
  data = url.json()
  #Getting the necessary variables
  category = data[0]['category']
  difficulty = data[0]['difficulty'].capitalize()
  question = data[0]['question']
  correct = data[0]['correctAnswer']
  incorrect = data[0]['incorrectAnswers']
  #Getting a random alphabet
  no = ['A','B','C','D']
  alpha = random.choice(no)
  #printing it
  print(alpha)
  incorrect1 = incorrect[0]
  incorrect2 = incorrect[1]
  incorrect3 = incorrect[2]
  #Assigning the correct answer of trivia to the alphabets
  if alpha == 'A':
    correctopt = "A"
    description=f'A : {correct}\nB : {incorrect1}\nC : {incorrect2}\nD : {incorrect3}'
  elif alpha == 'B':
    correctopt = "B"
    description=f'A : {incorrect1}\nB : {correct}\nC : {incorrect2}\nD : {incorrect3}'
  elif alpha == 'C':
    correctopt = "C"
    description=f'A : {incorrect1}\nB : {incorrect2}\nC : {correct}\nD : {incorrect3}'
  else:
    correctopt = "D"
    description=f'A : {incorrect1}\nB : {incorrect2}\nC : {incorrect3}\nD : {correct}'
  #building the embed message
  embed = discord.Embed(title=question,description=description,color=discord.Color.random())
  embed.add_field(name="Difficulty",value=f"`{difficulty}`")
  embed.add_field(name="Category",value=f"`{category}`")
  msg = await ctx.send(embed=embed)
  view = Trivia(ctx, alpha, msg)
  await msg.edit(embed=embed, view=view)
  #Done!

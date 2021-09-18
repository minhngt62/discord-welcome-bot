import discord
import os
from keep_alive import keep_alive

class MyClient(discord.Client):
  async def on_ready(self):
      print('Logged in as')
      print(self.user.name)
      print(self.user.id)
      print('------')

  async def on_member_join(self, member):
    logs_channel = client.get_channel(887732635210764319)
    await logs_channel.send("Greetings to you, " + member.mention + "! Please go to " + client.get_channel(887887332181696562).mention + " for self identication")
  
  async def on_member_remove(self, member):
    logs_channel = client.get_channel(887732635210764319)
    await logs_channel.send("It was a good time. Farewell, " + member.mention + "!")

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
keep_alive()
client.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
/help - Comandos del bot
/clear x - Borrar cantidad de mensajes donde "x" es la cantidad

Music commands:
/play <palabras> - Buscar canciones en Youtube
/queue - Lista de reproucción
/skip - Saltar canción de la lista
```
"""
        self.text_channel_list = []

    #Info debug    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Clears a specified amount of messages")
    async def clear(self, ctx, arg):
        #Monto a borrar
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)

    @commands.command(name = 'massdm', pass_context=True)
    async def dm(ctx, message):
      guild = ctx.message.guild
      for member in guild.members:
        try:
            await member.send(message)
            await ctx.send("Sent message")
        except:
            await ctx.send("Error")
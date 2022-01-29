import discord
from discord.ext import commands

import os

#importamos todos los modulos
from main_cog import main_cog
from image_cog import image_cog
from music_cog import music_cog
from test_cog import test_cog


bot = commands.Bot(command_prefix='/')

#remover comando help
bot.remove_command('help')

#registrando los modulos del bot
bot.add_cog(main_cog(bot))
#bot.add_cog(image_cog(bot))
bot.add_cog(music_cog(bot))
bot.add_cog(test_cog(bot))

#partir bot
bot.run("OTM2ODY2MjgxMzU1ODc4NDIw.YfTatw.6QRJhvcLExAQh9PRa5xhDFwHM6s")
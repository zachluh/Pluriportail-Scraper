import discord
from discord.ext import commands
from Pluribotrepo import login
from Pluribotrepo import bot
from user import user
import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys

class session(commands.Cog):

    
    
    @commands.command()
    async def plurilogin(self, ctx):
        loggeduser = user(bot, ctx.author)
        

def setup(bot):
    bot.add_cog(session(bot))




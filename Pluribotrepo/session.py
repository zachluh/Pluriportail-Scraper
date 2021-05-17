import discord
from discord.ext import commands
from Pluribotrepo import login
from Pluribotrepo import bot
from user import user
import selenium
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from Pluribotrepo import login, driver

class session(commands.Cog):

    def __init__(self, driver): 
        self.driver = driver
    
    @commands.command()
    async def plurilogin(self, ctx):
        loggeduser = user(bot, ctx.author)
        new_login = (await loggeduser.user_login_creation(ctx))
        print(new_login)

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        login(self.driver, new_login[0], new_login[1])
        

def setup(bot):
    bot.add_cog(session(driver))




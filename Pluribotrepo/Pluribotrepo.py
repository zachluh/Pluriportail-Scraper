import discord
import selenium
import calendar
from discord.ext.commands import Bot
from datetime import date
import datetime
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import os
from user import user
import session
import time

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True

classes = []

#classes here
class Embeds():
    def __init__(self):
        pass
    def getScheduleEmbed(self, class_list, tomorrow):
        embed = discord.Embed(
                title = f"Your schedule for {tomorrow} is:",
                description = "\n".join(class_list),
                color = discord.Color.green()
            )
        embed.set_thumbnail(url="https://store-images.s-microsoft.com/image/apps.3640.13510798887684659.37ddc7c7-7c13-48db-b3df-cfbdf6bb7f5c.ef84f088-428e-43d1-b45b-07da23f43efc?mode=scale&q=90&h=300&w=300")
        return embed




embedder = Embeds()

#make sure to change the path
PATH = r"C:\Users\bruhm\Desktop\chromedriver\chromedriver.exe"

driver = wb.Chrome(PATH)

today = date.today()
tomorrow = calendar.day_name[(date.today() + datetime.timedelta(1)).weekday()]
weekday = calendar.day_name[today.weekday()]


def login(driver, user:str, password:str):
    driver.get("https://portail.sainteanne.ca/pluriportail/fr/MainExterne.srf?P=LoginReq")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="NomLogin"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="MotPasse"]').send_keys(password, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="MainAgenda"]').click()

def day_switcher(day):
    switcher = {
            'Monday': [6, 11],
            'Tuesday': [11, 15],
            'Wednesday': [15, 20],
            'Thursday':  [20, 25],
            'Friday': [1, 6],
            'Saturday': [1, 6],
            'Sunday': [1, 6]
        }
    return switcher.get(day, "dumbass")

day_array = day_switcher(weekday)
print(day_array)




    

with open(r"C:\Users\bruhm\Documents\pluricreds.txt", "r") as f:
    credslist = f.readlines()

bot = Bot(command_prefix="pl!")
bot.load_extension('session')


@bot.event
async def on_ready():
    print("lets go")
    await bot.change_presence(activity=discord.Game(name="the system // pl!"))
    
    login(driver, credslist[1], credslist[2])
    for i in range(day_array[0], day_array[1]):
        stri = str(i)
        classes.append(driver.find_element_by_xpath(f'//*[@id="CaseItem{stri}"]/div/div[1]').text)
    channel = bot.get_channel(812332956101509130)
    message = await channel.fetch_message(812333382540984412)
    if message is None:
        await channel.send(embed=embedder.getScheduleEmbed(classes, tomorrow))
    else:
        await message.edit(embed=embedder.getScheduleEmbed(classes, tomorrow))

@bot.command()
async def registeraccount(ctx, name, password):
    author_id = ctx.author
    await ctx.send("ok, im gonna resend a message with your creds so i can remember them, thanks")
    message = await ctx.send(f"{name} {password}")
    new_user =  user(bot, ctx.author)
    await new_user.create_new_profile(ctx, message)



bot.run(f"{credslist[0]}")






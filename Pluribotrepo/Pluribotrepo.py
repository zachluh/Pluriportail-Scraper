import discord
import selenium
import calendar
from discord.ext.commands import Bot
from datetime import date
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import os

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True

classes = []

PATH = r"C:\Users\bruhm\Desktop\chromedriver\chromedriver.exe"

today = date.today()
weekday = calendar.day_name[today.weekday()]


def login(driver, user:str, password:str):
    driver.get("https://portail.sainteanne.ca/pluriportail/fr/MainExterne.srf?P=LoginReq")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="NomLogin"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="MotPasse"]').send_keys(password, Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="MainAgenda"]').click()

def day_switcher(day):
    switcher = {
            'Monday': [1, 6],
            'Tuesday': [6, 11],
            'Wednesday': [11, 15],
            'Thursday':  [15, 21],
            'Friday': [21, 26]
        }
    return switcher.get(day, "dumbass")

day_array = day_switcher(weekday)
print(day_array)
print(day_array[0])




    

with open(r"C:\Users\bruhm\Documents\pluricreds.txt", "r") as f:
    credslist = f.readlines()

bot = Bot(command_prefix="pl!")


@bot.event
async def on_ready():
    print("lets go")
    driver = wb.Chrome(PATH)
    login(driver, credslist[1], credslist[2])
    channel = bot.get_channel(811659339559075890)
    for i in range(day_array[0], day_array[1]):
        stri = str(i)
        classes.append(driver.find_element_by_xpath(f'//*[@id="CaseItem{stri}"]/div/div[1]').text)
    await channel.send(" ".join(classes))



bot.run(f"{credslist[0]}")






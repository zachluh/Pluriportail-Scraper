import discord
from discord.ext import commands

class user(commands.Cog):
    """Pluriportail user profile"""

    def __init__(self, bot, credmessage, discord_user):
        self.bot = bot
        self.credmessage = credmessage
        self.discord_user = discord_user

    async def create_new_profile(self, ctx, message_id=credmessage.id):

       message = await bot.fetch_message(message_id)

       with open(f"{str(discord_user.id)}.txt", "w") as f:
           f.write(message_id)
           
    async def user_login_creation():
        with open(f"{str(discord_user.id)}.txt", "r") as f:
            creds = f.read()

        final_creds = creds.split()
        return final_creds




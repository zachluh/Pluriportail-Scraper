import discord
from discord.ext import commands

class user(commands.Cog):
    """Pluriportail user profile"""

    def __init__(self, bot, discord_user):
        self.bot = bot
        self.discord_user = discord_user

    async def create_new_profile(self, ctx, credmessage):

       message = await ctx.fetch_message(credmessage.id)

       with open(f"{str(self.discord_user.id)}.txt", "w") as f:
           f.write(str(self.credmessage.id))
           
    async def user_login_creation(self, ctx):
        with open(f"{str(self.discord_user.id)}.txt", "r") as f:
            creds = f.read()

        message = await ctx.fetch_message(creds)
        login_creds = message.content.split()

        return login_creds




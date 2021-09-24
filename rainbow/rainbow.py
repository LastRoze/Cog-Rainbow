import discord
import time
import asyncio
from redbot.core import checks, commands
from random import choice, randint

__author__ = "Last Roze"
class rainbow:
    """Make your role colorful!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(administrator=True)
    async def arainbow(self, ctx, interval:float, *, role):
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.guild.roles)
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
        if interval < 120:
            interval = 120
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.guild, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)

    @commands.command(administrator=True)
    async def rainbow(self, ctx, *, role: discord.Role):

        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.guild, role, colour=discord.Colour(value=colour))
            await asyncio.sleep(0.0)

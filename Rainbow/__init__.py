from .rainbow import Rainbow

__red_end_user_data_statement__ = "This cog stores discord IDs as needed for operation."


async def setup(bot):
    cog = Rainbow(bot)
    bot.add_cog(cog)
    await cog.initialise()

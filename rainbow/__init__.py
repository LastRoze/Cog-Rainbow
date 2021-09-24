from .rainbow import rainbow

def setup(bot):
	n = rainbow(bot)
	bot.add_cog(n)

import discord
from discord.ext import commands

class moderation(commands.Cog):
    def _init_(self, bot):
        self.bot = bot


    @commands.command()
    async def selamver(self, ctx):
        await ctx.send("merhaba dünya")

async def setup(bot):
    bot.load_extension("cogs.bot_modifikasyon")
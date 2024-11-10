import os
import discord
from discord.ext import commands
import webbrowser
import time
from datetime import datetime
import random

class moderation(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command()
    async def selamver(self, ctx):
        await ctx.send("merhaba dünya")

    @commands.command()
    async def youtube_ara(self, ctx, *, search):
        url = f"https://www.youtube.com/results?search_query={search}"
        webbrowser.get().open(url)
        await ctx.send(f"youtubede bunun için {search},sonuclar")

    @commands.command()
    async def google_ara(self, ctx, *, search):
        url = f"https://www.google.com.tr/search?q={search}"
        webbrowser.get().open(url)
        await ctx.send(f"googlede bunun için {search},bulduğum sonuclar")

    @commands.command()
    async def saat_kac(self, ctx):
        clock = datetime.now().strftime("%H:%M")
        await ctx.send(f"şu an saat>:){clock}")


    @commands.command()
    async def selamla(self, ctx, *, name):
        pass      #buraya ^ *, koyarsan ctx den sonrasını alır sonra herşeyi alır 
        await ctx.send(f"merhaba, {name}")

    @commands.command()
    async def say(self, ctx, massage):
        await ctx.message.delete()
        await ctx.send(massage)    

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        print(reason)
        await member.kick(reason= reason)
        await ctx.send(f"**{member.mention}**, **{reason}** sunucudan atıldı.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason):
        print(reason)
        await member.ban(reason= reason)
        await ctx.send(f"**{member.mention}**, **{reason}** sunucudan atıldı.")

    @commands.command()
    async def kontrol_mesaj_et(self, ctx, member: discord.Member):
        # Şu anki kanalın geçmişindeki mesajları alır
        async for message in ctx.channel.history(limit=100):  # Limit, son 100 mesajı kontrol eder
            if message.author == member:  # `member`, komutla verilen kullanıcıdır
                print(f"{message.author} kullanıcısının geçmiş mesajı: {message.content}")

        await ctx.send(f"{member.mention} kullanıcısının mesajları kontrol edildi.")

async def setup(bot):
    await bot.add_cog(moderation(bot))

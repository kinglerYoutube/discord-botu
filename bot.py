import os
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TKN = "MTMwMTYxOTU5MDA0ODI1MTkyNA.GnMlEl.XpST2lXhs7a9_WVGIjQswotY7Qlpaq_Cjc7boY"
#"MThwMTYxOTU5MDA0ODI1MTkyNP.hsSrV_.LBUrZew3Veg48sQXE-lIXBIbAtrvObWuZWyBig"

initial_extensions = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename [:-3])

async def load_extension():
    for ext in initial_extensions:
        await bot.load_extension(ext)

bot.load_extension("cogs.bot_modifikasyon")

@bot.event
async def on_ready():
    await bot.load_extension("cogs.bot_modifikasyon")
    print("uyandım")

@bot.event
async def on_message(message: discord.Message):
        print("şu kullanıcı", message.author, "şu mesajı", message.content, "gönderdi") 

@bot.event
async def on_member_join(member: discord.member):
    print(member.name)

@bot.event
async def on_member_remove(member: discord.member):
    print(member.name)

@bot.event
async def on_guild_channel_create(channel: discord.TextChannel):
    print("channel", channel.name, "oluşturuldu")

@bot.event
async def on_guild_channel_delete(channel: discord.TextChannel):
    print("channel", channel.name, "silindi")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason):
    print(reason)
    await member.kick(reason= reason)
    await ctx.send(f"**{member.mention}**, **{reason}** sunucudan atıldı.")

@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
    print(reason)
    await member.ban(reason= reason)
    await ctx.send(f"**{member.mention}**, **{reason}** sunucudan atıldı.")

bot.run(TKN)
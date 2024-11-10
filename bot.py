import os
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TKN = #"MThwMTYxOTU5MDA0ODI1MTkyNP.hsSrV_.LBUrZew3Veg48sQXE-lIXBIbAtrvObWipoı"

initial_extensions = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename [:-3])

async def load_extension():
    for ext in initial_extensions:
        await bot.load_extension(ext)

@bot.event
async def on_ready():
    await bot.load_extension("cogs.bot_modifikasyon")
    print("bot hazır")

@bot.event
async def on_message(message):
    if message.author.id == 948292425863036958:  # KULLANICI_ID ile kontrol etmek istediğiniz kullanıcının ID'sini yazın.
        print(f"{message.author} kullanıcısının mesajı: {message.content}")
    
    await bot.process_commands(message)  # Botun komutlarını işlemesini sağlar    

@bot.event
async def on_member_join(member: discord.member):
    print(f"şu kullanıcı, **{member.name}**, sunucuya giriş yaptı")
    await member.send(f"aramıza hoşgeldin, **{message.author}**")


@bot.event
async def on_member_remove(member: discord.member):
    print(f"şu kullanıcı, **{member.name}**, sunucudan ayrıldı")
    await member.send(f"görüşmek üzere kullanıcı, **{member.name}**")


@bot.event
async def on_guild_channel_create(channel: discord.TextChannel):
    print(f"**{channel.name}**,channel oluşturuldu")
    log_channel_id = 1304187472011460700  # Bildirimleri göndermek istediğiniz kanalın ID'si
    log_channel = bot.get_channel(log_channel_id)
    
    if log_channel:
        await log_channel.send(f"**{channel.name}**,channel  oluşturuldu")

@bot.event
async def on_guild_channel_delete(channel: discord.TextChannel):
    print(f"**{channel.name}**,channel silindi")
    log_channel_id = 1304187472011460700  # Bildirimleri göndermek istediğiniz kanalın ID'si
    log_channel = bot.get_channel(log_channel_id)
    
    if log_channel:
        await log_channel.send(f"**{channel.name}** kanalı silindi.")
    

bot.run(TKN)

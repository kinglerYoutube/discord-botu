import os
from discord.ext import commands
import discord
import time
from datetime import datetime
import random
from random import choice
import webbrowser

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
TKN = MThwMTYxOTU5MDA0ODI1MTkyNP.hsSrV_.LBUrZew3Veg48sQXE-lIXBIbAtrvObWuZWyBig
durum = None

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
    if message.channel.id == 1304187472011460700 or message.channel.id == 1305252550488096829:
        durum = None
        log_channel_id_1 = 1305252550488096829
        log_channel_1 = bot.get_channel(log_channel_id_1)

        if message.author.id == 948292425863036958:  # KULLANICI_ID ile kontrol etmek istediğiniz kullanıcının ID'sini yazın.
            print(f"{message.author} kullanıcısının mesajı: {message.content}")
        
        if message.author == bot.user:
            return

        if message.channel.id == log_channel_id_1:
            if "merhaba" in message.content.lower() or "selam" in message.content.lower():
                selection_1 = ["nasılsın", "yardımcı olmamı istermisin", "ne yapmamı istersin"]
                selected_response = random.choice(selection_1)
                await message.channel.send(selected_response)
                if selected_response == "nasılsın":
                    durum = "nasılsın_soruldu"
                if selected_response == "yardımcı olmamı istermisin":
                        durum = "yardım_teklifi_soruldu"

            elif durum == "nasılsın_soruldu":
                # Kullanıcı iyiyim veya kötüyüm dediğinde cevap ver
                if "iyiyim" in message.content.lower():
                    await message.channel.send("Mükemmel, sana nasıl yardım edebilirim?")
                    durum = None  # Durumu sıfırla
                elif "kötüyüm" in message.content.lower():
                    await message.channel.send("Olsun, sana yardım edebilirim.")
                    durum = None  # Durumu sıfırla
            
            elif durum == "yardım_teklifi_soruldu":
                # Kullanıcı iyiyim veya kötüyüm dediğinde cevap ver
                if "evet" in message.content.lower():
                    await message.channel.send("Mükemmel,sadece 'yardım et' yaz")
                    durum = None  # Durumu sıfırla
                elif "hayır" in message.content.lower():
                    await message.channel.send("tamam.")
                    durum = None  # Durumu sıfırla

            elif "yardım et" in message.content.lower():
                await message.channel.send("Tabiki komutlar şunlardır")
                time.sleep(0.5)
                await message.channel.send("İlk komut (!selamver),komut selam veriyor yani (!selamver),yazarsan 'merhaba dünya'der.")
                time.sleep(0.5)
                await message.channel.send("İkinci komut (!selamla + isim),komut isme selam veriyor yani (!selamla kinglerYT),yazarsan 'selam kinglerYT'der.")
                time.sleep(0.5)
                await message.channel.send("Üçüncü komut (!say + çümle),komut botun senin yazdığın çümleyi yazmasını sağlar yani(!say kinglerYT),yazarsan 'kinglerYT'der.")
                time.sleep(0.5)
                await message.channel.send("Dördünçü komut (!saat_kac),komut adı üstünde saatin kaç olduğunu yazıyor yani (!saat_kac),yazarsan 'saat:dakika'der.")
                time.sleep(0.5)
                await message.channel.send("Beşinci komut (!google_ara + aramak istediğin şey),komut google'yi açıp aramak istediğin şeyi arar yani (!google_ara kinglerYT),yazarsan 'kinglerYT'yi google'de arar.")
                time.sleep(0.5)
                await message.channel.send("Altıncı komut (!youtube_ara + aramak istediğin şey),komut youtube'yi açıp aramak istediğin şeyi arar yani (!youtube_ara kinglerYT),yazarsan 'kinglerYT'yi youtube'de arar.")

            elif "teşekkür ederim" in message.content.lower() or "teşekkürler" in message.content.lower():
                selection_3 = ["rica ederim", "ne demek", "her zaman buradayım"]
                selected_response = random.choice(selection_3)
                await message.channel.send(selected_response)    

            elif "hangi gündeyiz" in message.content.lower() or "bugün günlerden ne" in message.content.lower():
                selection_5 = ["hemen bakıyorum:", "bugün günlerden:", "bugün:"]
                selected_response = random.choice(selection_5)
                today = time.strftime("%A").capitalize()
                days = {
                    "Monday": "pazartesi", "Tuesday": "salı", "Wednesday": "çarşamba",
                    "Thursday": "perşembe", "Friday": "cuma", "Saturday": "cumartesi", "Sunday": "pazar"
                }
                today = days.get(today, today)
                await message.channel.send(selected_response + today)

            elif "saat kaç" in message.content.lower():
                selection = ["saat şu an:", "hemen bakıyorum:"]
                selected_response = random.choice(selection)
                clock = datetime.now().strftime("%H:%M")
                await message.channel.send(selected_response + clock)

            elif "özel birşey aç" in message.content.lower():
                await message.channel.send("tamam'dır bende o iş ")
                time.sleep(1)
                webbrowser.get().open("https://www.youtube.com/watch?v=Y75Km7dlt94")
                webbrowser.get().open("https://www.arthipo.com/image/cache/catalog/poster/mustafa-kemal-ataturk/mka153-mustafa-kemal-ataturk-bayrakla-gokyuzune-bakarken-bayrakli-portre-42-844x1200.webp")
                time.sleep(1)
                await message.channel.send("geçmiş on kasım kutlu olsun")

            elif "geri dönüşüm" in message.content.lower() and "araç" in message.content.lower():
                selection_6 = ["", "", ""]
                selected_response = random.choice(selection_6)
                url_1 = ["https://www.youtube.com/shorts/iduGnb4J2-0", "https://www.youtube.com/shorts/q2CIlk013oU"]
                url_1_response = random.choice(url_1)
                await message.channel.send(f"{selected_response}\n{url_1_response}")


            elif "geri dönüşüm" in message.content.lower() and "saksı" in message.content.lower():
                selection_7 = ["", "", ""]
                selected_response = random.choice(selection_7)
                url_2 = ["https://www.youtube.com/shorts/5I5zIoEZQ18"]
                url_2_response = random.choice(url_2)
                await message.channel.send(f"{selected_response}\n{url_1_response}")

            elif "geri dönüşüm" in message.content.lower() and "silah" in message.content.lower():
                selection_8 = ["", "", ""]
                selected_response = random.choice(selection_8)
                url_3 = ["https://www.youtube.com/watch?v=A4V-_GgPulY&ab_channel=OrigamiK%C3%BClt%C3%BCr"]
                url_3_response = random.choice(url_2)
                await message.channel.send(f"{selected_response}\n{url_1_response}")

    await bot.process_commands(message)

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

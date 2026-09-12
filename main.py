import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
text_status = discord.Activity(type=discord.ActivityType.watching, name="watching for references")

bot = commands.Bot(command_prefix="n!", intents=intents, activity=text_status)
references = ["null", "scape", "mart", "baby", "celest", "flame", "bell", "symphony", "husk", "insurmountable", "abyss", "decay", "spring", "missile", "icbm", "flesh", "operator", "guardian", "tele", "greed", "purg", "nothing", "colon", "cadence", "sigil", "scrap", "random", "???", "ponder", "nil", "catalyst", "curse", "enemy", "upgrade", "greater", "dive", "charge", "spirit", "grapple", "glide", "wanted", "prisoner", "altar", "matrix", "swiftness", "paycheck", "medal", "esp", "belt", "wing", "trip", "shark", "tail", "gift", "blossom", "bloom", "fall", "boom", "panic", "shield", "shoe", "drown", "business", "run", "tile", "collapse", "gold", "mine", "chaos", "beacon", "patch", "chance", "protect", "pure", "razor", "sub", "space", "i guess bro", "ig bro", "votekick", "its time", "it's time", "operate", "bitter", "cease", "silence", "bound", "echo", "adrenaline", "pass", "mirage", "oblivion", "jackpot", "fragile", "trauma", "lap", "camo", "stairs", "void"]

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Loaded {len(references)} references.")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    if message.author.bot:
        return

    content = message.content.lower()
    detected_references = []
    reference_counter = 0

    for keyword in references:
        if keyword in content:
            reference_counter += 1
            detected_references.append(keyword)


    if reference_counter > 0:
        template = f"HOLY NULLSCAPE REFERENCE\n-# reference count: {reference_counter}\n-# references: "

        for i in range(reference_counter):
            if i >= reference_counter - 1:
                template = template + detected_references[i] + "."
            else:
                template = template + detected_references[i] + ", "

        response = await message.reply(template, mention_author=True)

# Replace "BOT_TOKEN_HERE" with your actual bot token
bot.run("BOT_TOKEN_HERE")
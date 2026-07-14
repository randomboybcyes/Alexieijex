import discord
import random
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")

    if not automatic_spawn.is_running():
        automatic_spawn.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def info(ctx):
    await ctx.send(
        "i am Alexieijex!\n"
        "i love pizza and countryballs!\n"
        "im cooler than you \n"
    )

SPAWN_CHANNEL_ID = 1526204933240520808

balls = {
    "Gabon": {
        "image": "images/gabon.png",
        "chance": 80
    },

    "Republic of Congo": {
        "image": "images/congo.png",
        "chance": 80
    },

    "Poland": {
        "image": "images/poland.png",
        "chance": 60
    },

    "France": {
        "image": "images/france.png",
        "chance": 50
    },

    "Spain": {
        "image": "images/spain.png",
        "chance": 50
    },

    "England": {
        "image": "images/England.png",
        "chance": 30
    },

    "Argentina": {
        "image": "images/argentina.png",
        "chance": 40
    },

    "Liechtenstein": {
        "image": "images/liechtenstein.png",
        "chance": 70
    },

    "Romanovyes German Empire": {
        "image": "images/Romanovyes_German_Empire.png",
        "chance": 5
    },

    "Tajikistan": {
        "image": "images/taijikistan.png",
        "chance": 80
    },
    

    "Greenland": {
        "image": "images/greenland.png",
        "chance": 60
    },

    "Belize": {
        "image": "images/belize.png",
        "chance": 70
    },

     "Pakistan": {
        "image": "images/pakistan.png",
        "chance": 67
    },

    "Namibia": {
        "image": "images/namibia.png",
        "chance": 80
    }
}

current_spawn = None
current_ball = None 

@bot.command()
async def catch(ctx, *, guess):
    global current_spawn

    if current_spawn is None:
        await ctx.send("❌ There is no Countryball available!")
        return

    if guess.lower() == current_spawn.lower():
        await ctx.send(
            f"🎉 Congratulations {ctx.author.mention}!\n"
            f"You caught {current_spawn}!"
        )
        current_spawn = None

    else:
        await ctx.send("❌ Wrong guess!")

@tasks.loop(minutes=5)
async def automatic_spawn():
    global current_spawn

    channel = bot.get_channel(SPAWN_CHANNEL_ID)

    if channel is None:
        return

    ball = random.choices(
        list(balls.keys()),
        weights=[balls[x]["chance"] for x in balls],
        k=1
    )[0]

    print(f"Spawned: {ball}")

    current_spawn = ball

    await channel.send(
        f"🌍 A wild **{ball}** appeared!\nUse `!catch <country>` to catch it!"
    )

bot.run(TOKEN)
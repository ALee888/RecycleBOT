# bot.py
import os
import random
import discord
import shelve
import logging

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_BUILD')
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/', help_command=help_command)
logging.basicConfig(level=logging.INFO)

materials = {
    "Aluminum" : 0,
    "Refined_aluminum" : 0,
    "Plastic" : 0,
    "Refined_plastic" : 0,
    "Rubber" : 0,
    "Refined_rubber" : 0,
    "Steel" : 0,
    "Refined_steel" : 0,
    "Scrap" : 0,
    "Refined_scrap" : 0,
    "Electronics" : 0,
    "Refined_electronics" : 0,
    "Glass" : 0,
    "Refined_glass" : 0,
    "Copper" : 0,
    "Refined_copper" : 0
}

def get_total():
    str_total = "```\n"
    for material in materials:
        str_total += material + " - " + str(materials[material]) + "\n" 
    str_total += "\n```"
    return str_total

def get_material(material):
    str_total = "`\n"
    str_total += material + " - " + materials[material]
    
    str_total += "\n`"

def save():
    print("REACH SAVE")
    try:
        s = shelve.open("RecycleData", writeback=True)
    except Exception as e:
        print("unexpected error ", e)
    else:
        for material in materials:
            s[material.capitalize()] = materials[material.capitalize()]
        s.sync()
        s.close()

def load():
    s = shelve.open("RecycleData")
    for material in materials:
        materials[material.capitalize()] = s[material.capitalize()]
    s.close()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} !!!!!is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command(name='status', help='prints all recycle values | Usage: /status')
async def status(ctx):
    await ctx.send(get_total())

@bot.command(name='roll', help='Simulates rolling dice | Usage: /roll (# dice) (# sides)')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='add', help='Add amount(x) to material(y) | Usage: /add x y')
async def add(ctx, amount: int, materialName: str):
    logging.info(f"Adding {amount} to {materialName}")
    materials[materialName.capitalize()] += amount
    await ctx.send(get_total())

@bot.command(name='remove', help='Remove amount(x) from material(y) | Usage: /remove x y')
async def remove(ctx, amount: int, materialName: str):
    materials[materialName.capitalize()] -= amount
    await ctx.send(get_total())

@bot.command(name='reset', help='Resets material(x) to 0 | Usage: /reset x')
async def reset(ctx, materialName: str):
    materials[materialName.capitalize()] = 0
    await ctx.send(get_total())

@bot.command(name='wipe', help='Clear all material values | Usage: /wipe')
async def add(ctx):
    for material in materials:
        materials[material] = 0
    await ctx.send(get_total())

@bot.command(name='backup', help='Save a backup of the table | Usage: /backup')
async def backup(ctx):
    save()
    await ctx.send("Table Saved")

@bot.command(name='restore', help='Restore data from backup | Usage: /restore')
async def restore(ctx):
    load()
    await ctx.send(get_total())

bot.run(TOKEN)

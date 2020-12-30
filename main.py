import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext


f = open("token.0", "r")
token = f.read()
f.close()


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, auto_register=True)


@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])


bot.run(token)

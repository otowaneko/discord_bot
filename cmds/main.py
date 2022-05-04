from datetime import datetime
from typing_extensions import Self
from matplotlib.pyplot import cla
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    #embed嵌入訊息,直接從這裡做https://cog-creators.github.io/discord-embed-sandbox/ ,timestamp要自己加
    @commands.command()
    async def embed(self,ctx):
        embed=discord.Embed(title="About", description="About the bot", color=0x6ab5fb,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="123", icon_url="https://pbs.twimg.com/media/FPKHg2waQAA31tK?format=jpg&name=small")
        embed.set_thumbnail(url="https://pbs.twimg.com/media/FPKHg2waQAA31tK?format=jpg&name=small")
        embed.add_field(name="test", value="test", inline=False)
        embed.set_footer(text="test")
        await ctx.send(embed=embed)

#設定bot
def setup(bot):
    bot.add_cog(Main(bot))
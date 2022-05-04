import discord
from discord.ext import commands
import random
import json
from core.classes import Cog_Extension

with open("setting.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):
    #傳送本機圖片
    @commands.command()
    async def 圖片(self,ctx):
        random_pic=random.choice(jdata['pic'])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

    #傳送網路圖片(pixiv不能用)
    @commands.command()
    async def web(self,ctx):
        random_pic=random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))
from ast import keyword
import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open("setting.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    #關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword=['hi','你好','嗨','Hello']
        if msg.content==keyword and msg.author != self.bot.user:
            await msg.channel.send('Hi')

def setup(bot):
    bot.add_cog(Event(bot))
import discord
from discord.ext import commands
import json
import random
import os

#載入資料
with open("setting.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

#設定指令的觸發字
bot=commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('>> Bot is online <<')

#啟用cog裡的指令
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

#關閉cog裡的指令
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

#更新cog裡的指令
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

#導入cog
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}') #從0~第len-3個字元

#避免重複執行之類的
if __name__=="__main__":
    bot.run(jdata['TOKEN'])
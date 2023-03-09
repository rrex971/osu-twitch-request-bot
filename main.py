import os
from twitchio.ext import commands
import websockets
import asyncio
false = False
true = True
null = None

mods = "HDDTHRFLEZDTHDHRDTHRNM"
config = open("config.txt")
configlist = config.readlines()
configdict = {}
for i in configlist:
    configdict[i.split(":",maxsplit=1)[0].strip()] = i.split(":",maxsplit=1)[1].strip()
bot = commands.Bot(token=configdict["oauth"],
    client_id=configdict["client_id"],
    nick=configdict["bot_name"],
    prefix=configdict["prefix"],
    initial_channels=[configdict["channel"]])                                                                                                    

@bot.command(name = "r")
async def r(ctx, link = "n", mods1 = "n"):
    global configdict
    print("sent")
    if link == "n":
        await ctx.channel.send("where link modCheck") 
        return
    if mods1 == "n":
        mods1 = "NM"
    if link.startswith("https://osu.ppy.sh/beatmapsets/"):  
        if mods1.upper() in mods or mods1 == "NM":
            await ctx.channel.send("Map request sent Okayge 👍")
            os.system(f"""python osuirc.py --link {link} --mods {mods1.upper()} --username {"_".join(configdict["osu_username"].split())} --irctoken {configdict["irc_password"]} --apiid {configdict["api_id"]} --apisecret {configdict["api_secret"]}""")
        else:
            await ctx.channel.send("Deadge invalid mod combination try again")
    else:
        await ctx.channel.send("Stare only send osu map links")

@bot.command(name = "helprequest")
async def helprequest(ctx):
	await ctx.channel.send("Use the !r command to request maps, usage: !r <map link> [mods if any, leave blank for nm]")

@bot.command(name = "np")
async def np(ctx):
    async with websockets.connect("ws://localhost:24050/ws") as ws:
        data = eval(await ws.recv())["menu"]
        print(data["bm"]["id"])
        await ctx.send(f"""Now Playing: {data["bm"]["metadata"]["title"]} - {data["bm"]["metadata"]["artist"]} [{data["bm"]["metadata"]["difficulty"]}], ({data["bm"]["metadata"]["mapper"]} {data["bm"]["stats"]["SR"]}*) +{data["mods"]["str"]} | Link: https://osu.ppy.sh/b/{data["bm"]["id"]} """)

@bot.command(name = "current")
async def current(ctx):
    async with websockets.connect("ws://localhost:24050/ws") as ws:
        data = eval(await ws.recv())
        dg = data["gameplay"]
        await ctx.send(f"""Current: {dg["pp"]["current"]}pp / {dg["pp"]["fc"]}pp""")

@bot.command(name = "nppp")
async def nppp(ctx):
    async with websockets.connect("ws://localhost:24050/ws") as ws:
        data = eval(await ws.recv())
        dm = data["menu"]
        await ctx.send(f"""100% : {dm["pp"]["100"]}pp | 99% : {dm["pp"]["99"]}pp | 98% : {dm["pp"]["98"]}pp | 97% : {dm["pp"]["97"]}pp | 96% : {dm["pp"]["96"]}pp | 95% : {dm["pp"]["95"]}pp""")

if __name__=="__main__":
    bot.run()





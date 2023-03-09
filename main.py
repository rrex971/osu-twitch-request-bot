import os
from twitchio.ext import commands
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



if __name__=="__main__":
    bot.run()





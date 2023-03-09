import argparse
import osu_irc
import asyncio
import urllib.request
from bs4 import BeautifulSoup
from ossapi import Ossapi


parser = argparse.ArgumentParser(description='osu! IRC connection.')
parser.add_argument("--link")
parser.add_argument("--mods")
parser.add_argument("--username")
parser.add_argument("--irctoken")
parser.add_argument("--apiid")
parser.add_argument("--apisecret")
args = parser.parse_args()
osuapi = Ossapi(int(args.apiid),args.apisecret)
osuirc = osu_irc.Client(token = args.irctoken, nickname = args.username.lower())

async def send(link, mods):
    await asyncio.sleep(1)
    map = BeautifulSoup(urllib.request.urlopen(link), features = "html.parser")
    maptitle = map.title.string.split("·")[0]
    mapinfodiff = osuapi.beatmap_attributes(link.split("/")[-1])
    mapinfo = osuapi.beatmap(link.split("/")[-1])
    await osuirc.sendPM(Us=args.username.lower(), content=f"Request map: [{link} {maptitle}[{mapinfo.version}] ] Mapper: {mapinfo.beatmapset().creator}  Stars: {round(mapinfodiff.attributes.star_rating, 2)} Mods: +{mods}")
    print(f"Request map: {link} Mods: +{mods}")
    osuirc.stop()

osuirc.Loop.create_task(send(args.link, args.mods))
try:
    osuirc.run()
except AttributeError:
    pass

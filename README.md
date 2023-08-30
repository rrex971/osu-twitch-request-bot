# osu! request bot for Twitch streamers
bad osu! beatmap request bot

## Prerequisites
Python 3.8+ (preferably latest)

requirements in `requirements.txt`
open folder in terminal and run:
```bash
pip install -r requirements.txt
```

## How to use
### Get your tokens
1. For your Twitch tokens, go [here](https://twitchapps.com/tmi/) to get your oauth key, and [here](https://dev.twitch.tv/console/apps/create) to get your bot application registered and to get your client id. Enter anything in application name and oauth redirect URLs. 
2. Next up, osu! api tokens: go [here](https://osu.ppy.sh/home/account/edit), scroll to the very bottom and hit new oauth application. Again, you can enter anything as application name and leave application url blank. Grab your api client ID and client secret
3. Finally, the osu! irc tokens: go [here](https://osu.ppy.sh/p/irc) and get your irc password.

Put all the above tokens in the config file along with your osu! username, bot username (your twitch username/bot's twitch username), bot prefix and channel name.

### Running the bot
Once you've verified that the config file is fine, run the `main.py` file and the bot should begin functioning.




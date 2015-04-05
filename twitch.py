import willie.module
#import requests
#import json

@willie.module.commands('streams')
def streams(bot, trigger):
'''
	game = "The+King+Of+Fighters+XIII"
	twitch = requests.get("https://api.twitch.tv/kraken/streams/?game="+ game)
	json_data = json.loads(twitch.text)

	s = json_data.get('streams')

	for i in s:
	        chan = i['channel']
        	bot.reply((chan['display_name'] +" - "+  chan['url'] +" - Viewers: "+ str(i['viewers'])))
'''
	bot.say("These are all the streams up right now!"


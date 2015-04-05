import willie.module
import requests
import json

@willie.module.commands('streams')
def helloworld(bot, trigger):
	game = "The+King+Of+Fighters+XIII"
	request = requests.get("https://api.twitch.tv/kraken/streams/?game="+ game)
	json_data = json.loads(request.text)
	
	streams = json_data.get('streams')
	
	for stream in streams:
		chan = stream['channel']
		
		bot.say(chan['display_name'] +" - "+  chan['url'] +" - Viewers: "+ str(stream['viewers']))

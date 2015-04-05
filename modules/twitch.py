import willie.module
import requests
import json
 
KOF = ["KOF","KOF13","KOFXIII"]
kofgame = "The%20King%20Of%20Fighters%20XIII"
GG = ["GG","XRD"]
gggame = "Guilty%20Gear%20Xrd%20-SIGN-"
SF = ["SF","USF","USF4","SF4"]
sfgame = "Ultra%20Street%20Fighter%20IV"
MARVEL = ["MARVEL","LEVRAM","MVC","UMVC","MVC3","UMVC3"]
marvelgame = "Ultimate%20Marvel%20vs.%20Capcom%203"
SG = ["SKULLGIRLS","SG"]
sggame = "Skullgirls"
BB = ["BB","BBCP"]
bbgame = "BlazBlue%3A%20Chrono%20Phantasma"
 
dic=[(KOF,kofgame),(GG,gggame),(SF,sfgame),(MARVEL,marvelgame),(SG,sggame),(BB,bbgame)]
 
@willie.module.commands('streams')
def helloworld(bot, trigger):
 
        game = "";
        for games in dic:
                (short, longname) = games
                if trigger.group(2).upper() in short:
                        game = longname
        if game == "":
                bot.say("I really can't understand you. Are you sure this game is VR-Fist approved?")
                return
        request = requests.get("https://api.twitch.tv/kraken/streams/?game="+ game)
        json_data = json.loads(request.text)
       
        streams = json_data.get('streams')
       
        for stream in streams:
                chan = stream['channel']
               
                bot.say(chan['display_name'] +" - "+  chan['url'] +" - Viewers: "+ str(stream['viewers']))

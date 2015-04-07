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
VF = ["VF","VF5","VF5FS"]
vfgame = "Virtua%20Fighter%205%20Final%20Showdown"
MK9 = ["MK","MK9"]
mk9game = "Mortal%20Kombat"
MKX = ["MKX"]
mkxgame = "Mortal%20Kombat%20X"
SFXT = ["CROSS TEKKEN","SFXT"]
sfxtgame = "Street%20Fighter%20X%20Tekken"

dic=[(KOF,kofgame),(GG,gggame),(SF,sfgame),(MARVEL,marvelgame),(SG,sggame),(BB,bbgame),(VF,vfgame),(MK9,mk9game),(MKX,mkxgame),(SFXT,sfxtgame)]
 
@willie.module.commands('streams')
def twitch(bot, trigger):

        if not trigger.group(2) or trigger.group(2).upper() == "LIST":
                help = "Approved games by VR-Fyct: "
                for games in dic:
                        (shorts, longname) = games
                        help+=longname.replace("%20"," ").replace("%3",":")+" as: "+shorts[0]
                        for short in shorts[1:]:
                                help+=", "+short
                        if len(help) >= 300:
                                bot.say(help)
                                help = ""
                        else:
                                help+=" || "
                bot.say(help)
                return
 
        game = "";
        for games in dic:
                (short, longname) = games
                if trigger.group(2).upper() in short:
                        game = longname
        if game == "":
                bot.say("I really can't understand you. Are you sure this game is VR-Fyct approved?")
		return

        request = requests.get("https://api.twitch.tv/kraken/streams/?game="+ game)
        json_data = json.loads(request.text)
       
        streams = json_data.get('streams')
       
        if not streams:
                bot.say("No streams for "+game.replace("%20"," ").replace("%3",":"))
                return
 
        for stream in streams[:5]:
                chan = stream['channel']
               
                bot.say(chan['display_name'] +" - "+  chan['url'] +" - Viewers: "+ str(stream['viewers']))

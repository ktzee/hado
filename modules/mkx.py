"""
countdown.py - Willie Countdown Module
Copyright 2011, Michael Yanovich, yanovich.net
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net
"""
from willie.module import commands, NOLIMIT
import datetime


@commands('hype')
def mkx_countdown(bot, trigger):
    """
    .countdown <year> <month> <day> - displays a countdown to a given date.
    """
#    text = trigger.group(2)
#    if not text:
#        bot.say("Please use correct format: .countdown 2012 12 21")
#        return NOLIMIT
#    text = trigger.group(2).split()
#    if text and (text[0].isdigit() and text[1].isdigit() and text[2].isdigit()
#            and len(text) == 3):
    diff = (datetime.datetime(2015, 04, 14)) - datetime.datetime.today()
    bot.say(str(diff.days) + " days, " + str(diff.seconds / 60 / 60) + " hours and " + str(diff.seconds / 60 - diff.seconds / 60 / 60 * 60) + " minutes until MKX")
#else:
#    bot.say("Please use correct format: .countdown 2012 12 21")
#   return NOLIMIT

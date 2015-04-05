import willie.module

@willie.module.commands('helloworld')
def helloworld(bot, trigger):
	bot.say('Hello, world')

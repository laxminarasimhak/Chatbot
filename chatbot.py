import random
hello = ["hi","is anyone there?", "hello", "good day","hello there"]
bye = ["cya", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
how_are = ["how are you","whats up","how you doing"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["i want to buy something", "what is on the menu", "what do you reccommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation","time","work time","time period"]
print("*******************************************************\n")
while True:
	a = input('User said -')
	if a.lower() in hello:
		botans = ["Hello !","hi","hi there","welcome"]
		print('Bot said - '+random.choice(botans)+'\n')
	elif a.lower() in bye:
		botans = ["sad to see you go :(","bye","miss you"]
		print('Bot said - '+random.choice(botans)+'\n')
	elif a.lower() in how_are:
		botans = ["I am fine ,thanks ","Happy","I am good"]
		print('Bot said -'+ random.choice(botans)+'\n')
	elif a.lower() in name:
		botans = ["My name is TVC bot","You can call me TVC bot","TVC Bot in your service","My friends call me TVC Bot"]
		print('Bot said -'+ random.choice(botans)+'\n')
	elif a.lower() in bye:
		botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		print('Bot said - '+random.choice(botans)+'\n')
	elif a.lower() in menu:
		botans = ["We sell fruits!", "Fruitss are on the menu!","Please take a look at Fruits"]
		print('Bot said - '+random.choice(botans)+'\n')
	elif a.lower() in hours:
		botans = ["We are open 24/7"]
		print('Bot said - '+random.choice(botans)+'\n')
	else:
		print('Bot said - Sorry What ?''\n')
		

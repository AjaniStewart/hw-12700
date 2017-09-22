import random

def madlibs(string):
	nouns = ["pony","goal in life","scourge upon the earth", "computer scientist", "sneaky criminal"]
	verbs = ["run", "program", "annoy", "medicate", "challenge"]
	adjs = ["pretty", "internet worthy", "brilliant", "self-centered", "insane"]
	return string \
	.replace('NOUN', nouns[random.randint(0,len(nouns) - 1)]) \
	.replace('VERB', verbs[random.randint(0,len(verbs) - 1)]) \
	.replace('ADJECTIVE', adjs[random.randint(0,len(adjs) - 1)])
	

string = "A NOUN is ADJECTIVE and it VERBs"

print(madlibs(string))

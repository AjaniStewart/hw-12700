
def piglatin(string):
	vowels = ['a','e','i','o','u']
	if string.lower()[0] in vowels:
		return string + "ay"
	else:
		return string[1:]+string[0]+"ay"

print(piglatin("latin"))
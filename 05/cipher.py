import sys

def encode_letter(c,r):
	return chr((((ord(c)-ord('a'))+r)%26)+ord('a'))


def encode_string(s,r):
	nS = ""
	for i in s:
		if i.isalpha():
			nS += encode_letter(i,r)
		else:
			nS += i
	return nS

def full_encode(s,n=27):
	nS = ""

	for i in range(1,n):
		nS += encode_string(s,i) + '\n'
	return nS

if len(sys.argv) == 1:
	print("Usage: python", sys.argv[0], " <string to flipped>" )
	print('Program will print all possible flips of entered string')
	print('Example: ')
	print(full_encode('abcd',5))
	print('...')
else:
	print(full_encode(sys.argv[1]))

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

def full_encode(s):
	nS = ""

	for i in range(1,27):
		nS += encode_string(s,i) + '\n'
	return nS
print(full_encode('mike zamansky'))

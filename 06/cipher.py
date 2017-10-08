import sys
import math

#real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

#file = open('Sherlock.txt')
#real_stats = build_frequency_vector(file.read())



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

def full_encode(s,n=26):
	nS = ""

	for i in range(n):
		nS += encode_string(s,i) + '\n'
	return nS

def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
    	print(s[i]," : ",v[i])

def distance(l1,l2):
	"""
    Euclidean distance between l1 and l2. If the lists are of 
    different lengths, go to the lenght of the shorter one
    """
	length = len(l1)
	if len(l2) < length:
		length = len(l2)

	sum = 0
	for i in range(length):
		sum += (l1[i]-l2[i])**2
	d = math.sqrt(sum)
	return d

def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
    	v.append(s.count(letter) / num_letters)
    return v

def decode(s):
	encodeList = full_encode(s).splitlines()
	freqVector = []
	for i in encodeList:
		freqVector.append(build_frequency_vector(i))

	smallestIndex = 0
	for i in range(len(freqVector)):
		if distance(freqVector[i], real_stats) < distance(freqVector[smallestIndex],real_stats):
			smallestIndex = i
	return (encode_string(s,smallestIndex))

"""
def main():
	if len(sys.argv) == 1:
		print("Usage: python", sys.argv[0], " <string to flipped>" )
		print('Program will print all possible flips of entered string')
		print('Example: ')
		print(full_encode('abcd',5))
		print('...')
	else:
		print(full_encode(sys.argv[1]))


if __name__ == '__main__':
	main()
"""
file = open('Sherlock.txt')
real_stats = build_frequency_vector(file.read().lower())
print(decode(encode_string("one hundred million",17)))

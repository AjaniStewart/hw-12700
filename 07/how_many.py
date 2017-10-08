def freq(n,l):
	count = 0
	for i in l:
		if i == n:
			count += 1
	return count

def min(l):
	m = l[0]
	for i in l:
		if i < m:
			m = i
	return m

def mode(l):
	fList = []
	for i in l:
		fList.append(freq(i,l))

	mIndex = 0
	for i in range(len(fList)):
		if fList[i] > fList[mIndex]:
			mIndex = i
	return l[mIndex]

tList = [3,2,2,1,3,4,5,4,3,4,3]
print(mode(tList))
print(min(tList))
print(freq(3,tList))
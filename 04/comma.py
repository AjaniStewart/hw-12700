import copy

def comma(list):
	string = ''
	cList = copy.copy(list)
	cList.insert(len(list)-1,'and')
	for i in cList:
		string += i
		if not (i == 'and' or i == cList[-1]):
			string += ', '
		else:
			string += ' '
	return string

print(comma(['apples','bananas','tofu','cats','death']))
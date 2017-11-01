#!/bin/python3

import sys

def ladyBug(s):
    """
    it cannot be solved if:
    there is only one occurence of a letter
    if there are no spaces in the board and they arnt already happy
    """
    l = [] #l has all the unique letters in the string
    for i in s:
        if i not in l:
            l.append(i)
            
    for i in l:
        if s.count(i) == 1 and i != '_' : #if there is only one occurence of a letter
            return 'NO'
        
        #if there are no spaces, and they arnt already happy
        #if the next and previous element are different, then it isnt happy
    if '_' not in l:
        for i in range(1,len(s)-1):
            if s[i] != s[i+1] and s[i] != s[i-1]:
                return 'NO'
    return 'YES' #all other cases it can be solved
        
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    print(ladyBug(b))


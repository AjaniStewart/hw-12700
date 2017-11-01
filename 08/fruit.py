#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleCount = 0
for i in apple:
    if i+a <= t and i+a >= s:
        appleCount += 1
print(appleCount)
 
orangeCount = 0    
for i in orange:
    if b+i <= t and b+i >= s:
        orangeCount += 1
print(orangeCount)


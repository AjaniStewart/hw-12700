#Number 1
def divide(A,B,u):
  return int(1/(A/B)) * u
  
#Number 2
def encode(s):
  l = []
  count = 1
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      count += 1
    else:
      if count != 1:
        l.append(count)
      l.append(s[i])
      count = 1
  else:
    if count != 1:
      l.append(count)
    l.append(s[i])
    
  return l
  
#Number 3
d = { ('a','e','i','o','l','n','r','s','t') : 1, 
      ('d','g') : 2,
      ('b','c','m','p') : 3,
      ('f','h','v','w','y') : 4,
      ('k') : 5,
      ('j','x') : 8,
      ('q','z') : 10
    }
    
def score(w):
  w = w.lower()
  sum = 0
  for i in w:
    for j,k in d.items():
      if i in j:
        sum += k
  return sum

print(divide(1,2,4))
print(encode('aaaaa'))
print(score('hello'))

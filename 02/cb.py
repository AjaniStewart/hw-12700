def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

 def string_bits(str):
  nStr = ""
  for i in range(len(str)):
    if i % 2 == 0:
      nStr += str[i]
  return nStr
  
def lone_sum(a, b, c):
  list = [0]
  if a == b and b == c:
    return 0
  for i in [a,b,c]:
    if i not in list:
      list.append(i)
    else:
      list.remove(i)
    sub = 0
    for i in list:
      sub += i
    
  return sub  


def string_splosion(str):
  strS = ""
  for i in range(len(str)):
    strS += str[:i+ 1]
  return strS

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  return cigars >= 40 and cigars <= 60

def caught_speeding(speed, is_birthday):
  lowerLimit = 61
  upperLimit = 80
  if is_birthday:
    lowerLimit += 5
    upperLimit += 5
    
  if speed < lowerLimit:
    return 0
  elif speed >= lowerLimit and speed <= upperLimit:
    return 1
  else:
    return 2

string = "MikeZamansky"
print(string_times(string,3))
print(front_times(string,3))
print(string_bits(string))
print(lone_sum(3,2,3))
print(string_splosion(string))
print(cigar_party(100,True))
print(caught_speeding(75,False))




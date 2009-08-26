r = open("out.txt",'r')
w = open("super.txt",'w')

def special(word):
  for char in word:
    ascii = ord(char)
    if ascii < 97 or ascii > 122:
      return True
  return False

processed = 0

for line in r:
  words = line.split(" ")
  for word in words:
    if not special(word):
      w.write(word + "\n")
  processed += 1
  if processed == 1337:
    processed = 0
    print "now at ",r.tell()
      

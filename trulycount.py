print "Opening Index"
f = open('sortedsuper.txt', 'r')

w = open('sortedcounted.txt', 'w')

print "Indexing Index"
pointer = ""
count = 0
index = {}

while True:
  line = f.readline()
  if line == "":
    break
  if line != pointer:
    w.write(str(count) + ";" + pointer)
    count = 0
    pointer = line
  count += 1
f.close()


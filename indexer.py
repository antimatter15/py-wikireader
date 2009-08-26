print "Opening Semi-Index"
f = open('semidex.txt', 'r')
print "Reading Semi-Index"
lines = f.readlines()
print "Sorting Contents"
lines.sort(lambda x, y: cmp(x,y))
print "Opening Save Index"
w = open('index.txt', 'w')
print "Saving Index"
w.writelines(lines)
w.close()
print "Done creating Index"

print "Opening Index"
f = open('index.txt', 'r')

depth = 2

print "Indexing Index"
pointer = ""
start = 0
index = {}

while True:
  line = f.readline()
  if line == "":
    break
  if line[0:depth] != pointer:
    index[pointer] = (start, f.tell()-start)
    start = f.tell()
    pointer = line[0:depth]
f.close()

print "Dumping (Saving)"

import pickle
w = open("indexindex.pickle","w")
pickle.dump(index, w)

print "Done"

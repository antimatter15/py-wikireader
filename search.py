import sys,bz2
query = sys.argv[1]

print "Query: ",query

print "Loading Indexed Index"
idx = open('indexindex.pickle', 'r')
import pickle
index = pickle.load(idx)
idx.close()

depth = 2 #sync with index config!

print "Searching Sub-Index"
try:
  subidx = index[query[0:depth]]
  print "Location in Index:",subidx
except KeyError:
  print "Sub Index not found!"
  exit()
  
print "Loading Main Index"
f = open('index.txt', 'r')

print "Finding Index Section"
f.seek(subidx[0])
end = subidx[0] + subidx[1]

artdx = 0
artde = 0
while f.tell() < end:
  line = f.readline()
  parts = line.split(';')
  if parts[0] == query:
    print line
    artdx = int(parts[1])
    artde = int(parts[2])
    break
else:
  print "Index not found!"
  exit()
  
f.close()

print "Opening Document"
wiki = "out.txt.bz2"
if wiki.endswith(".xml"):
  f = open(wiki, 'r')
elif wiki.endswith(".bz2"):
  f = bz2.BZ2File(wiki, 'r')

f.seek(artdx)
print f.read(artde)


import hashlib

def f1(seq):
    set = {}
    map(set.__setitem__, seq, [])
    return set.keys()

def test(l):
  narr = []
  for g in l:
    m = hashlib.sha1()
    m.update(g)
    narr.append(m.hexdigest()[0])
    print g, # "->", m.hexdigest()[0]
  print "|",len(f1(l))
  return narr

last = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f".split(",")
for x in range(0,100):
  last = test(last)

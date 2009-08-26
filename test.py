import xml.parsers.expat
import bz2

wiki = "simplewiki-20090716-pages-articles.xml.bz2"

page = ""
title = ""
action = 0
ignored = 0
total = 0


#w = open('out.txt', 'w')
w = bz2.BZ2File("out.txt.bz2","w")

d = open('semidex.txt', 'w')

# 3 handler functions
def start_element(name, attrs):
  global action
  if name == "title":
    action = 1
  elif name == "text":
    action = 2
  #print 'Start element:', name, attrs
  
def end_element(name):
  global action, page, title, ignored
  if name == "page":
    global total
    total += 1
    if page != "" and title != "":
      global w, d
      w.write(page.encode('utf-8'))
      pln = len(page.encode('utf-8'))
      d.write(title.encode('utf-8') + ";" + str(w.tell()-pln) + ";" + str(pln) + "\n") #todo: escape ; occurances
      page = ""
      title = ""
      if total % 7 == 0:
        print "Ignored: ",ignored," out of Total: ",total, "(",(100*ignored/float(total)),")%"
    else:
      ignored += 1
  action = 0
  #print 'End Element:',name
    

def char_data(data):
  #print 'Character data:', repr(data)
  global action, page, title
  
  if action > 0:
    if data.startswith("[[Category:"):
      action = 0
    if action == 1:
      title += data
    elif action == 2:
      page += data


p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

if wiki.endswith(".xml"):
  f = open(wiki, 'r')
elif wiki.endswith(".bz2"):
  f = bz2.BZ2File(wiki, 'r')
  
for line in f:
  p.Parse(line)
p.Parse("",1)



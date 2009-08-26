import math

f = open("in.txt", "r")
text = f.read()
words = text.split(" ")
lastword = ""
upper_except = ["I"]
main_dict = "i,will,apply,other,that,they,many,were,pickcall,small,even,this,felt,could,imply,time,cite,each,would,past,such,have,into,which,take,after,point,lead".split(",")
sub_dict = []
plural_except = ["this","thus","is","has"]


def simple(word):
  fword = word.replace(".","").replace(",","").replace(")","").replace("(","")
  if fword.endswith("ied"):
    fword = fword[0:-3] + "y"
  if fword.endswith("ed"):
    fword = fword[0:-2]
  if fword.endswith("ies"):
    fword = fword[0:-3] + "y"
  if fword.endswith("'s"):
    fword = fword[0:-2]
  if fword.endswith("s") and fword.lower() not in plural_except:
    fword = fword[0:-1]
  return fword
  

fwords = map(simple, words)  

for fword in fwords:
  if fwords.count(fword) > 2:
    if fword not in main_dict and fword not in sub_dict:
      if len(fword) < 5:
        main_dict.append(fword)
      else:
        sub_dict.append(fword)
  
for fword in fwords:
  if fword == "":
    continue
  if lastword.endswith(".") == True:
    if len(fword) < 5:
      if fword not in main_dict and fword not in sub_dict:
        main_dict.append(fword)
  else: #in the middle of sentence
    if fword[0].upper() == fword[0]: #if it's capitalized
      if fword not in upper_except:
        if fword not in main_dict and fword not in sub_dict:
          #this is a special word, goes straight to the dictionary
          sub_dict.append(fword)
    elif fword.lower() == fword:
      if len(fword) < 5:
        if fword not in main_dict and fword not in sub_dict:
          main_dict.append(fword)
  lastword = fword#.lower()

lastword = ""
main_len = len(main_dict)
sub_len = len(sub_dict)
bpw = math.log(main_len + sub_len)/math.log(2)
out = []

for fword in fwords:  
  lastword = fword#.lower()
  if fword not in main_dict:
    if fword not in sub_dict:
      print "lookup",fword
    else:
      #print "sub",word,sub_dict.index(word)
      out.append(main_len + sub_dict.index(fword))
  else:
    #print "main",word,main_dict.index(word)
    out.append(main_dict.index(fword))

print "SUBDICT",sub_dict
print "MAINDICT",main_dict
print "OUT",out

for idx in out:
  if idx < main_len:
    print main_dict[idx],
  else:
    print sub_dict[idx-main_len],

avg_wrd = len("".join(fwords))/len(fwords)

print ""
print "Original Words:",len(words),"Compressed Words:",len(out),"Data Loss:",1.0-(len(out)/float(len(words)))
print "MAINDICT size",main_len,"SUBDICT size",sub_len,"bits per word",bpw
print "Average Word Size:",avg_wrd,"Bits per character:",avg_wrd/bpw
print "Original Size (bits):",len(text)*8,"Estimated Compressed Size (bits):",(bpw*len(out)), "Compression Ratio:",((bpw*len(out))/(len(text)*8))


f = open('sortedcounted.txt', 'r')
print "Reading Semi-Index"
lines = f.readlines()
print "Sorting Contents"
lines.sort(lambda x, y: cmp(int(y.split(";")[0]),int(x.split(";")[0])))
print "Opening Save Index"
w = open('sortedcountedsorted.txt', 'w')
print "Saving Index"
w.writelines(lines)
w.close()
print "Done creating Index"

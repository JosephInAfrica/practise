x=[]
for i in range(1,6):
	x.append(i)
	print i

print x
print len(x)
for i in range(5):
	for j in range(i,5):
		print "i:%s,j:%s "%(x[i],x[j])

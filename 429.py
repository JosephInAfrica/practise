import re
from re import match
from re import split
a=r'([A-Za-z0-9/_]+)@([A-Za-z0-9]+).([A-Aa-z]+)'
b='lochlee@qq.com'

def mat(a,b):
	c=match(a,b)
	if c is not None:
		print "match"
	else:
		print "no match"
	print c
m=match(a,b)

print m.groups()
for i in range(4):
	print m.group(i)

c=re.compile(a)
print c.match(b).groups()
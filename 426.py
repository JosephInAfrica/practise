import hashlib

a=hashlib.md5()
b=hashlib.sha1()
a.update('what is this')
b.update('what is that')

print a.hexdigest()
print b.hexdigest()

import itertools
c=itertools.count(1)
d=itertools.cycle('ABC')
d=itertools.repeat('ABC',10)
e=itertools.takewhile(lambda x:x<100,c)
print d

print e

for i in e:
	print i


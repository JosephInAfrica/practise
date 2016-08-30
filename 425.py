import hashlib

md5=hashlib.md5()
md5.update('how to use md5 inpython hashlib?')

sha1=hashlib.sha1()
sha1.update('how to use md5 inpython hashlib?')

md4=hashlib.md5()
md4.update('how to use')
md4.update(' md5 inpython hashlib?')

def calc_md5(password):
	return md5.update(password+'salt')
print calc_md5('how to use')
print md5.hexdigest()
print md4.hexdigest()
print sha1.hexdigest()

import itertools
natuals=itertools.count(10)
cs=itertools.cycle('ABC')
ten=itertools.repeat('abc',10)
natal10=itertools.count(1)
before10=itertools.takewhile(lambda x:x<10,natal10)

# for c in itertools.cycle(itertools.chain('ABC','XYZ')):
	# print c
for key,group in itertools.groupby('AAABBBCCCAAA'):
	print key,list(group)

r=itertools.imap(lambda x:x*x,[1,2,3])
# natuals=itertools.count(10)
for i in r:
	print i

m=itertools.imap(lambda x:x*x,itertools.count(1))


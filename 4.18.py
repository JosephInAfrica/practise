import json
d=dict(name='Joe',age=25,score=90)
print "d:%s"%d
e=json.dumps(d)
print e
f=json.loads(e)
print f

class student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
	def __repr__(self):
		return '>>object  %s'%self.name
	def __str__(self):
		return self.name
	def __getitem__(self,n):
		return 2*n
	def __getattr__(self,attr):
		return "this is to get attr %s"%attr
	def __call__(self,thing):
		return 'to call %s'%thing

lisa=student('lisa',26,90)

print lisa
print lisa[8]

def stu2dict(std):
	return{
	'name':std.name,
	'age':std.age,
	'score':std.score
	}
a=json.dumps(lisa,default=stu2dict)
b=json.loads(a)
print b

try:
	liz=json.dumps(lisa,default=stu2dict)
	print liz
except:
	pass

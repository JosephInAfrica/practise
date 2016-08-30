class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration();
        return self.a
    def __getattr__(self,attr):
        if attr=='score':
            return 99

class Chain(object):
    def __init__(self,path=''):
        self.__path=path
    def __getattr__(self,attr):
        return Chain("%s/%s"%(self.__path,attr))
    def __str__(self):
        return self.__path

def fn(self,name='world'):
    print ('Hello,%s'%name)

Hello=type('Hello',(object,),dict(hello=fn))

def test():
    h=Hello()
    h.hello()

# test()

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list):
    __metaclass__=ListMetaclass








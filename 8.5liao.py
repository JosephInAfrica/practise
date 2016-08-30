class Student(object):
    pass

bar=Student()

class fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __str__(self):
        return "a fib iterator"

    def __repr__(self):
        return 'repr fib iterator'

    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=0,1
            for i in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            end=n.stop
            step=n.step
            a,b=0,1
            result=[]
            for i in range(end):
                a,b=b,a+b
                if i>=start:
                    result.append(a)
            return result[::2]

    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a

def test():
    Fib =fib()
    print Fib
    print Fib[10]
    print Fib[5:10]
# test()
class chain(object):

    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return chain("%s/%s"%(self._path,path))

    def __str__(self):
        return self._path



class users(object):
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return self._name

    __repr__=__str__
    def __getattr__(self,name):
        return users("%s/%s"%(self._name,name))


def test1():
    print chain().Micheal.user
    print users('micheal')
    print chain().whatever.users('Micheal').user
    # print chain().users('micheal').user

test1()









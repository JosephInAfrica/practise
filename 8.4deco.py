class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=value

def test1():
    lee=Student()
    lee.score=78
    print lee.score

test1()


class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'this is a student object'
    __repr__=__str__

def test():
    print student('Joe')



class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def next(self):
        self.a,self.b=b,self.a+self.b
        if self.a>100:
            # raise StopIteration:
            pass
        return self.a
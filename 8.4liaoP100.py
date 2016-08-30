from types import MethodType
# class Student(object):
#     # def __init__(self,name,score):
#         # self.__name=name
#         # self.score=score

#     # def get_name(self):
#     #     return self.__name
#     # def print_name(self):
#     #     print self.__name
#     # def set_age(self,age):
#     #     self.age=age

#     @property
#     def score(self):
#         return self.score

#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('Score must be an integer')
#         if value<0 or value >100:
#             raise ValueError('Score must be between 0~100')
#         self.score=value


class student(object):
    @property
    def score(self):
        return self.grade
    @score.setter
    def score(self,score):
        self.grade=score

lee=student()
lee.score=90
print lee.score
# print lee.get_score()

def set_gener(self,gender):
    self.gender=gender
# set_gender=MethodType(set_gender,None,Student)
# lee.print_name()
def test1():
    print isinstance(lee,Student)
    print isinstance(lee,object)
    for i in dir(lee):
        try:
            print "%s:%s"%(i,lee[i])
        finally:
            print "alright"


def test2():
    a='ABC'
    # print dir(a)
    print "hasattr(a,'__doc__'):>>>"+str(hasattr(a,'__doc__'))
    print getattr(a,'__doc_','i dont have this attr')
    # print a.__doc__
    setattr(a,'__doc__','want to fuck the world upside down')

# test2()

def test3():
    pass

class Const(type):
    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            print('Atribute cant be changed')
        else:
            super(Const, self).__setattr__(key, value)

class A(metaclass=Const):
    x=1




A.y=1
print(A.__dict__)

A.x = 2



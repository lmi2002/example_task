from .Task2 import *


class A(metaclass=Const):
    x = 1

class TestClass:
    def test_set_new_attr(self):
        A.y = 2
        assert A.y == 2

    def test_change_attr(self):
        try:
            A.x = 1
        except Exception as e:
            assert isinstance(e, ConstAttributeError)



#
# A.y=1
# a = A()
#
# a.x=1
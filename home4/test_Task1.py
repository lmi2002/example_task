from Task1 import *

class TestClass(object):
    """
    Testing class for homework1. To run all tests with pytest,
    run the following command in current path:
    $ pytest
    """
    def test_context_init(self):
        obj = Context(a=1, b=1.0, c=1+2j, d='abc')
        assert obj.a == 1
        assert obj.b == 1.0
        assert obj.c == 1+2j
        assert obj.d == 'abc'

    def test_setattr(self):
        obj = Context()
        obj.a = 100
        assert obj.a == 100

    def test_len(self):
        obj = Context(a=1, b=1.0, c=1 + 2j, d='abc')
        assert len(obj) == 4

    def test_print(self):
        obj1 = Context(e=1)
        assert str(obj1.__str__()) == 'Class (e = 1)'
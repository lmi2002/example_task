from home1 import Stack
from home1 import LimitExceedError
from home1 import EmptyStackError
import pytest

class TestClass(object):
    def test_init_empty(self):
        s = Stack()
        assert s.limit is None
        assert s.type is object

    def test_init_set(self):
        s = Stack(data_type=float, limit=10)
        assert s.limit == 10
        assert s.type is float

    def test__push_limit_error(self):
        s = Stack(data_type=int, limit=0)
        with pytest.raises(LimitExceedError):
            s._push(2)

    def test__push_type_error(self):
        s = Stack(data_type=int, limit=2)
        with pytest.raises(TypeError):
            s._push(2.1)

    def test_push_ok(self):
        s = Stack(data_type=str, limit=10)
        s.push('Vova')
        assert s.pull() == 'Vova'

    def test_pull_error(self):
        s = Stack(data_type=int, limit=10)
        s.push(1)
        s.pull()
        with pytest.raises(EmptyStackError):
            s.pull()

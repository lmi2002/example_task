class LimitExceedError(StandardError):
    pass


class EmptyStackError(StandardError):
    pass


class Stack:
    def __init__(self, limit=None, data_type=object):
        self.__items = []
        self.limit = limit
        self.data_type = data_type

    def __str__(self):
            print 'self type', self.type
            return 'Stack<{}>'.format(str(self.type)[7:-2])

    def _push(self, item):
        if self.count() < self.limit:
            raise LimitExceedError

        if not isinstance(item, self.data_type):
            raise TypeError

    def push(self, item):
        self._push(item)
        self.__items.insert(0, item)

    def pull(self):
        try:
            return self.__items.pop(0)
        except IndexError:
            raise EmptyStackError

    def count(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    @property
    def type(self):
        return self.data_type



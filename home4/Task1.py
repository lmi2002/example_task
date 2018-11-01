import re

class ValidationError(Exception):
    """
    Self defined exception, used in RealComplex class.
    Raises when trying to add neither complex nor real type attribute.
    """
    pass
class Context:

    context = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.validate_name(key)
        self.context.update(kwargs)

    def __str__(self):
        describe = "Class ("
        for keys, values in self.context.items():
            describe += '{key} = {value}, '.format(key=keys, value=values)
        describe = describe[:-2] + ')' if self.context.items() else\
            describe + (')')
        return describe

    def __setattr__(self, key, value):
        self.validate_name(key)
        self.context.update({key:value})

    def __getattr__(self, key):
        return self.context[key]

    def __len__(self):
        return len(self.context)

    def __iter__(self):
        for key, value in self.context.items():
            yield {key: value}

    @staticmethod
    def validate_name(name):
        reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
        if not reg.match(name):
            raise NameError('Wrong variable name')


class RealContext(Context):

    def __init__(self, **kwargs):
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key:value})

    @staticmethod
    def validate_type(name):
        if not (isinstance(name, int) or isinstance(name, float)):
            raise TypeError ('Wrong variable type')


class ComplexContext(Context):

    def __init__(self, **kwargs):
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key: value})

    @staticmethod
    def validate_type(name):
        if not isinstance(name, complex):
            raise TypeError('Wrong variable type')


class NumberContext(RealContext, ComplexContext):

    def __init__(self, **kwargs):
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key: value})

    @staticmethod
    def validate_type(value):
        if isinstance(RealContext.validate_type(value), TypeError) and \
                isinstance(ComplexContext.validate_type(value), TypeError):
            raise ValidationError('Variable type neither real nor complex')

# obj = Context(a=10, b=3, c='abc')
# obj = RealContext(a=10, b=3, c=1)
obj = ComplexContext()
# obj = NumberContext()
obj.a = 1+1j
print(obj)

# obj.d = 'ggg'
# iterator = iter(obj)
#
# print(next(iterator))
# print(next(iterator))
#
# print(obj.context)
# print(obj)
# print(len(obj))
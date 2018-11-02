from abc import ABCMeta, abstractmethod
import re


class ValidationError(Exception):
    """
    Self defined exception, used in RealComplex class.
    Raises when trying to add neither complex nor real type attribute.
    """
    pass


class NumberBaseContext:
    """
    Abstract interface class
    """
    __metaclass__=ABCMeta

    @abstractmethod
    def __init__(self, **kwargs):
        """ Self defined constructor with specific validation"""

    @abstractmethod
    def __setattr__(self, key, value):
        """Self defined setattr with specific validation"""

    @staticmethod
    @abstractmethod
    def validate_type(name):
        """Validation of context values"""


class Context:
    """
    Stores context of variables and their values as dictionary
    """


    def __init__(self, **kwargs):
        """
        Class constructor
        :param kwargs: values that will be added to class context on object
         initialization
        """
        self.__dict__['context'] = {}
        for key, value in kwargs.items():
            self.validate_name(key)
        self.context.update(kwargs)

    def __str__(self):
        """
        Prints object context
        :return: string like: Class (a = 10, b = 'a')
        """
        describe = "Class ("
        for keys, values in self.context.items():
            describe += '{key} = {value}, '.format(key=keys, value=values)
        describe = describe[:-2] + ')' if self.context.items() else\
            describe + (')')
        return describe

    def __setattr__(self, key, value):
        """
        Add item to class context as setting class attribute
        :param key: variable name
        :param value: variable value
        :return: None
        """
        self.validate_name(key)
        self.context.update({key:value})

    def __getattr__(self, key):
        """
        Getting context attribute value as class attribute value
        :param key: variable name from context
        :return: variable value
        """
        return self.context[key]

    def __len__(self):
        """
        Counts number of context values
        :return: number of context values
        """
        return len(self.context)

    def __iter__(self):
        """
        Makes class iterable
        :return: next item from context
        """
        for key, value in self.context.items():
            yield {key: value}

    @staticmethod
    def validate_name(name):
        """
        Context item name validator
        :param name: variable name
        :return: raises error if name is invalid python lexeme
        """
        reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
        if not reg.match(name):
            raise NameError('Wrong variable name')


class RealContext(Context):
    """
    Context child with strong data validation. Accept int and float values only
    """
    def __init__(self, **kwargs):
        """
        Class constructor. Inherits from parent and applies self validation
        """
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        """
        Inherits __setattr__ from parent and applies self validation
        """
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key:value})

    @staticmethod
    def validate_type(name):
        """
        Context item type validator
        :param name: value for validation
        :return: raises TypeError if value neither float nor int
        """
        if not (isinstance(name, int) or isinstance(name, float)):
            raise TypeError ('Wrong variable type (Neither int nor float)')


class ComplexContext(Context):
    """
    Context child with strong data validation. Accept real values only
    """
    def __init__(self, **kwargs):
        """
        Class constructor. Inherits from parent and applies self validation
        """
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        """
        Inherits __setattr__ from parent and applies self validation
        """
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key: value})

    # @staticmethod
    def validate_type(self,name):
        """
        Context item type validator
        :param name: value for validation
        :return: raises TypeError if value in not complex
        """
        if not isinstance(name, complex):
            raise TypeError('Wrong variable type (Not Complex)')


class NumberContext(NumberBaseContext, RealContext, ComplexContext):
    """
    Context child with strong data validation. Accept real values only
    """
    def __init__(self, **kwargs):
        """
        Class constructor. Inherits from parent and applies self validation
        """
        Context.__init__(self, **kwargs)
        for key, value in self.context.items():
            self.validate_type(value)
        self.context.update(kwargs)

    def __setattr__(self, key, value):
        """
        Inherits __setattr__ from parent and applies self validation
        """
        Context.__setattr__(self, key, value)
        self.validate_type(value)
        self.context.update({key: value})

    @staticmethod
    def validate_type(value):
        """
        Context item type validator
        :param value: value for validation
        :return: raises ValidationError if value is other then 
                int, float, complex
        """
        err_count = 0
        try:
            validate_type(value)
        except TypeError:
            err_count += 1
        try:
            ComplexContext.validate_type(value)
        except TypeError:
            err_count += 1
        if err_count == 2:
            raise ValidationError('Variable type neither real nor complex')



# obj = Context(a=10, b=3, c='abc')
# obj = RealContext(a=10, b=3, c=1)
# obj = ComplexContext()
# obj = NumberContext()
# obj.a = 1+1j
# obj.b = 1.0
obj = Context()
obj.a = 10

obj2 = Context()
obj2.b = 20

print (obj2)



# obj2 = Context(a=2)
# print(obj2)

# obj.d = 'ggg'
# iterator = iter(obj)
#
# print(next(iterator))
# print(next(iterator))
#
# print(obj.context)
# print(obj)
# print(len(obj))
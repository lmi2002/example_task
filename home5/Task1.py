import re

def validate_name(name):
    reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
    if not reg.match(name):
        raise NameError('Wrong variable name')


def validate_input(str):
        try:
            inp = str.split('=')
            validate_name(inp[0])
            return {inp[0]: inp[1]}
        except:
            raise TypeError('Wrong input format')

# class CustomMetaclass(type):
#
#     def __new__(cls, classname, bases, params):
#         return type.__new__(cls, classname, bases, params)
#
#     def __str__(cls):
#         # describe = 'Class <{}>:'.format(cls.__name__)
#         print('XXX')
#         # return describe

def output(self):
    describe = 'Class <{}>:\n'.format(self.__class__.__name__)
    params='\n'.join(['{key} = {value}'.format(key=k, value=v) for k,v in self.__class__.__dict__.items() if not k.startswith('__')])
    return describe + params

def main():
    classname = input('Classname = ')
    params = {}
    while True:
        a = input('Set up class items ')
        if a != '':
            try:
                params.update(validate_input(a))
            except Exception:
                print('Input class properties in a=x format')
        else:
            break

    params.update({'__str__': output})
    Myclass = type(classname, (), params)
    print(Myclass())


if __name__== "__main__":
    main()


# print({k: v for k, v in Vova.__dict__.items() if not k.startswith('__')})

# for key, value in v.__class__.__dict__.items():
# # for key, value in v.__dict__.items():
#     print('{} = {}'.format(key, value))
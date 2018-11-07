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

class CustomMetaclass(type):
    def __new__(cls, classname, bases, params):
        return type.__new__(cls, classname, bases, params)

    def __str__(cls):
        # describe = 'Class <{}>:'.format(cls.__name__)
        print('XXX')
        # return describe



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

    Myclass = CustomMetaclass(classname, (), params)

    obj = Myclass()
    print (obj)


if __name__== "__main__":
  main()
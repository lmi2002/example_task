import re

def validate_name(name):
    reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
    if not reg.match(name):
        raise NameError('Wrong variable name')


def validate_str(str):
    inp = str.split('=')
    validate_name(inp[0])
    return {inp[0]: inp[1]}

def main():
    cls = input('Classname = ')
    dct = {}
    while True:
        a = input('Set up class items ')
        if a != '':
            try:
                dct.update(validate_str(a))
            except NameError:
                pass
        else:
            break
    print(dct)


if __name__== "__main__":
  main()
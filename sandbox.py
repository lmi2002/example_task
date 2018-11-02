import time
import json
import pickle
import csv
import keyword

def str_tuple(st):
    lst = []
    for i in range(len(st)):
        lst.append(ord(st[i]))
    return tuple(lst)


def foo(n):
    if n == 1:
        return 1
    return n*foo(n-1)


def clock(fn):
    def wrapper(n):
        start = time.clock()
        fn(n)
        end = time.clock()
        print ('delay= ', end-start)
        return fn(n)
    return wrapper


@clock
def foo1(n):
    if n == 1:
        return 1
    return n*foo(n-1)


def unpacker(*args, **kwargs):
    result = []
    lst = list(args) + list(kwargs.keys())
    for arg in lst:
        if not hasattr(arg, '__iter__'):
            result.append(arg)
        else:
            result += unpacker(*arg)
    return result


def power(x):
    def internal(y):
        return x**y
    return internal

# p = power(4) #- fabric
# print p(2)


def exporter():
    f = open('input.json', 'r')
    j = json.loads(f.read())
    out = open('output.bin', 'wb')
    pickle.dump(j, out)

    out.close()
    f.close()


def importer():
    f = open('output.bin', 'rb')
    print (pickle.load(f))
    f.close()


def privet(hello):
    def internal(name, surname):
        return '{}, {} {}'.format(hello, name, surname)
    return internal


def foo():
    with open('input.csv', 'r') as file:
        j = open('output.json', 'w')
        sfile = csv.reader(file, delimiter=',')
        d = dict()
        i = 0
        for row in sfile:
            d[i] = max(row)
            i += 1
        print(d)
        j.write(json.dumps(d,indent=4))
        j.close()

def process(string):
    def internal(path):
        file = open(path, 'w')
        file.write(string)
        file.close()
    return internal


class Language:
    _words = []
    def lexicon(self):
        return self._words


class Proglanguage(Language):
    _keywords = []
    def lexicon(self):
        return self._keywords


class Python(Proglanguage):
    _keywords = keyword.kwlist

#
# p = Python()
# print(p.lexicon())

print('Start')

class A:

    def __init__(self):

        print('Constructor A')

class B(A):

    def __init__(self):
        super(B, self).__init__()
    #     # A.__init__(self,a)
    #     # self.context.append(2)
        print('Constructor B')

class C(B):
    def __init__(self):
        super(C, self).__init__()
        #     # A.__init__(self,a)
        #     # self.context.append(2)
        print('Constructor C')

class D(B):
    def __init__(self):
        super(D, self).__init__()
        #     # A.__init__(self,a)
        #     # self.context.append(2)
        print('Constructor D')

    def zzz(self):
        print('I am D')
    pass

class E(C):
    def __int__(self):
        print('int E')
        self.zzz()

e = E()


# b = B([1])

# print(b.context)





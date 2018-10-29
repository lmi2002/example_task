class Context:

    context = {}

    def __init__(self, **kvargs):
        self.context.update(kvargs)


    def __str__(self):
        describe = "Class ("
        for keys, values in self.context.items():
            describe += '{key} = {value}, '.format(key=keys, value=values)
        describe = describe[:-2] + ')'
        return describe

    def __setattr__(self, key, value):
        self.context.update({key:value})

    def __getattr__(self, key):
        return self.context[key]

    def __len__(self):
        return len(self.context)



obj = Context(a=10, b=3)


print(obj.context)
print(obj)
print(len(obj))
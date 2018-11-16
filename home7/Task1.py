import os

class LogReader:

    def __init__(self, path=os.getcwd(), mask='*.log'):
        self.path = path
        self.mask = mask

        self.log_filenames = sorted([f for f in os.listdir(self.path) if f[-4:] == self.mask[-4:]])
        self.txt_files = list(map(lambda x: open(os.path.join(self.path, x), 'r'), self.log_filenames))

    def __iter__(self):
        for file in self.txt_files:
            for l in file:
                yield l.rstrip('\n')

obj = LogReader()

for line in obj:
    print(line)





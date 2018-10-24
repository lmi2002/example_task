import xlrd
import json
import csv

class FileConverter:

    def __init__(self, filename):
        self.filename = filename
        self.book = xlrd.open_workbook(filename)
        self.sh = self.book.sheet_by_index(0)

    @staticmethod
    def read_xls(filename):
        try:
            book = xlrd.open_workbook(filename)
        except FileNotFoundError:
            print('File {} not found'.format(filename))
            book = None
        # else:
            # print("The number of worksheets is {0}".format(book.nsheets))
            # print("Worksheet name(s): {0}".format(book.sheet_names()))
            # sh = book.sheet_by_index(0)
            # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
            # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
            # for i in range(1, sh.nrows):
            #     for j in range(sh.ncols):
            #         print(sh.cell_value(rowx=i, colx=j))
        return book


    def read_line(self, number):
        sh = self.book.sheet_by_index(0)
        line = []
        for i in range(sh.ncols):
            line.append(sh.cell_value(rowx=number, colx=i))
        return line


    def convert_sheet(self):
        output = []
        for i in range(1, f.sh.nrows):
            d = dict(zip(f.read_line(0), f.read_line(i)))
            output.append(d)
        return output


    def write_data(self, data):
        with open('output.json', 'w') as jfile:
            jfile.write(json.dumps(data, indent=4))

        with open('output.csv', 'w') as cfile:
            csvwriter = csv.writer(cfile, delimiter=',')
            for row in data:
                csvwriter.writerow(row.values())


f = FileConverter('Input.xlsx')
f.write_data(f.convert_sheet())
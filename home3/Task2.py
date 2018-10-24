import xlrd

class FileConverter:

    @staticmethod
    def read_xls(filename):
        try:
            book = xlrd.open_workbook(filename)
        except FileNotFoundError:
            print('File {} not found'.format(filename))
        else:
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sh = book.sheet_by_index(0)
            # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
            # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
            for i in range(1, sh.nrows):
                for j in range(sh.ncols):
                    print(sh.cell_value(rowx=i, colx=j))

FileConverter.read_xls('Input.xlsx')

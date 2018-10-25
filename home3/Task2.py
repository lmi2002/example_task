import xlrd
import json
import csv
import pickle
import datetime
import re

class FileConverter:

    def __init__(self, filename):
        self.filename = filename
        self.book = xlrd.open_workbook(filename)
        self.sh = self.book.sheet_by_index(0)


    def read_line(self, number):
        sh = self.book.sheet_by_index(0)
        line = []
        c0 = sh.cell(rowx=number, colx=0).value
        c1 = sh.cell(rowx=number, colx=1).value
        c2 = sh.cell(rowx=number, colx=2).value

        try:
            self.name_valid(c0)
            line.append(c0)
            self.email_valid(c1)
            line.append(c1)
            self.date_valid(c2)
            c2 = datetime.datetime(*xlrd.xldate_as_tuple(c2, self.book.datemode)).date().isoformat()
            c2 = datetime.datetime.strptime(c2, "%Y-%m-%d").strftime("%m/%d/%Y")
            line.append(c2)
        except Exception:
            line = [c0, c1, c2]
            if number:
                with open('errors.log', 'a') as file:
                    file.write(str(line)+'\n')
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

        with open('output.bin', 'wb') as bfile:
            pickle.dump(data, bfile)


    @staticmethod
    def date_valid(date):
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
        except Exception:
            raise ValueError


    @staticmethod
    def email_valid(email):
        reg = re.compile(r'^[A-Za-z0-9\.\+_]+@[A-Za-z0-9\._]+\.[a-zA-Z]*$')
        if reg.match(email) is None or email.split('@')[1].count('.') > 2:
            raise ValueError


    @staticmethod
    def name_valid(name):
        reg = re.compile('^[a-zA-Z]+$')
        if reg.match(name) is None:
            raise ValueError



f = FileConverter('Input.xlsx')
# print(FileConverter.email_valid('vov_a@gmail.com'))
# print(f.sh.cell(rowx=1, colx=1))
f.write_data(f.convert_sheet())


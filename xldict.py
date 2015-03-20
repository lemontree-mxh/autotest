import xlrd
from collections import OrderedDict

class xldict():
    def __init__(self, filename, header=1):
        self.__head = header
        self.__xl = xlrd.open_workbook(filename)
        self.__totalsheets = len(self.__xl.sheets())
        self.__nrows = self.__xl.sheet_by_index(0).nrows

    def getdict(self, line, sheetno):
        result = OrderedDict()
        sheet = self.__xl.sheet_by_index(sheetno)
        headers = sheet.row_values(self.__head)
        data = sheet.row_values(line)
        for i in range(len(headers)):
            result[headers[i]] = data[i]
        return result

    def getwhdict(self, line):
        result = OrderedDict()
        for i in range(self.__totalsheets):
            odict = self.getdict(i)
            result.update(odict)
        return result

    def getrows(self):
        return self.__nrows

    def getsheetno(self):
        return self.__totalsheets

if __name__ == '__main__':
    xl = xldict('E:\\Python_codes\\autotest\\test_cases\\fund.xlsx')
    a = xl.getdict(2, 0)
    print(xl.getsheetno())
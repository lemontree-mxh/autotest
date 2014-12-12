__author__ = 'maxh'
# coding = utf-8
from autourl import autourl
from xldict import xldict
from headParse import xl2array
import time


merchant_entry = autourl()
xl = xldict('D:\\PycharmProjects\\autotest\\test_cases\\ets-demo-waika.xlsx')

for sheetno in range(xl.getsheetno()):
    for line in range(2, xl.getrows()):
        print('Run Test Case ' + str(line - 1))
        data = xl.getdict(line, sheetno)
        for key in data:
            header = xl2array(key)
            if sheetno > 2:
                time.sleep(3)
            print(header.elem + ':' + header.value + ':' + header.action + '-' + data[key] + 'LEN:', len(data[key]))
            merchant_entry.execute(header.elem, header.value, header.action, data[key])
        time.sleep(2)
print('completed')
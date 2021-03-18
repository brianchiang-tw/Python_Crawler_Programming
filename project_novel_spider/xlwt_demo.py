import xlwt

book = xlwt.Workbook(encoding='utf-8')

sheet_1 = book.add_sheet('Sheet1')
sheet_2 = book.add_sheet('Sheet2')

sheet_1.write(1, 1, 'Hello, World')
sheet_1.write(2, 2, 'Use python to operate excel file')
sheet_2.write(2, 2, '你好')

book.save('demo_xlwt_lib.xls')
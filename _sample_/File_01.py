# Program extracting all columns
# name in Python 
"""import xlrd

loc = ('Data')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))
"""

import datetime

timestamp = datetime.datetime.fromtimestamp(43673.0)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

'''

fname=input('Enter file name:')
with open(fname) as f:
    data=f.readlines() # Here it will read data line by line
    for row in data: # Here it make loop to read and separate the data into feilds
        row=row.rstrip('\n')
        feilds=row.split(',')  '''

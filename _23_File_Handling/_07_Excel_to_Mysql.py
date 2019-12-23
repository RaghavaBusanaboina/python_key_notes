import postgres
from xlsxwriter.workbook import Workbook

user = 'postgres'  # your username
passwd = 'naveen1213'  # your password
host = 'local host'  # your host
db = 'postgres'  # database where your table is stored
table = 'customers_customer'  # table you want to save

con = postgres.ConnectionPool(user=user, passwd=passwd, host=host, db=db)
# con = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db)
cursor = con.cursor()

query = "SELECT * FROM %s;" % table
cursor.execute(query)

workbook = Workbook('C:/Users/manne/Desktop/Book3.xls')
sheet = workbook.add_worksheet()
for r, row in enumerate(cursor.fetchall()):
    for c, col in enumerate(row):
        sheet.write(r, c, col)

Now slow...
# 3,154,368 records, 679.477 seconds. (11 minutes)
import pyodbc
import os
import time

def sqlClass():
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=YourServer;DATABASE=YourDatabase;UID=YourUser;PWD=Password')
	cursor = cnxn.cursor()
	return cursor
	
def writeSlow(data):
	with open('C:\\results.txt','a',encoding='utf-8') as file:
		file.write(str(data.CustomerNumber) + ',' + str(data.OrderNumber) + ',' + str(data.Amount) + '\n')

def main():
	sql = sqlClass()
	rows = sql.execute('SELECT CustomerNumber,OrderNumber,Amount FROM dbo.TestData').fetchall()
	for row in rows:
		writeSlow(row)

if __name__ == '__main__':
	t0 = time.time()
	main()
	t1 = time.time()
	total = t1-t0
	print(total)

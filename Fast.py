# 3,154,368 records, 14.62 seconds.
import pyodbc
import os
import time

def sqlClass():
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=YourServer;DATABASE=YourDatabase;UID=YourUser;PWD=Password')
	cursor = cnxn.cursor()
	return cursor

def writeFile(data):
	with open('C:\\results.txt','a',encoding='utf-8') as file:
		for x in data:
			file.write(str(x.CustomerNumber) + ',' + str(x.OrderNumber) + ',' + str(x.Amount) + '\n')

def results(sql):
	iter = sql.execute('SELECT CustomerNumber,OrderNumber,Amount FROM dbo.TestData')
	while True:
		rows = iter.fetchmany(50000)
		if not rows:
			break
		for row in rows:
			yield row
def main():
	sql = sqlClass()
	data = results(sql)
	writeFile(data)
	
if __name__ == '__main__':
	t0 = time.time()
	main()
	t1 = time.time()
	total = t1-t0
	print(total)

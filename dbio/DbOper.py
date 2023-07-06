import sqlite3

class DbOper(object):
	def __init__(self, date = ''):
		self.cx = sqlite3.connect('./dbio/app.db')
		self.cu= self.cx.cursor()
		
	def writeTable(self, sql = ''):
		self.cu.execute(sql)
		
	def readTable(self, sql = ''):
		self.cu.execute(sql)
		rows=self.cu.fetchall()
		return rows
		
	def closeDb(self):
		self.cu.close()
		self.cx.commit()
		self.cx.close()


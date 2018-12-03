#!/usr/bin/env python
# -*- coding: utf_8 -
import Pyro.core
import Pyro.naming
import select
Pyro.core.initServer()
daemon = Pyro.core.Daemon(host="192.168.30.129",port = 8888)
import sqlite3
# locator = Pyro.naming.NameServerLocator()
#ns = locator.getNS()
#daemon.useNameServer(ns)
class sqlite_remote():
	"""docstring for test"""
	def __init__(self):
		print "__init__"
		

	def execute_sql(self,database,sql):
		print "getSQLite"
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		cursor.close()
		
		return data

	def fetchone(self):
		return self.fetchone()
		

		

class ObjectImpl(Pyro.core.ObjBase,sqlite_remote):
	def __init__(self):
		Pyro.core.ObjBase.__init__(self)
		sqlite_remote.__init__(self)

obj = ObjectImpl()

daemon.connect(obj,"sqlite")
def run():
	while True:
		sockets = daemon.getServerSockets()
		ins,outs,exs= select.select(sockets,[],[],1)
		for s in sockets:
			if s in ins:
				daemon.handleRequests()

try:
	run()
	pass
except Exception as e:
	daemon.shutdown()
	raise e

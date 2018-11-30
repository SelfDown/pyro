#!/usr/bin/env python
# -*- coding: utf_8 -
import Pyro.core
import Pyro.naming
import select
Pyro.core.initServer()
daemon = Pyro.core.Daemon(host="192.168.30.129",port = 7766)
# locator = Pyro.naming.NameServerLocator()
#ns = locator.getNS()
#daemon.useNameServer(ns)
class test:
	"""docstring for test"""
	def __init__(self):
		print "__init__"

	def helloWorld(self):
		print "say hello world"
		return "hello world"

class ObjectImpl(Pyro.core.ObjBase,test):
	def __init__(self):
		Pyro.core.ObjBase.__init__(self)
		test.__init__(self)

obj = ObjectImpl()

daemon.connect(obj,"object")
def run():
	while True:
		sockets = daemon.getServerSockets()
		ins,outs,exs= select.select(sockets,[],[],2)
		for s in sockets:
			if s in ins:
				daemon.handleRequests()

try:
	run()
	pass
except Exception as e:
	daemon.shutdown()
	raise e

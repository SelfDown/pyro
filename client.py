#!/usr/bin/env python
# -*- coding: utf_8 -
import Pyro.core
import Pyro.naming
Pyro.core.initClient(banner = 0)
obj = Pyro.core.getProxyForURI("PYROLOC://192.168.30.129:7766/object")

print "start",obj
# help(obj)
print obj.create_client()
# data = obj.helloWorld()
# print data
print "end"
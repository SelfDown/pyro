#!/usr/bin/env python
# -*- coding: utf_8 -
import Pyro.core
import Pyro.naming
Pyro.core.initClient(banner = 0)
obj = Pyro.core.getProxyForURI("PYROLOC://192.168.30.129:8888/sqlite")

print "start",obj

data = obj.execute_sql("database.db","select * from collection_list order by id desc")

print "end",data

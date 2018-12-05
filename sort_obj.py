#!/usr/bin/env python
# -*- coding: utf_8 -

data = [{"name":"zz","sort":1000},{"name":"sss","sort":23},{"name":"kkk","sort":800}]
data = sorted(data,key=lambda item:item["sort"],reverse=True)
print data
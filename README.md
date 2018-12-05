# pyro
一个远程能访问sqlite的程序，返回一个sqlite 的连接 connect ，原api接口不变
 
利用Pyro远程对象访问，在sqlite服务端部署一套程序，以8848端口暴露出去
远程访问对象api 一样

源pyro建议搭建一个注册服务器。感觉模仿open_opc 比较好，直接ip加端口访问，获取到对象

server 是服务端代码，可以做出servcie，或者开机启动

client 是客户端代码


pyro-ns   (Name Server)


pyro-es   (Event Server)



pyro-nsc   (Name Server Control tool)

pyro-xnsc   (Graphical NS control tool)

pyro 工具列表
https://pythonhosted.org/Pyro/4-usage.html

事件查看器  eventvwr.msc

**判断类型是否为字符串
   len([t for t in tags if type(t) not in types.StringTypes])==0



import win32com
from win32com.client import Dispatch, constants

w = win32com.client.Dispatch('Word.Application')
# 或者使用下面的方法，使用启动独立的进程：
# w = win32com.client.DispatchEx('Word.Application')

# 后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0

# 打开新的文件
doc = w.Documents.Open( FileName = filenamein )
# worddoc = w.Documents.Add() # 创建新的文档

# 插入文字
myRange = doc.Range(0,0)
myRange.InsertBefore('Hello from Python!')

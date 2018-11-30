# pyro
一个远程能访问sqlite的程序，返回一个sqlite 的连接 connect ，原api接口不变
 
利用Pyro远程对象访问，在sqlite服务端部署一套程序，以8848端口暴露出去
远程访问对象api 一样

源pyro建议搭建一个注册服务器。感觉模仿open_opc 比较好，直接ip加端口访问，获取到对象

server 是服务端代码，可以做出servcie，或者开机启动

client 是客户端代码

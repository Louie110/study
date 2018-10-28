# coding: utf-8

import pymysql  

class MySQLConnect(object):

    def __init__(self,host,user,passwd,port,dbase,charset,sql):
        self.host = host       # 主机
        self.user = user       #用户
        self.passwd = passwd   #用户密码
        self.port = port       #端口号
        self.dbase = dbase     #数据库
        self.charset = charset #编码格式
        self.sql = sql 
        
    def connectMysql(self):
        try:
            self.db = pymysql.connect(host = self.host,user = self.user,passwd = self.passwd,port = self.port,database = self.dbase,charset = self.charset)   #建立数据库连接
            self.cursor = self.db.cursor()   #获得游标
        except Exception:    #捕捉与程序相关的所有异常
            print('connect mysql error.')
    
    ###查询数据
    def selectdata(self):
        '''下面执行sql语句，
        如果有异常，执行except子句，
        没有异常的话执行else子句，
        无论是否发生异常最后都要执行finally子句'''

        try:
            self.cursor.execute(self.sql)
        except:
            print(self.sql + ' execute failed')
        else:
            dt = self.cursor.fetchall()
            print(dt)
        finally:
            self.cursor.close()
            self.db.close()

##创建实例对象进行测试   
dj = MySQLConnect('localhost','root','643521',3306,'example','utf8','select * from grade;')
dj.connectMysql()
dj.selectdata()
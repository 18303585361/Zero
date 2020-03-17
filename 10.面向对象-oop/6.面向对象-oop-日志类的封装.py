# 日志类的封装
'''
日志类
    class MyLog
    功能：
        能够随时写入一个日志信息
分析：
    日志文件在什么地方？  默认在当前目录
    日志的文件名时什么？  当前日期 2020-03-15.log
    日志的格式是什么样的？ 2020-03-15 12:12:12 错误信息。。。

    属性：成员属性的作用就是存储信息，供成员方法来使用
        1.fileurl   日志文件的地址
        2.filename  日志文件的名称
        3.fileobj   打开的文件对象

    方法：具体完成的一个功能的过程
        1.__init__()    初始化方法：完成对象的初始化并打开文件
        2.wlog()        负责接收用户给的日志信息，并写入到日志文件中
        3.__del__()     析构方法：在对象被销毁时，关闭打开的文件
'''

import time
class MyLog():
    # 成员属性
    fileurl = './'
    filename = time.strftime('%Y-%m-%d')+'.log'
    fileobj = None
    # 成员方法
    def __init__(self,):
        # 打开文件
        self.fileobj = open(self.fileurl+self.filename,'a+',encoding='utf-8')

    def wlog(self,s):
        # 准备数据，开始写入
        # 2020-03-15 12:12:12 错误信息。。。
        date = time.strftime('%Y-%m-%d %H:%M:%S\n')
        msg = date + s + '\n'
        # 写入
        self.fileobj.write(msg)

    def __del__(self):
        # 关闭打开的文件
        self.fileobj.close()

# 实例化对象
w = MyLog()

# 调用方法 写日志
w.wlog('今天天气不太好，而且楼上在装修。。。')
w.wlog('楼上装修能理解，但是说话不算数，很讨厌。。。')






































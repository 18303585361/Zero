# 内置成员
'''
内置成员：
    1.类/对象.__dict__       获取类/对象的所属成员
    2.类/对象.__doc__        获取类/对象的文档信息
    3.类.__name__            获取类名称组成的字符串
    4.类/对象.__module__     获取类所在的文件名称，如果是当前文件，显示为__main__
    5.类.__bases__           获取当前类的父类列表
      类.__base__            获取当前类的第一个父类
    6.类.__mro__             MRO列表 获取当前类的继承链
'''

class Demo():
    '''
    此处是类的说明文档
    '''
    name = 'a'
    age = 20

    def say(self):
        print('会说会唱')

obj = Demo()
obj.san = 'aaa'
# 获取类/对象的所属成员   格式:类/对象.__dict__
# res = Demo.__dict__ # 获取当前类的所属成员
# res = obj.__dict__  # 获取当前对象的所属成员

# 获取类的文档信息  格式:类/对象.__doc__
# res = Demo.__doc__
# res = obj.__doc__

# 获取类名称组成的字符串   格式：类.__name__
# res = Demo.__name__

# 获取类所在的文件名称，如果是当前文件，显示为__main__
# res = Demo.__module__

# 获取当前类的父类列表
# res = Demo.__bases__    # 获取继承的所有的父类列表
# print(Demo.__base__)    # 获取继承的第一个父类

# MRO列表 获取当前类的继承链
# res = Demo.__mro__
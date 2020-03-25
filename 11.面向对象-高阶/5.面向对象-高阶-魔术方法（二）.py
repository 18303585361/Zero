# 面向对象 魔术方法（二）
'''
1. __len__
    触发机制：当使用 len 函数去检测当前对象的时候自动触发
    作用:可以使用 len 函数检测当前对象中某个数据的信息
    参数：一个 self 接收当前对象
    返回值：必须有，并且必须是一个整型
    注意事项：len 要获取什么属性的值，就在返回值中返回哪个属性的长度即可
2. __str__
    触发机制：当使用 str 或者 print 函数对对象进行操作时，自动触发
    作用：代替对象进行字符串的返回，可以自定义打印的信息
    参数：一个 self 接收当前对象
    返回值：必须有，而且必须是字符串类型
3. __repr__
    触发机制：在使用 repr 方法对当前对象进行转换时自动触发
    作用：可以设置 repr 函数操作对象的结果
    参数：一个 self 接收当前对象
    返回值：必须有，而且必须是字符串类型
    注意事项：正常情况下，如果没有 __str__ 方法， __repr__ 方法就会代替 __str__方法
4. __bool__
    触发机制：当前使用 bool 函数转换当前对象时，自动触发。默认情况下，对象会转为True
    作用：可以代替对象进行 bool 类型的转换，可以转换任何数据
    参数：一个 self 接收对象
    返回值：必须是一个 bool 类型的返回值
'''
class Demo():
    listurl = []

    # 可以代替对象使用 len 函数，并返回一个制定的整型
    def __len__(self):
        return len(self.listurl)

    # 可以代替对象进行 str 或者 print 的字符串信息返回
    def __str__(self):
        return '<这是当前脚本中的一个 对象 str>'

    def __repr__(self): # 可以代替 str 方法触发
        return '这是一个对象 repr'

    def __bool__(self):
        return bool(self.listurl)

# 实例化对象
obj = Demo()

# res = len(obj)
# res = str(obj)
# print(res)

# print(obj)

# res = repr(obj)

res = bool(obj)
print(res)



























































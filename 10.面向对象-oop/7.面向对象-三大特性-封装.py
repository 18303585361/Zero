# 面向对象的三大特性：封装、继承、多态
# 封装 
'''
封装
    使用特殊的语法，对成员属性和成员方法进行包装，达到保护和隐藏的目的
    但是一定注意，不能把成员全部封装死
    被封装的成员，主要是供类的内部使用
    被特殊语法封装的成员，会有不同的访问权限
    为了限制一些访问和操作，但是不能全部都限制（不能不让使用）
    被封装的成员只是限制了访问的权限，并不是不让访问

封装的级别
    成员   ==> 公有的
    _成员  ==> 受保护的（约定俗成，而Python没有具体实现）
    __成员 ==> 私有的
    1.公有（public）    2.受保护的（protected）    3.私有的（private）
类的内部    ok                  ok                      ok
类的外部    ok           No（Python可以访问）            No

在Python中，给成员进行私有化，其实就是改了成员的名字
私有化 ==> _类名__成员

'''
class Person():
    # 成员属性
    name = '名字'
    _age = '年龄' # 在成员前面加一个下划线 _，就变成受保护的成员
    __sanwei = '三围'   # 在成员前面加两个 __下划线，就变成私有的成员

    # 初始化方法
    def __init__(self,n,a,s):
        self.name = n
        self._age = a
        self.__sanwei = s

    def func(self):
        # 在类的内部可以操作任意成员
        print(self.__sanwei)
        self.__kiss()


    # 成员方法
    def say(self):
        print('聊聊人生和理想')
    def _sing(self):
        print('高歌一曲，豪放一生')
    def __kiss(self):
        print('打个kiss。。。')

# 实例化对象
ym = Person('杨幂',28,'60 50 60')

print(ym._age)  # 类的外部不能操作  受保护的成员（但是Python中可以）
# print(ym.__sanwei)  # 类的外部不能操作  私有成员属性
# print(ym._Person__sanwei)   # 可以使用特殊的语法获取私有成员

ym._sing()
ym.func()
# ym.__kiss()

# 查看对象的所有成员
print(ym.__dict__)  # 可以获取当前对象的所有信息
# print(Person.__dict__) # 可以获取当前类的所有成员信息































































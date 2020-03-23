# 类方法分类
'''
共有4种方法：
    1.对象方法：通过对象调用类方法
        特征：1.在类中定义的方法，含有 self 参数
              2.含有 self 的方法只能使用对象进行调用
              3.该方法会把调用的对象传递进来
    2.类方法
        特征：1.在类中定义的方法，使用装饰器 @classmethod 进行了装饰
              2.方法中有 cls 这个形参，不需要实例化对象，可以使用类和对象进行调用
              4.会把调用这个方法的类传递进来
    3.绑定类方法
        特征：1.在类中定义的方法
              2.只能使用类进行调用
              3.不会传递对象或者类进来
    4.静态方法
        特征：1.在类中定义的方法，使用 装饰器 @staticmethod 进行了装饰
              2.可以使用类和对象进行调用
              3.不会传递对象或者类进来
'''
class Demo():

    # 对象方法：
    def func1(self):
        print(self)
        print('this is object function func1')

    # 类方法：
    @classmethod
    def func2(cls, a):
        print(cls, a)
        print('this is class function func2')

    # 绑定类方法
    def func3():
        print('this is bind class function func3')

    # 静态方法
    @staticmethod
    def func4():
        print('this is staticmethod function func4')

# 实例化对象
# obj = Demo()

# 对象方法  调用
# obj.func1()
# Demo.func1('a') # 不能直接使用类调用 对象方法，除非传递一个对象进去，不推荐使用

# 类方法   调用
# Demo.func2()  # 可以使用类直接调用
# obj.func2()   # 即便使用对象进行调用，传递进去的依然是类

# 绑定类方法
# Demo.func3()    # 只能使用类调用绑定类方法
# obj.func3() # 不能使用对象调用绑定类方法

# 静态方法调用
# Demo.func4()
# obj.func4()



































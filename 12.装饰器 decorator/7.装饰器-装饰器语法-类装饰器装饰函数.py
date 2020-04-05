# 类装饰器装饰函数

class Outer():

    # 魔术方法：当把该类对象当作函数调用时自动触发
    def __call__(self,func):
        self.func = func    # 把传进来的函数作为对象的成员方法
        return self.inner   # 返回一个函数

    # 在定义的需要返回的新方法中，去进行装饰和处理
    def inner(self,who):
        print('1')
        self.func(who)
        print('2')


@Outer()    # Outer() ==> 实例化个对象 obj ==> obj(love) ==> __call__(love) ==> inner()
def love(who):
    print(f'{who}和妹子聊天')
love('恒')   # inner('恒')
print(love) # 此时的love就是属于Outer类这个对象中的inner方法
























































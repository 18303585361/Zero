# 用类方法装饰函数

class Outer():
    def __call__(self, func):
        pass
    def newinner(func):
        Outer.func = func   # 把传递进来的函数定义为类方法
        return Outer.inner  # 同时返回一个新的类方法
    def inner():
        print('拿到妹子微信')
        Outer.func()
        print('看一场电影')

@Outer.newinner # 调用Outer.newinner(love) 方法 ==> Outer.inner
def love():
    print('和妹子聊天')

love()  # love() ==> Outer.inner()

'''
到目前为止，以上所有形式的装饰器，包括函数装饰器、类装饰器、类方法装饰器，都有一个共同的特点：
    都是在给函数去进行装饰，增加功能
还有一种装饰器，是专门装饰类的。也就是在类的定义的前面使用 @装饰器 这种语法
'''






























































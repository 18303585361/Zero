# 带有参数的装饰器

# 如果你的装饰器需要有参数，那么给当前的装饰器套一个壳，用于接收装饰器的参数
def kuozhan(var):
    def outer(func):
        def inner1():
            print('妹子给微信')
            func()
        def inner2():
            print('妹子给你介绍个闺蜜')
            func()

        # 装饰器壳的参数，可以用于在函数内去做流程控制
        if var == '高富帅':
            return inner1
        else:
            return inner2
    return outer

@kuozhan('穷屌丝')
def love():
    print('找个妹子聊聊天')

love()
















































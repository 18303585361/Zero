# 对带有参数的函数进行装饰

# 定义装饰器
def outer(func):
    # 被装饰的函数有参数，则装饰器的内函数需要定义形参，并传递给调用的函数。
    # 因为调用被装饰的函数等于调用内函数
    def innner(var):
        print(f'找到{var}妹子，拿到微信')
        func(var)
        print(f'约{var}妹子，看电影')
    return innner

@outer
def love(name):
    print(f'跟{name}妹子聊天')

love('思思')  # love('思思') ==> inner('思思')



































































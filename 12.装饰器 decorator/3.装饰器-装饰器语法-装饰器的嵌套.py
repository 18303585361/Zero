# 装饰器的嵌套

# 1.普通装饰器的定义

# 定义装饰器
# 外函数
def outer(func):
    # 内函数
    def inner():
        print('找到妹子，拿到微信 3')
        func()  # 在内函数中调用外函数中的形参
        print('约妹子看电影 4')
    # 在外函数中返回内函数
    return inner

# @outer
# def love():
#     print('跟妹子聊天')
#
# love()  # 调用

# 2.装饰器嵌套

def kuozhan(f):
    def kzinner():
        print('扩展1')
        f()
        print('扩展2')
    return kzinner

@kuozhan
@outer
def love():
    print("跟妹子聊天 5")

love()

'''
1.先使用最近的 outer 装饰器，装饰 love 函数，返回了一个 inner
2.再使用 kuozhan 装饰器，装饰 上一次返回的 inner 函数，又返回了 kzinner 函数

最后在调用 love() 函数时的执行过程：
    love() ==> kzinner()
            ==> 扩展1
            ==> inner()
                ==> 3
                ==> love() ==> 5
                ==> 4
            ==> 扩展2
'''
























































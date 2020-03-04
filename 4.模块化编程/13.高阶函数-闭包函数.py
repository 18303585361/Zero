# 闭包函数

# 既然可以把函数作为一个形参进行传递作为回调函数，那么，如果在一个函数中，返回一个函数呢？
# 在一个函数内返回了一个内函数，并且这个返回的内函数还使用了外函数中的局部变量，这就是闭包函数。

# # 钱包
# money = 0
# # 工作
# def work():
#     global money
#     money += 100
# # 加班
# def overtime():
#     global money
#     money += 200
# # 购物
# def buy():
#     global money
#     money -= 50
# work()
# work()
# work()
# overtime()
# buy()
# # 银行垮台了，没钱了。。。
# money = 0
# work()
# print(money)

# 对程序进行改造

'''
闭包的特点
    1.在外函数中定义了局部变量，并且在内部函数中使用了局部变量
    2.在外函数中返回了内函数，返回的内函数就是闭包函数
    3.主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏

'''
# 定义一个函数
def person():
    money = 0   # 函数中定义了一个局部变量

    # 工作  定义的内函数
    def work():
        nonlocal money
        money += 100    # 在内函数中使用外函数的临时变量
        print(money)
    # 在外函数中返回了内函数，这个内函数就是闭包函数
    return work

res = person()  # return work    res = work
res()   # res() == work()
res()
# 此时    就不能在全局中对money这个局部变量进行任何操作了
# 闭包操作：保护了函数内的变量不受外部的影响，但是又能够不影响使用

## 如何检测一个函数是否为闭包函数
# 函数名.__closure__  如果是闭包函数返回 cell
print(person.__closure__)
print(res.__closure__)











































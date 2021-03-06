# yield 关键字
'''
yield 关键字使用在生成器函数中
    + yield 和函数中的 return 有点像
    + 共同点：执行到这个关键字后会把结果返回
    + 不同点：
        + return 会把结果返回，并结束当前函数的调用
        + yield 会返回结果，并记住当前代码执行的位置，下一次调用时，会从上一次离开的位置继续向下执行
'''
# 定义一个普通函数
# def hello():
#     print('hello 1')
#     return 1    # return 在函数中会把结果返回，并且结束当前的函数，后面的代码不再执行
#     print('world 2')
#     return 2
# hello()
# hello()

# 使用 yield 定义一个 生成器函数
# def hello():
#     print('hello 1')
#     yield 1    # return 在函数中会把结果返回，并且结束当前的函数，后面的代码不再执行
#     print('world 2')
#     yield 2
#     print('haha 3')
#     yield 3

# 调用生成器函数，返回一个迭代器
# res = hello()

# 使用生成器返回的迭代器
# r = next(res)
# print(r)
# r = next(res)
# print(r)

# 使用 list 函数去调用生成器返回的迭代器时，会把迭代器的返回结果，作为容器的元素
# r = list(res)
# print(r)

# 使用生成器返回的迭代器
# for i in res:
    # print(i)

'''
上面的生成器函数调用时的过程
首先，调用了生成器函数，返回了一个迭代器
1.第一次去调用迭代器：
    走到当前的生成器函数中，遇到了 yield 1，把 1 返回，并且记住了当前的执行状态（位置），暂停了执行，等待下一次的调用
2.第二次去调用迭代器：
    从上一次遇到的 yield 位置开始执行，遇到了 yield 2，把 2 返回，并记住状态，暂停执行，等待下一次的调用
3.第三次去调用迭代器
    从上一次遇到的 yield 位置开始执行，遇到了 yield 3，把 3 返回，并记住了状态，暂停执行，等待下一次调用
如果在最后又调用了迭代器，那么会从上一次的 yield 位置开始，结果后面没有了，直接就超出范围，报错。
'''



























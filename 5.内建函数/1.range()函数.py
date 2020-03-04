# 内置函数

'''
内置函数就是在系统安装完python解释器时，由python解释器给提供好的函数
'''

# range() 函数
'''
官网链接：https://docs.python.org/zh-cn/3/tutorial/controlflow.html#the-range-function
如果你确实需要遍历一个数字序列，内置函数 range() 会派上用场。它生成算术级数
功能：能够生成一个指定的数字序列
参数：
    start：开始的值  默认值为0
    stop：结束的值
    [，step]：可选，步进值  默认值为1
返回值：可迭代的对象，数字序列
'''
# res = range(10)
# 转为list列表
# print(list(res))

# 通过 for循环 进行遍历
# for i in res:
#     print(i)

# 转为迭代器，使用 next() 函数调用
# print(next(res))    # 不能直接用next()函数 TypeError: 'range' object is not an iterator
# res = iter(res)
# print(next(res))

# 只写一个参数，就是从 0 开始到10之前
# res = range(10)

# 两个参数时，第一个参数是开始的值，第二个参数是结束的值（在结束值之前）
# res = range(5,10)

# 三个参数时，参数1是开始值，参数2是结束值，参数3是步进值
# res = range(1,10,2)

# 获取一个倒序的数字序列
# res = range(10,0,-1)
# res = range(10,0,-3)

res = range(-10,-20,-1)
res = range(-20,-10)
res = range(-10,10)
print(list(res))
















































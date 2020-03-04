# filter() 过滤器函数

'''
filter(func,iterable)
    功能：
        把 iterable 中的每个元素拿到 func 进行处理
        如果函数返回 True 则保留，返回 False 则丢弃
    参数：
        func 自定义函数
        iterable： 可迭代的数据
    返回值：
        保留下来的数据组成的 迭代器
'''

# 要求 保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]

# 普通方法实现
# newlist = []
# for i in varlist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

# 使用 filter函数 实现
# 定义一个函数，判断当前这个函数是否为偶数
# def func(num):
#     if num % 2 == 0:
#         return num
# 调用 过滤器 函数进行处理
# res = filter(func,varlist)
# print(list(res))

# 优化版
# it = filter(lambda n : n if n % 2 == 0 else False,varlist)
# print(list(it))
































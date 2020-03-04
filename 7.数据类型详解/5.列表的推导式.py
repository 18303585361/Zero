# 列表的推导式

'''
推导式定义：
    采用一种表达式的方式，对数据进行过滤或处理，并且把结果组成一个新的列表
一、列表推导式的基本方式
    变量 = [变量或变量处理结果 for 变量 in 容器类型数据]
二、带有判断条件的列表推导式
    变量 = [变量或变量的处理结果 for 变量 in 容器类型数据 条件表达式]
三、带有条件判断的多循环推导式

'''
# 计算0—9的平方列表

    # 第一种方法：
    # varlist = []
    # for i in range(0,10):
    #     varlist.append(i ** 2)
    # print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 使用 map() 函数和list 完成
    # varlist = list(map(lambda x:x**2,range(0,10)))
    # print(varlist)

    # 使用列表推导式完成     下面这个列表推导式和第一种方式是一样的
    # varlist = [i**2 for i in range(10)]
    # print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# '1234' ==> [2,4,6,8]

    # 第一种方式：
    # varstr = '1234'
    # newlist = []
    # for i in varstr:
    #     newlist.append(int(i)*2)
    # print(newlist)

    # 使用列表推导式完成：
    # varstr = '1234'
    # newlist = [int(i)*2 for i in varstr]
    # print(newlist)

    # 使用 列表推导式 + 位运算 完成
    # varstr = '1234'
    # newlist = [int(i)<<1 for i in varstr]
    # print(newlist)

# 0—9 求所有的偶数
    # varstr = [i for i in range(10) if i%2==0]
    # print(varstr)

# [1,2,3]   [3,1,4]  ==> 把两个列表中的元素 两两组合，要求组合的元素不相同
    # 第一种办法
    # newlist = []
    # for x in [1,2,3]:
    #     for y in [3,1,4]:
    #         if x != y:
    #             newlist.append((x,y))
    # print(newlist)

    # 第二种办法
    # varlist = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
    # print(varlist)

'''
把下面的3x4的矩阵交换其行和列
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
'''
# 第一种办法
# arr = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# newlist = []
# for i in range(4):
#     res = []
#     for row in arr:
#         res.append(row[i])
#     newlist.append(res)
# print(newlist)

# 第二种办法 使用列表推导式完成
# newlist = [[row[i]for row in arr]for i in range(4)]
# print(newlist)

























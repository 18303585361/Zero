# 冰冻集合
'''
语法：
    定义冰冻集合，只能使用 frozenset() 函数进行冰冻集合的定义
    冰冻集合一旦定义，不能修改
    冰冻集合只能做集合相关的运算：求交集、差集、补集等
    frozenset() 本身就是一个强制转换类的函数，可以把其它任何容器类型的数据转为冰冻集合
'''
vars = frozenset({'love',666,1,2,3})
# vars = frozenset([1,2,3])

# 遍历
# for i in vars:
    # print(i)
# print(vars)

# 冰冻集合的推导式
# res = frozenset({i<<1 for i in range(6)})

# 冰冻集合可以和普通集合一样，进行集合的交集、差集
print(vars)
































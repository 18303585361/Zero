# 字典（映射类型）
'''
    字典也是一种数据的集合，由键值对组成的数据集合，字典中的键不能重复
    字典中的键必须时不可变的数据类型。
    常用的键主要有：字符串、整型。。。
字典的定义：
    1.通过将以逗号分隔的 键：值 对列表包含于花括号 {} 之内来创建
    2.通过 dict 构造器来创建
'''
# 使用 {} 来定义
# vardict = {'a':1,'b':2,'c':2}
# print(vardict)

# 使用 dict（key=value, key=value) 函数来定义
# vardict = dict(name='zhangsan',sex='男',age=22)

# 数据类型的转换   dict(二级容器类型) 列表或元组，并且是二级容器才能转换
# vardict  = dict([['a',1],['b',2]])
# print(vardict)

# zip压缩函数，dict转类型
# var1 = [1,2,3,4]
# var2 = ['a','b','c','d']
# vardict = dict(zip(var1,var2))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# print(vardict)

'''
字典的操作：
    1.不能用于加法 + 运算
    2.不能用于乘法 * 运算
    3.可以获取、删除、添加元素
    4.可以重复值，但是不能重复键
    5.成员检测,只能检测 key键，不能检测 value值
    6.获取当前字典的长度 len()，只能检测当前有多少个 键值对
    7.获取当前字典中的所有 key键、value值 及 键值对
    8.遍历字典操作
'''
var1 = {'a':1,'b':2,'c':3}
var2 = {1:'a',2:'b',3:'c',4:'d'}

# 获取元素
res = var1['a'] = 111

# 删除元素
# del var1['a']

# 添加元素
# var1['aa'] = 'AA'
# 如果字典中的 key 重复了,会被覆盖
# var1['aa'] = 'aa'

# 成员检测,只能检测 key键，不能检测 value值
# res = 'aa' in var1
# res = 'aa' not in var1

# 获取当前字典的长度 len()，只能检测当前有多少个 键值对
# print(len(var1))

# 获取当前字典中的所有 key键
# res = var1.keys()

# 获取当前字典中所有的 value值
# res = var1.values()

# 获取当前字典中所有的 键值对
# res = var1.items()

# 对字典进行遍历时
    # 在遍历当前字典时，只能获取当前的key
    # for i in var1:
    #     print(i)    # 只能获取 key
    #     print(var1[i])  # 通过字典的 key 获取对应的 value

    # 遍历字典时使用items() 函数，可以在遍历中获取 key 和 value
    # for k,v in var1.items():
    #     print(k)
    #     print(v)

# 遍历字典的所有 key
# for k in var1.keys():
#     print(k)

# 遍历字典所有的 value
# for v in var1.values():
#     print(v)



















































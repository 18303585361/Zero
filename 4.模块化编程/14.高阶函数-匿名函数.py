# 匿名函数 lambda 表达式

# 匿名函数的意思就是说可以不使用 def 定义，并且这个函数也没有名字
# 在python中可以使用 lambda 表达式来定义匿名函数
# 注意：lambda 表达式仅仅是一个表达式，不是一个代码块，所以 lambda 又称为一行代码的函数
# lambda 表达式也有形参，并且不能访问除了自己的形参之外的任何数据，包括全局变量

'''
语法：
    lambda [参数列表]：返回值
'''

# 封装一个函数，做加法运算
# 普通函数
# def jiafa(x,y):
#     return x+y
# print(jiafa(2,3))
#
# 改成 lambda 表达式来封装
# res = lambda x,y:x+y
# print(res(4,5))

# lambda 是一个表达式，因为不能写太复杂的逻辑，功能相对单一
# lambda 是否可以使用分支结构

def func(sex):
    if sex == "男":
        return '很man'
    else:
        return '人妖？'
print(func('男'))

# 带有分支结构的 lambda 表达式
# lambda 参数列表：真区间 if 表达式判断 else 假区间
res = lambda sex:"很man" if sex == "男" else "人妖？"
print(res('1'))














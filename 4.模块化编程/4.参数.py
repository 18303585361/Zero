# 普通参数，默认参数，收集参数 *args，命名关键字参数，

# 命名关键字参数
'''
1.关键字参数定义在 收集参数 后面
2.关键字参数必须通过 形参的名字 传递
'''
# def func(a, b, c=3, *args, name):
#     print(a, b, c, *args)
#     print(args)
#     print(name)

# 在调用时，必须按照形参的名字进行参数的传递
# func(1,2,3,4,5,6,7,8,9,name="admin")

# 普通函数
def love(name):
    print(name)
love('abc')
# 在调用普通函数时，需要按照顺序进行参数的传递
# 也可以把普通函数的普通参数按照关键字参数进行传递
love(name="abc")



























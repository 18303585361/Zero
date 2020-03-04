# reduce() 函数

'''
reduce()
    功能：
        每一次从 iterable 中拿出两个元素，放入到 func函数 中进行处理，得出一个计算结果
        然后把计算结果和 iterable 中的第三个元素放入 func函数 中继续运算，
        得出的结果和之后的第四个元素继续运算直到最后一个元素。
    参数：
        func：内置函数或自定义函数
        iterable：可迭代的数据
    返回值：
        最终的运算处理结果
    注意：
        使用 reduce()函数 时需要导入
        from functools import reduce
'''

from functools import reduce
# (1) [5,2,1,1] ==> 5211

# 普通方法：
# varlist = [5,2,1,1]
# res = ''
# for i in varlist:
#     res += str(i)
# res = int(res)
# print(res,type(res))

# 使用 reduce() 函数
'''
5   2   1   1
5 * 10 + 2 == 52
52 * 10 + 1 == 521
521 * 10 + 1 == 5211
'''
# varlist = [5,2,1,1]
# # def myfunc(x,y):
# #     return x*10 + y
# # # 调用函数
# # res = reduce(myfunc,varlist)
# # print(res,type(res))

# （2） 把字符串的 '456' ==> 456
# 要求不能使用int方法进行类型转换时，如何解决上面的问题？

# 普通方法：
# a = '456'
# b = int(a)
# print(b)

# 定义函数，给定一个字符串的数字，返回一个整型的数字
def myfunc(s):
    vardict = {'0': 0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return vardict[s]

# 1.先使用 map()函数，把数字字符串转为整型的数字
iter1 = map(myfunc,'456')
# 2.把数字列表中的值，使用 lambda 进行二次处理
iter2 = reduce(lambda x,y:x*10 + y,iter1)
print(iter2)



































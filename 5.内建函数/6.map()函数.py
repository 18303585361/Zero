# map() 函数
'''
map(func,*iterables)
    功能：对传入的可迭代数据中的每一个元素进行处理，返回一个新的迭代器
    参数：
        func 函数    自定义函数|内置函数
        iterables：  可迭代的数据
    返回值：
'''
'''
把一个字符串数字的列表转为 整型的数字列表
普通的处理方法
varlist = ['1','2','3','4']     # ==>[1,2,3,4]
newlist = []
for i in varlist:
    newlist.append(int(i))
print(newlist)

使用map函数进行处理
varlist = ['1','2','3','4']
res = map(int,varlist)  # <map object at 0x0000000002665B80>
print(list(res))
'''

'''
[1,2,3,4] ==> [1,4,9,16]
arr = [1,2,3,4]
def func(num):
    return num ** 2
res = map(func,arr)
print(list(res))

arr = [1,2,3,4]
res = map(lambda x:x**2,arr)
print(list(res))
'''

# 练习作业：['a','b','c','d'] ==> [65,66,67,68]

list1 = ['a','b','c','d']
list2 = []
for i in list1:
    i.upper()
    res1 = ord(i)
    list2.append(i)
# def func(num):
    # 第一步：list1中每一个小写字母变大写
    # 第二步：通过 ord 函数 进行转换
print(list2)

# res = map(func,list1)
# print(list(res))















































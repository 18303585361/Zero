# sorted() 函数

'''
sorted(iterable,[reverse,key])
    运行原理：
        把可迭代数据里面的元素一个一个的取出来，放到 key 函数中进行处理，
        并按照函数中return（返回）的结果进行排序，返回一个新的列表。
    功能：排序
    参数：
        iterable    可迭代的数据/对象（容器类型数据、range数字序列、迭代器）
        reverse     可选，是否反转，默认值为 False（不反转）
        key         可选，函数类型，可以是自定义函数，也可以是内置函数
    返回值：排序后的结果
'''

# arr = [3,7,1,-9,20,100]
# 默认可以按照从小到大的方式进行排序
# res = sorted(arr)

# 可以按照从大到小的方式进行排序
# res = sorted(arr,reverse=True)  # [100, 20, 7, 3, 1, -9]

# 使用 abs()函数（求绝对值），作为 sorted 的 key关键字 参数使用
# res = sorted(arr,key=abs)   # [1, 3, 7, -9, 20, 100]
# print(res)

# 使用自定义函数
# def func(num):
#     return num % 6
#
# arr = [1,8,2,4,5,6,3,7,9]
#
# 在sorted函数中使用自定义函数
# res = sorted(arr,key=func)  # [6, 1, 7, 8, 2, 3, 9, 4, 5]
# print(res)

# arr = [1,8,2,4,5,6,3,7,9]
#
# res = sorted(arr,key=lambda x:x%6)  # [6, 1, 7, 8, 2, 3, 9, 4, 5]
# print(res)









































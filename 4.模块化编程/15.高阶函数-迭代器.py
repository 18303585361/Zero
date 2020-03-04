# 迭代器

'''
迭代器是python中最具特色的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住访问遍历的位置的对象
从集合的第一个元素开始访问，直到集合中的所有元素被访问完毕
迭代器只能从前往后一个一个的遍历，不能后退
能被 next()函数调用，并不断返回下一个值的对象称为迭代器(iterator  迭代器对象)
'''

# range(10,3,-1)  10--4   返回一个可迭代的对象

# arr = ['a','b','c',4,5]
# for i in arr:
#     print(i)


'''
iter() 
    功能：把可迭代的对象，转为一个迭代器对象
    参数：可迭代的对象   （str, list, tuple, dict, set, range...)
    返回值：迭代器对象   
注意：迭代器一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器。
'''
# 定义一个列表，是一个可迭代的对象
f4 = ['赵四','刘能','小沈阳','海参炒面']
# 可以使用for循环来遍历数据

# 可以把可迭代对象转为迭代器使用
res = iter(f4)
# print(res,type(res))    # <list_iterator object at 0x0000000002615880> <class 'list_iterator'>
'''
迭代器取值的特点，取出一个少一个，直到都取完，最后再获取就会报错。
迭代器取值的方案
    1.  next() 调用一次获取一次，直到数据被取完
    2.  list() 使用list函数直接取出迭代器中的所有数据
    3.  for     使用for循环遍历迭代器的数据
'''
# 使用 next() 函数去调用迭代器对象
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))    # 超出可迭代的范围 StopIteration
# r = list(res)
# print(r)

# 检测迭代器和可迭代对象的方法

from collections.abc import Iterator,Iterable

varstr = '123456'
res = iter(varstr)

# type()  函数返回当前数据的类型
# isinstance()  检测一个数据是不是一个指定的类型
r = isinstance(varstr,str)  # True 是一个字符串类型
print(r)
r = isinstance(varstr,int)  # False 不是一个迭代器
print(r)
r = isinstance(varstr,Iterable) # True 可迭代对象
print(r)
r = isinstance(varstr,Iterator) # True 是一个迭代器
print(r)

# 迭代器一定是一个可迭代的对象，可迭代对象不一定是迭代器

# next(varstr)  # TypeError: 'str' object is not an iterator




























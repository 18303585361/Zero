# 列表

'''
定义：
    列表就是一组有序的数据组合，列表中的数据可以被修改
    可以使用 中括号[] 或 list函数 定义
    在定义列表中的元素时，需要在每个元素之间使用逗号，进行分割
    列表中的元素可以是任意类型，通常用于存放同类项目的集合
基本操作：
    列表的定义
    列表的相加-拼接
    列表的相乘-重复
    列表的下标-获取、更新
    列表的元素的添加-append()
    列表元素的删除：
        del 列表名[下标]
        pop()函数 删除最后一个元素
切片：

列表相关函数：

列表推导式：
    x for x in iterable
'''
# varlist1 = [1,2,3,4]
# varlist2 = ['a','b','c','d']

# 列表的拼接。把多个列表的元素拼接成一个列表
# res = varlist1 + varlist2
# 列表元素的重复
# res = varlist1 * 3
# res = varlist1 * ['aa','bb']    # TypeError: can't multiply sequence by non-int of type 'list'
# 检测元素是否存在于列表中
# res = 'a' in varlist2
# 列表的索引操作
'''
 0   1   2   3
'a','b','c','d'
-4  -3  -2  -1
'''
## 通过下标获取指定的元素
# res = varlist2[2]
# res = varlist2[-3]
## 可以通过下标修改元素，不能通过下标添加元素
# res = varlist2[2] = 'cc'
# varlist2[4] = 'ff'  # IndexError: list assignment index out of range
## 向列表中追加元素
# varlist2.append('ff')
## 列表元素的删除
# del varlist2[2]
# res = varlist2.pop()    # pop方法，弹出最后一个元素
# 获取列表的长度 len()
# res = len(varlist2)
# print(varlist2)














































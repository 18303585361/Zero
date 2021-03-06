# 元组

'''
元组：
    元组和列表一样，都是一组有序的数据的组合。
    元组中的元素一旦定义，不可修改。因此元组称为不可变数据类型。
定义：
    空元组     变量 = () 或者  变量=tuple()
    有数据元组   变量 = (1,2,3)
    如果元组中只有一个元素，必须加逗号  变量 = (1，)
    其他定义方式    变量 = 1,2,3
操作：
    由于元组时不可变的数据类型，因此只能使用索引进行访问，不能进行其它操作
    元组可以和列表一样使用切片方式获取元素
切片：

'''
# 注意，定义元组时，如果只有一个元素，也需要使用 逗号
# vart = 1,2,3
# vart = 1,
# print(vart,type(vart))


# 元组的切片操作   和列表一样
# vart = (1,2,3,4,5,5,4,3,2,1)
# res = vart[:]   # 获取全部
# res = vart[::]  # 获取全部
# res = vart[1:3] # 从索引1开始到索引3之前
# res = vart[1:5:1]   # 从索引1开始到索引5之前，步进值为1
# res = vart[1:5:2]   # 从索引1开始到索引5之前，步进值为2
# res = vart[:3]  # 从索引0开始到索引3之前
# res = vart[5:1:-1]  # 从索引5开始索引1，步进值为-1  倒着输出

# 获取元组的长度 len()
# print(len(vart))

# 统计一个元素在元组中出现的次数   count()
# res = vart.count(5)

# vart = ('张学友','吴恩达','柳岩','吴恩达')
# 获取一个元素在元组的索引值
# res = vart.index('吴恩达')
# res = vart.index('吴恩达',2)   # 从指定下标位置开始查找
# res = vart.index('吴恩达',2,5) # 从指定的 索引区间内 查找
# print(res)

# 元组的 + 运算，也就是合并元组，组成新的元组
# res = (1,2,3) + ('a','b')   # (1, 2, 3, 'a', 'b')

# 元组的 * 运算，也就是合并元组，组成新的元组
res = (1,2,3) * 3   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 检测一个元素是否在元组中
# res = 2 in res
# res = 2 not in res
# print(res)













































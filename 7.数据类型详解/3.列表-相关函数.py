# 列表相关函数

# varlist = ['刘德华','张学友','张国荣','刘德华','黎明','郭富城','刘能','宋小宝','赵四']

# len() 检测当前列表的长度，列表中元素的个数
# res = len(varlist)

# count()   检测当前列表中某个元素出现的个数
# res = varlist.count('刘德华')

# append()  向列表的尾部追加新的元素，返回值为 None
# res = varlist.append('川哥')

# insert(self,index,object) 向列表中指定的索引位置添加新的元素
#                           可以超出列表元素位置去追加
# varlist.insert(1,'aa')  #   ['刘德华', 'aa', '张学友', '张国荣', '刘德华', '黎明', '郭富城', '刘能', '宋小宝', '赵四']

# pop() 可以对指定索引位置上的元素做 出栈 操作，返回 出栈的元素
# res = varlist.pop(5) # 默认会把列表中的最后一个元素 出栈

# remove()  可以指定列表中的元素进行 删除，只删除第一个。如果没有找到则报错
# varlist = [1,2,3,4,11,22,33,44,1,2,3,4]
# res = varlist.remove(1)

# index()   可以查找指定元素在列表中第一次出现的位置
# res = varlist.index(1)
# res = varlist.index(1,5,10) # 可以在指定索引范围内查找元素的索引位置

# extend()  接收一个容器类型的数据，把容器中的元素追加到原列表中
# res = varlist.extend(['a','b','c'])

# clear()   清空列表内容
# res = varlist.clear()

# reverse() 列表翻转    没有返回值
# varlist.reverse()

# sort()    对列表进行排序     没有返回值
# res = varlist.sort()  # 默认对元素进行从小到大的排序
# res = varlist.sort(reverse=True)  # 对元素进行从大到小的排序
# res = varlist.sort(key=abs) # 可以传递一个函数，按照函数的处理结果进行排序

# copy()    拷贝，复制当前的列表
# res = varlist.copy()
# print(res)
# print(varlist)

# 对 copy 后的列表进行操作
# del res[4]
# 定义 多维列表
# varlist = ['a','b','c',[1,2,3]]
# res = varlist.copy()
# 对 copy 的列表进行一个操作
# del res[1]    # 对一维列表进行操作，没有问题
# del res[3][1]   # 对多维列表中的元素，进行操作，则出现了全部改变的情况
# print(res)
# print(varlist)
































































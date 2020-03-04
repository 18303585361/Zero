# 集合 set()：确定的一组无序的数据集合

'''
定义：
    可以直接使用 {} 来定义集合
    可以使用 set() 进行集合的定义和转换
    使用 集合推导式 完成集合的定义
    注意：
        集合中的元素不能重复
        集合中存放的数据：number Strings Tuple 冰冻集合
特点：
    1.当前集合中元素的值不能重复
    2.可以由多个数据组合的复合型数据
    3.集合中的数据没有顺序
功能：
    成员检测
    从序列中去除重复项
    数学中集合类的计算，例如交集、并集、差集与对称差集等
操作和常规函数：
    1.检测元素是否在集合中 in  not in
    2.获取集合中元素的个数 len()
    3.集合的遍历
    4.给集合追加元素 set.add()
    5.删除集合中的元素
        set.pop()方法   是随机删除一个元素并返回
        set.remove()    返回None，删除的元素不存在则报错
        set.discard()  删除的元素不存在也不会报错
        set.clear()     清空集合
    6.更新集合  set.update(*other)  添加*other的全部元素
    7.浅拷贝   set.copy()
        当前集合中的浅拷贝.并不存在 深拷贝 的问题
        因为集合中的元素都是不可变的，包括元组和冰冻集合
        不存在拷贝后，对集合中不可变的二级容器进行操作的问题
冰冻集合：
    例：v = frozenset((1,2,3))
'''
# vars = {123,'abc','love',True,(1,2,3),0,False,3.1415,123,'123'}
# 1.无序
# 2.布尔类型 True 表示为 1，False 表示为 0.布尔和数字只存在一个
# 3.元素的值不能重复
# ==> {0, True, 3.1415, (1, 2, 3), 'love', 'abc', 123}

# 检测集合中的值
# res = '123'in vars

# 获取集合中元素的个数
# res = len(vars)

# 集合的遍历
# for i in vars:
#     print(i)

# 向列表中追加元素  set.add()
# res = vars.add('def')

# 删除集合中的元素  set.pop()方法是随机删除一个元素并返回
# res = vars.pop()
# res = vars.pop()

# 指定删除元素 set.remove()   返回None，删除的元素不存在则报错
# res = vars.remove('love')

# 指定删除元素 set.discard()  删除的元素不存在也不会报错
# res = vars.discard('aaa')

# clear() 清空集合
# res = vars.clear()

# update(*other)  更新集合。添加*other的全部元素
# res = vars.update({1,2,3,4,5})

# 当前集合中的浅拷贝.并不存在 深拷贝 的问题
# res = vars.copy()
'''
当前集合中的浅拷贝.并不存在 深拷贝 的问题
    因为集合中的元素都是不可变的，包括元组和冰冻集合
    不存在拷贝后，对集合中不可变的二级容器进行操作的问题
'''
# print(res)
# print(vars)










































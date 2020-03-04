# 集合运算

'''
集合的主要运算
    交集  &   set.intersection()  set.intersection_update()
    并集  |   把集合中所有元素全部集中起来，去除重复的值   set.union()     set.update()
    差集  -   set.difference()    set.difference_update()
    对称差集  ^     set.symmetric_difference()  set.symmetric_difference_update()
    超集  set1.issuperset(set2)
    子集  set1.issubset(set2)
    检测是否不相交 set1.isdisjoint(set2)
注意：
    凡是带 update 的函数全部是生成新的运算结果赋值给第一个集合

'''
# vars1 = {'郭富城','刘德华','张学友','黎明','都敏俊',1}
# vars2 = {'尼古拉斯赵四','刘能','小沈阳','宋小宝','都敏俊',1}

# 求两个集合相交的部分
# res = vars1 & vars2

# 交集运算函数
# vars1.intersection()  返回交集的结果 是一个新的集合
# res = vars1.intersection(vars2)
# vars1.intersection_update()   没有返回值，计算两个集合的相交部分，把计算结果重新赋值给第一个集合
# res = vars1.intersection_update(vars2)

# 求两个集合的并集
# res = vars1 | vars2

# 并集运算函数    set.union():返回并集结果，新的集合     set.update()：求并集运算，把运算结果赋值给第一个集合
# res = vars1.union(vars2)
# res = vars1.update(vars2)

# 求差集运算
# res = vars1 - vars2     # vars1有，vars2没有的。    {'郭富城', '黎明', '张学友', '刘德华'}
# res = vars2 - vars1     # vars2有，vars1没有的。    {'刘能', '小沈阳', '尼古拉斯赵四', '宋小宝'}

# 求差集运算的函数
# res = vars1.difference(vars2)   # 返回差集结果，新的集合
# res = vars2.difference_update(vars2)    # 求差集运算，把运算结果赋值给第一个集合

# 求对称差集
# res = vars1 ^ vars2     # {'张学友', '郭富城', '刘能', '刘德华', '黎明', '小沈阳', '宋小宝', '尼古拉斯赵四'}

# 求对称差集的函数
# vars1.symmetric_difference(vars2)     # 返回对称差集的结果
# vars1.symmetric_difference_update(vars2)  # 把对称差集的运算结果赋值给第一个集合

# 检测 超集 子集
# vars1 = {1,2,3,4,5,6,7,8,9}
# vars2 = {1,2,3}

# issuperset() 检测是否是超集
# res = vars1.issuperset(vars2)   # True vars1是vars2的超集
# res = vars2.issuperset(vars1)   # False vars2不是vars1的超集

# issubset() 检测是否为子集
# res = vars1.issubset(vars2) # False
# res = vars2.issubset(vars1) # True    vars2是vars1的子集

#　检测两个集合是否不相交   不相交返回True，相交返回False
# res = vars1.isdisjoint(vars2)
# print(res)




































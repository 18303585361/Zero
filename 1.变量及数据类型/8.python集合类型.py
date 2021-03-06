# set集合类型

'''
+ set集合是一个无序且元素不重复的 集合的数据类型
+ set集合使用 大括号{} 或者set() 方法来定义
'''

# 集合的定义方式
# vars = {1,2,3,4,5,'a','b',1}
# vars = set('23')
# 如果需要定义一个空集合时，只能使用 set() 方法，因为大括号使定义的空字典
# vars = {}
# vars = set()
# print(vars,type(vars))

# a = {1,2,3,'a'}
# 给集合添加元素
# a.add('b')
# 无法获取集合中的单个元素，但是可以添加和删除
# a.discard('b')
# print(a)
# 检查当前的元素是否在集合中
# print('a' in a)

# 集合主要用于运算：交集，差集，并集，对称集合等。
a = {1,2,3,'a','b'}
b = {1,'a',22,33}
print(a & b) # 交集 {1, 'a'}
print(a - b) # 差集 {'b', 2, 3},a集合有，b集合没有
print(a | b) # 并集 {1, 2, 3, 33, 'a', 'b', 22}，两个集合放到一起，并且去重
print(a ^ b) # 对称集合 {33, 2, 3, 22, 'b'}，把两个集合中不重复的内容拿出来形成一个新的集合















































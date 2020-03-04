# python 的数据类型

# 什么是数据类型？
# 数据类型就是数据的表现形式，比如：你好 就是一个字符串，200 就是一个数字。
# 在程序当中，除了这种常用的字符和数字外，还有很多其它的数据表现形式。

# 常用的数据类型
# 1.字符串类型
love = 'iloveyou'
hello = '你好 世界'
like = "i like you"

# 大字符串，可以换行写
s = '''
比如说，这是一个很长很长的文章内容
'''
# 在python中提供了一个方法，用于获取当前变量的数据类型
# type()函数，专门返回一个变量的数据类型结果
# res = type(s) # <class 'str'>  str == string
# print(love, type(love), hello, type(hello),like, type(like))
# print(s, res)

# 使用引号定义的字符串可以嵌套别的引号
# 单双引号可以互相嵌套，但是不能嵌套自己
# s = 'i "love" you'
# print(s)

# s = '''
# 床前明月光
# 疑似'地上'霜
# 举头"""望明"""月
# 低头"思故"乡
# '''
# print(s)

# 关于转义字符 \n 表示换行    \t  表示一个制表符

s = '床前\n明月光'
s1 = r'床前\n明月光' # 可以取消转义字符
print(s)
print(s1)

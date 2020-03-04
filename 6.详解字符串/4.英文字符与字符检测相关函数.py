# 英文字符与字符检测相关函数

varstr = 'i 我 Love 喜欢 you 你'

# 一、大小写转换函数
# 1. str.capitalize() 返回原字符串的副本，其首个字符大写，其余小写。
# res = varstr.capitalize()
# 2. str.title() 返回原字符串的副本，把字符串中的每个单词首字母大写，其余小写。
# res = varstr.title()
# 3. str.upper() 把字符串中的英文字符全部转为  大写
# res = varstr.upper()
# 4. str.lower() 把字符串中的英文字符全部转为  小写
# res = varstr.lower()
# 5. str.swapcase() 返回原字符串的副本，其中大写字符转换为小写，反之亦然
# res = varstr.swapcase()
# print(res)

# 二、字符检测方法( is 开头的全部是检测方法）
# 1. str.isupper() 检测当前的字符串的英文字符是否全部由大写字符组成
# res = varstr.isupper()
# 2. str.islower() 检测当前的字符串的英文字符是否全部由小写字符组成
# res = varstr.islower()
# 3. str.istitle()  检测当前的字符串的英文字符是否符合 title标题 的要求
#                   即：每个单词的首字母是否大写
# res = varstr.istitle()
# 4. str.isalpha()  检测当前的字符串是否由字符（中文、英文字符）组成
#                   即：如果字符串中包含 数字、空格等 返回 False
# res = varstr.isalpha()
# 5. str.isalnum()  检测当前的字符串是否由字符（中文、英文字符、数字）组成
#                   即：如果包含 空格等 返回 False
# res = varstr.isalnum()
# 6. str.isdigit()  检测当前的字符串是否由数字字符组成，有其它字符返回 False
# res = varstr.isdigit()
# 7. str.isspace()  检测当前的字符串是否全部由 空格字符 组成
# res = varstr.isspace()
# 8. str.startswith()   检测一个字符串是否由指定的字符开头
#    str.startswith('',1)   也可以指定开始的位置。
# res = varstr.startswith('i')
# res = varstr.startswith('l',1)
# 9. str.endswith('',1) 检测一个字符串是否由指定的字符结尾
#                       也可以指定开始和结束的位置
# res = varstr.endswith('you')
# res = varstr.endswith('you',0,5)
# print(res)






















































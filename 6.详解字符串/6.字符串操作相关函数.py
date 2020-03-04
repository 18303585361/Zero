# 字符串操作相关函数

'''
1. str,split()  从左往右 可以按照指定的字符进行分割，把一个字符串分割成一个列表
'''
# vars = 'user_admin_id_123'
# res = vars.split('_')   # ['user', 'admin', 'id', '123']
# print(res)
# res = vars.split('_',2)     # ['user', 'admin', 'id_123']
# print(res)

# vars = 'uid=123&type=ab&kw=hh'
# res = vars.split('&')
# for i in res:
#     r = i.split('=')
#     print(r.pop())

'''
2. str.rsplit() 从右往左 可以按照指定的字符进行分割，把一个字符串分割成一个列表     
'''
# res = vars.rsplit('_',2)    # ['user_admin', 'id', '123']
# print(res)

'''
3. str.join()   按照指定的字符，把容器类型中的数据连接成一个字符串
'''
# arr = ['user','admin','id','123']
# res = '@'.join(arr) #   user@admin@id@123
# print(res)

'''
4. str.strip()  可以去除字符串左右两侧的指定字符
5. str.lstrip() 去除字符串左侧的指定字符
6. str.rstrip() 去除字符串右侧的指定字符
'''
# vars = '   这是一个文章的标题    '
# res = vars.strip(' ')
# print(res)

'''
7. str.replace(old,new,[,count])    可以做替换用,可以全部替换也可以指定替换几个
'''
# vars = 'iloveyoutosimidailoveyou'
# res = vars.replace('love','like',1)
# print(res)

'''
8. str.center()     可以按照指定字符 补齐字符
'''
# vars = 'love'
# res = vars.center(10,'*')
# print(res)

'''
9. str.ljust()  在字符串的右侧按照指定字符补齐
10. str.rjust() 在字符串的左侧按照指定字符补齐
'''
# vars = 'love'
# res = vars.ljust(10,'*')
# res = vars.rjust(10,'*')
# print(res)






































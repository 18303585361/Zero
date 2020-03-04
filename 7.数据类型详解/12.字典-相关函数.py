# 字典的相关函数

'''
1.  len() 获取字典的键值对个数
2.  dict.keys()   获取当前字典的所有 key键 组成的列表
3.  dict.values() 获取当前字典的所有 value值 组成的列表
4.  dict.items()  返回由字典(键值对)组成的一个新视图
5.  iter(dict)    返回以字典的键为元素的迭代器
6.  dict.pop()    通过 key键 从当前字典中弹出（删除）键值对
7.  dict.popitem()    把最后加入到字典中的 键值对 删除并返回一个元组
8.  dict.get()    使用 key键 获取字典中不存在的元素会报错
                  使用 get 获取，存在则返回，不存在则默认返回None
9.  dict.update(key=value)  更新字典.如果 key 存在则更新，不存在则添加
10. dict.setdefault(key,[,default])     如果字典存在 key键，返回它的值
                                        如果不存在，插入值为 default 的 key键，并返回default值
11. dict.clear()    清空字典
'''
# vardict = {'a':1,'b':2,'c':2}
# res = iter(vardict)
# res = vardict.pop('a')
# res = vardict.popitem()
# res = vardict.get('b')
# vardict.update(a=11,b=22)
# res = vardict.setdefault('a')
# res = vardict.setdefault('aa')
# res = vardict.setdefault('aa','123')
# print(vardict)





















































# 字典推导式

'''
把字典中的 键值对 位置进行交换：{'a':1,'b':2,'c':3}
vardict = {'a':1,'b':2,'c':3}
一、普通方法
newdict = {}
for k,v in vardict.items():
    k,v = v,k
    newdict[k] = v
print(newdict)

二、推导式完成
newdict = {v:k for k,v in vardict.items()}
print(newdict)

三、注意：以下推导式，返回的结果是一个集合，集合推导式
newdict = {v for k,v in vardict.items()}
print(newdict,type(newdict))
'''

# 把以下字典中的是偶数的值保留下来并且交换键值对位置
vardict = {'a':1,'b':2,'c':3}
# newdict = {}
# for k,v in vardict.items():
#     if v%2 == 0:
#         newdict[v] = k
# print(newdict)

# 字典推导式完成
newdict = {v:k for k,v in vardict.items() if v % 2 == 0}
print(newdict)

















































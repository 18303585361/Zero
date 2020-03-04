# 集合推导式

'''
1.普通推导式
2.带有条件表达式的推导式
3.带有多循环的集合推导式
4.带条件判断表达式的多循环集合推导式
'''
# varset = {1,2,3,4}
# newset = {i<<1 for i in varset}
# newset = {i<<1 for i in varset if i%2 == 0}
# vars1 = {1,2,3}
# vars2 = {4,5,6}
# newset = set()
# for i in vars1:
#     for j in vars2:
#         print(i,j)
#         newset.add(i+j)
# print(newset)

# newset = {i+j for i in vars1 for j in vars2 if i%2==0 and j%2==0}
# print(newset)







































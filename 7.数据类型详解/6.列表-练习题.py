# 练习题
'''
列表推导式完成九九乘法表
1*1 = 1
2*1 = 2 2*2 = 4
3*1 = 3 3*2 = 6 3*3 = 9
......
9*1 = 9 9*2 = 18 9*3 = 27 9*4 = 36......
'''
# 普通方法
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f'{x}*{y} = {x*y}',end=" ")
#     print()

# 列表推导式
# newlist = [[f'{x}*{y} = {x*y}' for y in range(1,x+1)]for x in range(1,10)]
# for i in range(10):
#     print(newlist[i])
'''
练习题1.使用列表推导式完成
{'user':'admin','age':20,'phone':'133'}
==> ['user=admin','age=20','phone=133']
==> user=admin&age=20&phone=133
'''
# 第一种方法：
# dict1 = {'user':'admin','age':20,'phone':'133'}
# newlist = []
# for i in dict1:
#     res = i + '=' + str(dict1[i])
#     newlist.append(res)
# print(newlist)

# 代码优化：
# dict1 = {'user':'admin','age':20,'phone':'133'}
# newlist = []
# for k,v in dict1.items():
#     res = k + '=' + str(v)
#     newlist.append(res)
# print(newlist)

# 使用列表推导式完成
# newlist = [i+'='+str(dict1[i]) for i in dict1]
# print(newlist)
'''
练习题2：用列表推导式完成 把列表中的所有字符全部转为小写
['AAAAA','bbBb','CCCcc'] ==> ['aaaaa','bbbb','ccccc']
'''
# 普通方法
# lista = ['AAAAA','bbBb','CCCcc']
# listb = []
# for i in lista:
#     res = i.lower()
#     listb.append(res)
# print(listb)

# 使用列表推导式完成
# newlist = [i.lower() for i in lista]
# print(newlist)
'''
练习题3：   x 是0—5之间的偶数，y 是0-5之间的奇数
            把 x,y 组成一个元组，放到列表中
'''
# 普通方法
# newlist = []
# for x in range(0,6):
#     for y in range(0,6):
#         if x%2 == 0 and y%2 == 1:
#             newlist.append((x,y))
# print(newlist)

# 列表推导式
# newlist = [(x,y) for x in range(6) for y in range(6) if x%2 == 0 and y %2 == 1]
# print(newlist)
'''
练习题4： 求M,N中矩阵和元素的乘积
M=[
[1,2,3],
[4,5,6],
[7,8,9]
]
N=[
[2,2,2],
[3,3,3],
[4,4,4]
]
实现乘积的结果
(1) ==> [2,4,6,12,15,18,28,32,36]
(2) ==> [[2,4,6],[12,15,18],[28,32,36]]
'''
# (2)普通方法
# M=[[1,2,3],[4,5,6],[7,8,9]]
# N=[[2,2,2],[3,3,3],[4,4,4]]
# endlist = []
# for i in range(3):
#     newlist = []
#     for j in range(3):
#         res = M[i][j] * N[i][j]
#         newlist.append(res)
#     endlist.append(newlist)
# print(newlist)
# print(endlist)      # [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

# (1)普通方法
# M=[[1,2,3],[4,5,6],[7,8,9]]
# N=[[2,2,2],[3,3,3],[4,4,4]]
# endlist = []
# for i in range(3):
#     for j in range(3):
#         res = M[i][j] * N[i][j]
#         endlist.append(res)
# print(endlist)      # [2, 4, 6, 12, 15, 18, 28, 32, 36]
# 列表推导式求矩阵乘积
# newlist = [M[i][j] * N[i][j] for i in range(3) for j in range(3)]
# print(newlist)
































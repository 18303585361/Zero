# 函数封装的练习题

# 打印九九乘法表，矩形，十二生肖。。

# 定义函数：打印九九乘法表

# def jiujiu(n=0):
#     '''
#     当前函数的功能就是 打印九九乘法表
#     n：控制 正向输出 和 反向输出  九九乘法表，0为正向 默认，1为反向
#     '''
#     if n == 0:
#         rs = range(1,10)
#     else:
#         rs = range(9,0,-1)
#     for x in rs:
#         for y in range(1,x+1):
#             print(f'{x}x{y}={x*y}',end=" ")
#         print()
#
# jiujiu(1)

# 封装打印矩形的函数
def juxing():
    for x in range(0,100):
        if x <10 or x>=90:
            print('#', end=" ")
        elif x>=10 and x<90:
            if x % 10 == 0 or x % 10 == 9:
                print('#', end=" ")
            else:
                print(end="  ")
        if x % 10 == 9:
            print()
juxing()

'''
# # # # # # # # # # 
#                 #  
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
# # # # # # # # # # 
'''





















































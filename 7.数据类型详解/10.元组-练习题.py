# 练习题：使用 生成器 改写 斐波那契数列函数
'''
斐波那契数列：
1,1,2,3,5,8,13......
0,1,2,3,4,5,6,......
a,b,
1.第一次调用返回 1
2.第二次调用返回 1
3.第三次调用返回 2
4.第四次调用返回 3
.......
'''
# 斐波那契数列
# def fibo(num):
#     a,b,i = 0,1,0
#     while i < num:
#         print(b,end=',')
#         a,b = b,a+b
#         i += 1
# fibo(6)

# 使用 生成器函数 改写 斐波那契数列
# def fibo(num):
#     a,b,i = 0,1,0
#     while i < num:
#         yield b
#         a,b = b,a+b
#         i += 1
# res = fibo(10)
# print(res)
# print(list(res))

# num = int(input('请输入一个正整数'))
# for i in fibo(num):
#     print(i,end=',')
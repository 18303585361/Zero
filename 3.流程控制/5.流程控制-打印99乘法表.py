# 99乘法表
'''
9行
1 1x1=1
2 2x1=2 2x2=4
3 3=1=3 3x2=6 3x3=9
4 ...
9 9x1=9 9x2=19 ... 9x9=81
'''
# 第一层循环控制 9行
# for x in range(1,10):
#     # 第二层循环，内循环
#     # 内循环负责当前行的列数，第一行 1列；二行 2列。。。九行 9列
#     for y in range(1,x+1):
#         print(f'{x}x{y}={x*y}', end=" ")
#     # 控制换行
#     print()
'''
1x1=1 
2x1=2 2x2=4 
3x1=3 3x2=6 3x3=9 
4x1=4 4x2=8 4x3=12 4x4=16 
5x1=5 5x2=10 5x3=15 5x4=20 5x5=25 
6x1=6 6x2=12 6x3=18 6x4=24 6x5=30 6x6=36 
7x1=7 7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49 
8x1=8 8x2=16 8x3=24 8x4=32 8x5=40 8x6=48 8x7=56 8x8=64 
9x1=9 9x2=18 9x3=27 9x4=36 9x5=45 9x6=54 9x7=63 9x8=72 9x9=81 
'''

# 练习题：使用while循环实现99乘法表
# x = 0
# while x<=9:
#     y = 0
#     while y<=x:
#         print(f'{x}x{y}={x*y}', end=" ")
#         y += 1
#     x += 1
#     print()
# 反向输出99乘法表
# x = 9
# while x > 0:
#     y = x
#     while y > 0:
#         print(f'{x}x{y}={x*y}', end=" ")
#         y -= 1
#     x -= 1
#     print()














































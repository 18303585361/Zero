# 循环结构

# while 循环
# 定义变量
# num = 1
#
# # while 循环：判断当前的条件是否成立
# while num <= 10:
#     # 要执行代码
#     print(num)  # 输出 变量 内容
#     num += 1    # 更改变量，目的主要为了继续进行下一步，并且朝着循环结束的方向执行

# print(num)


# for 循环  通常  for循环用来遍历一个容器类型的数据
# vars = '123456789'
# vars = [1,2,3,4,5]
# 使用for..in 循环 遍历容器类型数据，那么中间的 i 变量就是当前容器类型中的每一个元素
# for i in vars:
#     print(i)

# for 循环一列数字
# for i in range(0,10):
#     print(i)

# 1.break 语句   指跳出
# 2.continue 语句  指跳过
# 3.pass 语句   指占位

# range() 是一个函数，返回一个迭代对象，
# print(range(1,10),type(range（1,10）))

# num = 0
# while num < 10:
#     num += 1
#     # 判断当前的num 是否为偶数
#     if num % 2== 0:
#         continue    # 跳过本次循环，继续执行下一次
#     else:
#         print(num)
#
#     # 判断当前的num是否 == 7
#     if num == 7:
#         break   # 跳出循环，后面不再执行，结束循环


# 1.exit()
# 2.quit()
# 适用于结束当前python解释器程序的，而 break 和 continue 是用来控制程序的


# 作业练习：
'''
循环输出十行十列 ❤
'''
# x = 0
# s = '❤'
# while x <= 10:
#     print(s*10)
#     x += 1
'''
循环输出n行n列 ❤
'''
# x = int(input('请输入你想输出多少行❤，只能输入正整数：'))
# y = int(input('请输入你想输出多少列❤，只能输入正整数：'))
# love = '❤'
# while x > 0:
#     print( love * y )
#     x -= 1
'''
循环交替输出 n行n列 ❤ ☀
'''
# x = int(input('请输入你想输出多少行❤，只能输入正整数：'))
# y = int(input('请输入你想输出多少列❤，只能输入正整数：'))
# love = '❤'
# shu = '☀'
# while x > 0:
#     if x % 2 == 0:
#         print(shu * y)
#     else:
#         print(love * y)
#     x -= 1

'''
隔列交替输出 ❤ ☀
'''
x = int(input('请输入你想输出多少行❤，只能输入正整数：'))
y = int(input('请输入你想输出多少列❤，只能输入正整数：'))
love = '❤'
shu = '☀'
while x > 0:
    while y > 0:
        if y % 2 == 0:
            print(shu)
            y -= 1
        else:
            print(love)
            y -= 1
    x -= 1






















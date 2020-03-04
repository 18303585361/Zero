'''
循环输出十行十列 ❤
'''
# x = 0
# s = '❤'
# while x <= 10:
#     print(s*10)
#     x += 1

# 老师的答案：
# 第一种：
# num = 1
# while num <= 100:
#     print('❤', end=' ')
#     # 判断 是否需要换行
#     if num % 10 == 0:
#         print()
#     num += 1
# 第二种：
# num = 0
# while num < 100:
#     print('❤', end=' ')
#     print(num % 10, end="")
#     # 判断 是否需要换行
#     if num % 10 == 9:
#         print()
#     num += 1

# 隔行换色
# num = 0
# while num < 100:
#     if num // 10 % 2 == 0:
#         print('❤', end=' ')
#     elif num // 10 % 2 == 1:
#         print('☀', end=" ")
#     # 判断 是否需要换行
#     if num % 10 == 9:
#         print()
#     num += 1

# 作用：三角形 菱形



# 隔列换色
# num = 0
# while num < 100:
#     # 判断当前数是奇数还是偶数
#     if num%2 == 0:
#         print('❤', end=' ')
#     else:
#         print('☀', end=" ")
#     # 判断 是否需要换行
#     if num % 10 == 9:
#         print()
#     num += 1

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
# x = int(input('请输入你想输出多少行❤，只能输入正整数：'))
# y = int(input('请输入你想输出多少列❤，只能输入正整数：'))
# love = '❤'
# shu = '☀'
# while x > 0:
#     while y > 0:
#         if y % 2 == 0:
#             print(shu)
#             y -= 1
#         else:
#             print(love)
#             y -= 1
#     x -= 1
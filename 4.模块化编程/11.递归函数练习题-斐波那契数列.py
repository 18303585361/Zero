# 递归函数的练习

# 斐波那契数列 1,1,2,3,5,8,13。。。
# 求第n位上的数是多少？  例如第六位

num = 0
def fb(n):
    global num
    num += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fb(n-1) + fb(n-2)

res = fb(6)
print(res)
print(num)  # 计算斐波那契数列数列第6位共计算15次
'''
fb(6) ==>   fb(5)                            +       fb(4)                   
            ==> fb(4) + fb(3)                       ==> fb(3) + fb(2)
                ==> fb(3) + fb(2)                       ==> fb(2) + fb(1)
                    ==> fb(2) + fb(1)
'''






































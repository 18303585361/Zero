# 实现阶乘 求一个数的阶乘结果   7  1*2*3*4*5*6*7

def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n*jiecheng(n-1)

res = jiecheng(7)
print(res)

'''
递归函数的效率并不会高，尽量能不用就不用。。。
一个函数如果调用后，没有结束，那么在栈空间中一直存在，知道这个函数运算结束才销毁

'''





































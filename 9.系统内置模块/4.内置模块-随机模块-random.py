# 随机模块 random
import random

# random.random()   返回 0—1 之间的随机小数(左闭右开)
# res = random.random()

# random.randrange([开始值], 结束值, [间隔值])   随机获取指定范围内的整数
# res = random.randrange(5)   # 一个参数时，随机从 0 到整数之间的值
# res = random.randrange(5,10)    # 两个参数，随机从第一个值到第二个值之间的随机整数（左闭右开）
# res = random.randrange(5,20,2)  # 三个参数，按照指定步进值随机从第一个值到第二个值之间的整数（左闭右开）
# 随机数的应用场景：数字验证码；高并发下的订单号。。。

# random.randint()  随机产生指定范围内的随机整数
# res = random.randint(5,10)

# random.uniform()  获取指定范围内的随机小数
# res = random.uniform(5,10)

# random.choice()   随机获取容器类型中的值
# res = random.choice('32174098357')
# res = random.choice([1,2,3,4,5,6,7,8,9])

# random.shuffle()  随机打乱当前列表中的值,没有返回值，直接打乱原数据
# arr = [1,2,3,4,5,6,7,8]
# res = random.shuffle(arr)
# print(res,arr)





















































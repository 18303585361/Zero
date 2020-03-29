# 装饰器应用场景-函数执行时间的统计
import time
# 定义一个统计函数执行时间的装饰器
def runtime(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter() - start
        print(f'函数的调用执行时间为：{end}')
    return inner
# 定义一个函数
@runtime
def func():
    for i in range(10):
        print(i,end=" ")
        time.sleep(1)

func()  # 结果：0 1 2 3 4 5 6 7 8 9 函数的调用执行时间为：10.1059011




































































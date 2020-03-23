# 时间模块 time
import time

'''
概念：
    1.时间戳   1584147615.3953142  表示从1970年1月1日0时0分0秒到现在的一个秒数，目前可以计算到2038年
    2.时间字符串     Sat Mar 14 09:03:12 2020
    3.时间元组  time.struct_time(tm_year=2020, tm_mon=3, tm_mday=14, tm_hour=9, tm_min=5, tm_sec=50, tm_wday=5, tm_yday=74, tm_isdst=0)
'''

# 1.获取当前系统的时间戳  ***
# res = time.time()

# 2. 获取当前系统时间(时间字符串）
# res = time.ctime()

# 3. 获取当前系统时间（时间元组）
# res = time.localtime()

# 4.以上时间字符串和时间元组可以通过指定的时间戳来获取
# t = 1564007615.3953142
# res = time.ctime(t)
# res = time.localtime(t)

# 5.使用localtime方法获取的时间元组如何格式化成为 XXXX年XX月XX日 时：分：秒
# res = time.localtime()
# print(f'{res.tm_year}年{res.tm_mon}月{res.tm_mday}日 {res.tm_hour}：{res.tm_min}：{res.tm_sec} 星期{res.tm_wday+1}')

# 6.strftime(格式)  格式化时间 ***
# res = time.strftime('%Y年%m月%d日 %H：%M：%S 星期%w')

# 7.sleep(秒) 做时间休眠，在给定的秒数内暂停调用线程的执行。该参数可以是浮点数，以指示更精确的睡眠时间。   ***
# print(res)
# time.sleep(3)
# print(res)

# 8.perf_counter()  计算程序的运行时间
# 100万次的字符串比较 需要执行的时间
# start = time.perf_counter()
# for i in range(1000000):
#     if 'abc' > 'acd':
#         pass
# end = time.perf_counter()
# print(end-start)

# start = time.perf_counter()
# for i in range(1000000):
#     if 103 > 100 :
#         pass
# end = time.perf_counter()
# print(end-start)
































































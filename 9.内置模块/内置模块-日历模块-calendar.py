# 日历模块 calendar
import calendar
import time

# 1.monthrange(年,月)    返回指定年份和月份的数据，月份的第一天是周几，和月份中的天数。
# res = calendar.month(2020,3)
def showdate(year,month):
    res = calendar.monthrange(year,month)
    days = res[1]    # 当前月份的天数
    w = res[0]+1    # 当前月份第一天周几信息
    print(f'======{year}年{month}月的日历信息======')
    print(' 一  二  三  四  五   六  日 ')
    print('*****************************')
    # 实现日历信息的输出
    d = 1
    while d <= days:
        # 循环周
        for i in range(1,8):
            # 判断是否输出
            if d > days or (i<w and d==1):
                print('    ',end='')
            else:
                print(' {:0>2d} '.format(d),end='')
                d += 1
        print()
    print('*****************************')


# 作业练习：切换 <上一个月     下一个月>

res = time.localtime()
year = res.tm_year
month = res.tm_mon
showdate(year, month)
a = 0
b = 0
while True:
    user = input('输入 < 查看上个月日历，输入 > 查看下个月日历!输入 exit 关闭\n')
    if user == 'exit':
        break
    else:
        if user == '<':
            a += 1
            if month > 0:
                showdate(year, month - a)
            elif month ==0:
                showdate(year - 1, month)
        elif user == '>':
            b += 1
            if month > 12:
                month = 1
                showdate(year + 1, month)
            else:
                showdate(year, month + a)











































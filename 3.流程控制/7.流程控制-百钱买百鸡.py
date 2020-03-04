# 百钱买百鸡
'''
一共有100块钱，需要买100只鸡
公鸡 == 3元
母鸡 == 1元
小鸡 == 0.5元

问：100块钱买100只鸡，一共有多少种方案

1.都买母鸡
'''
# a = 1
# for gj in range(1,34):
#     for mj in range(1,101):
#         for xj in range(1,201):
#            if gj+mj+xj == 100 and 3*gj + mj + 0.5*xj == 100:
#                print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只')
#                a += 1
# print(f'共有{a}种方案')

a = 1
for gj in range(1,34):
    for mj in range(1,101):
        xj = 100 - gj - mj
        if gj+mj+xj == 100 and 3*gj + mj + 0.5*xj == 100:
            print(f'公鸡买{gj}只，母鸡买{mj}只，小鸡买{xj}只')
            a += 1
print(f'共有{a}种方案')










































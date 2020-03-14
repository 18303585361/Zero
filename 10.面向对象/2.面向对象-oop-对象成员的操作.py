# 对象成员的操作
'''
什么是对象的成员？
    一个对象通过类实例化之后，那么在类中定义的属性和方法，可以使用实例化的对象进行操作
    类中定义的属性也称为 成员属性，类中定义的方法也称为 成员方法
'''
# 定义一个汽车的类
class Cart():
    # 属性 ==> 特征 ==> 变量
    color = '白色'    # 表示颜色特征
    brand = '奥迪'    # 表示品牌属性
    pailiang = 2.4    # 表示排量属性

    # 方法 ==> 功能 ==> 函数
    def lahuo(self):
        print('小汽车能拉货')
    def doufeng(self):
        print('小汽车能兜风')
    def bamei(self):
        print('带妹子去嗨')

# 实例化对象
a = Cart()
b = Cart()
# print(a)
# print(b)
'''
一个类可以实例化多个对象
以上的 a 和 b 变量都是对象，也都是通过 Cart 这个类实例化出来的对象
但是 a 和 b 是两个对象，相同之处就在于都是 由同一个类实例化出来的
'''
# 对象成员的操作   1.在类的外部，使用对象操作成员
# res = a.color   # 通过对象访问类中的属性
a.color = '黑色'  # 修改对象的属性
# 此时 b 对象的color属性是什么？
a.name = 'A6'   # 添加对象的属性
# 此时 b 对象是否有name这个属性？
print(b.color)  # b对象的属性依然是原来的值
# res = a.lahuo() # 通过对象访问类中的方法
print(a.color)
print(a.name)












































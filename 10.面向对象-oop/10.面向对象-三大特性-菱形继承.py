# 菱形继承
'''
mro()   获取MRO列表，就是类的继承关系
    例：print(C.mro())
super()
    使用super()去调用父级的方法（属性）
    实际上是在用super 调用MRO列表中的上一级中的方法（属性）
super()
    本身调用父级方法时
    传递的self对象，就是这个方法中的那个self对象自己
'''

# 祖先类
class HuMan():
    num = 444
    def eat(self):
        print(self.num)
        print('顿顿小烧烤')
# 父亲类
class F(HuMan):
    num = 333
    def eat(self):
        super().eat()
        print(super().num)
        print('大口喝酒，大口吃肉')

# 母亲类
class M(HuMan):
    num = 222
    def eat(self):
        super().eat()
        print(super().num)
        print('动作优雅，浅尝辄止')

# 孩子类
class C(F, M):
    num = 111
    def eat(self):
        super().eat()
        print(super().num)
        print('吃也哭，不吃也哭')

# 实例化对象
c = C()
c.eat()
print(C.mro())
'''
输出结果：
    111
    顿顿小烧烤
    444
    动作优雅，浅尝辄止
    222
    大口喝酒，大口吃肉
    333
    吃也哭，不吃也哭
'''











































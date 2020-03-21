# 单继承和多继承
'''
一个父类可以被多个子类继承，还可以存在链式继承
链式继承：
    1.a类继承b类，b类继承了c类，c类继承了d类
单继承：
    1.一个类只能继承一个父类的方式
    2.语法格式：
        class 父类():
            pass
        class 子类(父类):
            pass
多继承：
    1.一个类可以去继承多个父类的方式
    2.语法格式：
        class 父类():
            pass
        class 母类():
            pass
        class 子类(父类,母类):
            pass
'''


class F():
    def eat(self):
        print('大口喝酒，大口吃肉')


class M():
    def eat(self):
        print('动作优雅，浅尝辄止')


class C(F, M):
    def eat(self):
        super().eat()   # 多继承和多继承中的父类方法的调用
        print('吃也哭，不吃也哭')

# 实例化对象
c = C()
c.eat()

















































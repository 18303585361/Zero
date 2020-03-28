# 抽象类（了解）

'''
抽象类是一个特殊的类：
    1.抽象类定义以后不能用，不能直接实例化成为一个对象
    2.抽象类中包含了抽象方法，抽象方法就是没有实现代码的方法
    3.抽象类需要子类继承，并重写父类的抽象方法，才可以使用

抽象类一般应用在程序设计，程序设计中一般是要对功能和需求进行规划
其中有一些需求是明确的并且可以完成的，但是也有一些需求是不明确或者不确定具体需要怎么实现
此时，就可以把这个不确定怎么实现或者需要后面去实现的方法，定义为抽象方法（只定义方法名，不写具体代码）

举例：
    公司有一项新的产品需要开发，交给了开发部门的老大
    这个老大开始会规划设计怎么去完成这个产品的开发
    必须项目需要用到不同的技术，需要不同的人去完成
    这样的话，老大就自己完成了一部分功能，还有一部分定义了需求，但是没有具体实现，需要其它人来实现

    这样，已经完成的部分就是 普通方法，定义了但未完成的就可以理解为抽象方法
'''
import abc
# 如果要定义为抽象类，那么这个类的metaclass属性必须是    metaclass=abc.ABCMeta
class WriteCode(metaclass=abc.ABCMeta):

    # 需要抽象的方法，使用装饰器进行装饰
    @abc.abstractmethod
    def write_pip(self):
        pass
    def write_java(self):
        print('实现了java代码的开发')
    def write_python(self):
        print('实现了python代码的开发')

# 抽象类不能直接实例化
# a = WriteCode() # 报错    Can't instantiate abstract class WriteCode with abstract methods write_pip

# 定义子类，继承抽象类，并实现抽象类中的抽象方法
class Demo(WriteCode):
    def write_pip(self):
        print('实现了pip代码的开发')

obj = Demo()
obj.write_java()
obj.write_python()
obj.write_pip()
print(obj)

'''
抽象类的应用：
    例如要开发一个框架，这个框架要有什么什么功能
    但是你具体用这个框架开发什么样的产品，并不清楚，因此，这个框架中能否知道你要什么样的开发
    框架就具备一定的功能即可，剩下的需要具体开发项目的人来实现自己的业务逻辑
'''

























































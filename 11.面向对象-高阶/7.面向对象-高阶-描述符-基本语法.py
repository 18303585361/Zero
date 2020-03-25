# 面向对象-高阶-描述符与设计
'''
当一个类中包含了三个魔术方法之一，或者全部时，那么这个类就称为描述符类
    三个魔术方法是指： __get__   __set__     __delete__
    作用：对一个类中的某个成员进行一个详细的管理操作（获取、赋值、删除）
          描述符就是代理了一个类中的成员的操作，描述符属于类，只能定义为类的属性
    使用格式(示例如下）：
        把当前的描述符类赋值给一个需要代理的类中的成员属性


        ** 一个类中成员的值是另一个描述符类的对象
        ** 那么当对这个类中的成员进行操作时，可以理解为就是对另一个对象的操作
'''
# 定义描述符类
class PersonName():
    __name = 'abc'
    def __get__(self, instance, owner):
        return self.__name
    def __set__(self, instance, value):
        self.__name = value
    def __delete__(self, instance):
        del self.__name
        print('不允许删除')
# 定义的普通类
class Person():
    # 把类中的一个成员属性交给一个描述符类来实现
    name = PersonName()

# 实例化对象
zs = Person()
print(zs.name)
zs.name = '张三'
print(zs.name)
del zs.name
print(zs.name)





























































# 面向对象 常用函数
'''
issubclass(子类，父类)  检测一个类是否是另一个类的子类
isinstance(对象, 类)  检测一个对象是否是该类或该类的子类的实例化对象

hasattr(类/对象, 成员) 检测类/对象是否包含指定名称的成员(除了私有成员）
getattr(类/对象, 成员名) 获取类/对象的成员（除了私有成员）
setattr(类/对象, 成员名, 赋值属性) 设置类/对象的成员属性值
delattr(类/对象, 成员名称) 删除类/对象的成员属性值
dir() 获取当前对象所有可以访问的成员列表
'''
class A():
    pass
class B(A):
    pass
class C(A):
    ccc = 'abc'

class D(B, C):
    name = 'a'
    __age = 20

    def say(self):
        pass

d = D()
# 检测类和对象相关
# issubclass(子类，父类)  检测一个类是否是另一个类的子类
# res = issubclass(D, B)  # 检测D类是不是B类的子类

# isinstance(对象, 类)  检测一个对象是否是该类或该类的子类的实例化对象
# res = isinstance(d, D)  # 检测 d 是不是 D类的实例化

# 操作类和对象成员相关
# hasattr(类/对象, 成员) 检测类/对象是否包含指定名称的成员(除了私有成员)
# res = hasattr(d, 'name')

# getattr(类/对象, 成员名) 获取类/对象的成员（除了私有成员）
# res = getattr(d,'name')

# setattr(类/对象, 成员名, 赋值属性) 设置类/对象的成员属性值
# res = setattr(d, 'name', 'or')  # 无返回值
# print(d.name)

# delattr(类/对象, 成员名称) 删除类/对象的成员属性值
# res = delattr(D, 'name')    # 无返回值

# dir() 获取当前对象所有可以访问的成员列表
res = dir(d)
print(res)




























































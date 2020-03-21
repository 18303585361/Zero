# 继承关系检测
'''
在实现继承语法后，程序会自动生成一个继承列表 MRO 方法关系列表

MRO列表生成规则：
    1.同一等级的类，按照子类中的继承顺序摆放
    2.先子类、后父类的顺序原则，最终的类是 object 类
    3.使用格式：
        print(需要检测的类名.mro())
super()
    1.在调用该函数时，是去 MRO 列表上找上一个类
    2.在调用时，会自动把当前 self 传入上一级类的方法中
类关系检测 issubclass()

'''
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

# 获取类的 MRO 列表
# print(C.mro())

# 检测一个类是否是另一个类的子类
res = issubclass(D, B)  # 检测D类是不是B类的子类
res = issubclass(B, D)  # 检测B类是不是D类的子类
print(res)

























































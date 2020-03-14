# 魔术方法  初始化方法
'''
魔术方法：
    魔术方法也和普通方法一样，都是类中定义的成员方法
    魔术方法不需要去手动调用的，魔术方法会在某种情况下，自动触发（自动执行）
    魔术方法还有一个比较特殊的地方：多数的魔术方法前后都有两个连续的下划线
    魔术方法不是我们自己定义的，而是系统定义好的，我们来使用

__init__    初始化方法
    触发机制：在通过类实例化对象后，自动触发的一个方法
    作用：    可以在对象实例化后，完成对象的初始化（属性的赋值,方法的调用）
    应用场景：文件的打开，数据的获取。。。干活前的一些准备功能。。。

'''
class Person():
    # 成员属性
    name = None
    age = None
    sex = None

    # __init__  初始化方法
    def __init__(self,n,a,s):
        # print('我是一个初始化方法')
        # 完成对象属性的初始化
        self.name = n
        self.age = a
        self.sex = s
        # 调用方法
        self.say()
    # 成员方法
    def say(self):
        print(f'大噶好，唔系{self.name}，系兄弟就来砍我。。')

# 实例化对象
# zzh = Person()
zzh = Person('渣渣灰',56,'男')
# print(zzh.name)




























































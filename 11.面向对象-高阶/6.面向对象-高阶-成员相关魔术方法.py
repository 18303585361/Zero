# 成员相关魔术方法
'''
1. __getattrbute__
    触发机制：当访问对象成员时自动触发，无论当前成员是否存在
    作用：可以在获取对象成员时，对数据进行一些处理
    参数：一个 self 接收对象，一个 item 接收当前访问的成员名称
    返回值：可有可无，返回的值就是访问的结果
    注意事项：在当前的魔术方法中，禁止使用 对象.成员 的方式进行成员访问，会触发递归
             如果想要在当前魔术方法中访问对象的成员，必须使用 object.__getattrbute__ 来进行
             格式：object.__getattribute__(self,item)
2.

'''
# 定义类
class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print('聊聊人生，谈谈理想')

    def sing(self):
        print('高歌一曲')

    # 获取对象成员时自动触发

    def __getattribute__(self, item):
        # 通过 hsattr 来判断是否存在这个属性
        if

        # 在方法中使用 object 来获取属性值
        res = print(object.__getattribute__(self,item))
        # 在方法中可以对访问的成员数据进行处理
        return res[0]+'*'+res[2]

# 实例化对象
zs = Person('张三丰',120,'男')
print(zs.name)


























































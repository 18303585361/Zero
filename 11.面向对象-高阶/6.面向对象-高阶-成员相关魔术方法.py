# 成员相关魔术方法
'''
1. __getattribute__(self, item) 优先级最高
    触发机制：当访问对象成员时自动触发，无论当前成员是否存在
    作用：可以在获取对象成员时，对数据进行一些处理
    参数：一个 self 接收对象，一个 item 接收当前访问的成员名称
    返回值：可有可无，返回的值就是访问的结果
    注意事项：在当前的魔术方法中，禁止对当前对象的成员进行访问，会报错
             如果想要在当前魔术方法中访问对象的成员，必须使用 object.__getattrbute__ 来进行
             格式：object.__getattribute__(self,item)
2.__getattr__(self, item)   ==>类比不存在成员时操作
    触发机制：当访问对象中不存在的成员时，自动触发
    作用：防止访问不存在的成员时报错，也可以为不存在的成员进行赋值操作
    参数：一个 self 接收当前对象，一个 item 接收当前访问的成员名称
    返回值：可有可无
    注意事项：当存在 __getattribute__ 方法时，会去执行 __getattribute__
             也要注意，不要在当前的方法中再次访问这个不存在的成员，会报错
3.__setattr__(self, key, value) ==>类比添加、修改操作
    触发机制：给对象的成员进行赋值操作时自动触发（包括添加、修改成员）
    作用：可以限制或管理对象成员的添加和修改操作
    参数：self 接收当前对象，key 设置成员名，value 设置成员值
    返回值：无
    注意事项：在当前的魔术方法中，禁止给当前对象的成员直接进行赋值操作，会报错，触发递归
             如果想要给当前对象的成员进行复制，需要借助 object
             格式：object.__setattr__(self,key,value)
4.__delattr__(self, item)   ==>类比删除操作
    触发机制：当删除对象成员时自动触发
    作用：可以限制对象成员的删除，还可以删除不存在成员时防止报错
    参数：self 接收当前对象， item 删除的成员名称
    返回值：可有可无
    注意事项：在当前魔术方法中禁止直接删除对象的成员，会报错，触发递归
             如果想要删除当前对象的成员，需要使用 object
             格式：object.__delattr__(self, item)
5.类中访问成员的顺序（以下步骤是调用某个成员时的顺序，如果前面的调用成功，后面的不再执行）
    1.调用 __getattribute__(self, item)
    2.当方法 1 不存在时，调用数据描述符
    3.当方法 2 不存在时，调用当前对象的成员
    4.当方法 3 不存在时，调用当前类的成员
    5.当方法 4 不存在时，调用非数据描述符
    6.当方法 5 不存在时，调用父类成员
    7.当方法 6 不存在时，调用 __getattr__ 方法
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

    # def __getattribute__(self, item):
    #     try:
    #         # 在方法中使用 object 来获取属性值
    #         res = print(object.__getattribute__(self,item))
    #         # 在方法中可以对访问的成员数据进行处理
    #         return res[0]+'*'+res[2]
    #     except:
    #         return False
    # 当访问不存在的成员时自动触发
    def __getattr__(self, item):
        print(item)
        return '访问的成员不存在'

    # 当给对象成员进行赋值时触发，该方法中如果没有给对象成员赋值，那么对象成员赋值失败
    def __setattr__(self, key, value):
        print(self,key,value)
        object.__setattr__(self,key,value)
    # 当删除对象的成员时自动触发
    def __delattr__(self, item):
        print(item)
        object.__delattr__(self,item)

# 实例化对象
zs = Person('张三丰',120,'男')
print(zs.name)
print(zs.abc)
zs.abc = 'aabbcc'
print(zs.abc)

del zs.name
print(zs.name)























































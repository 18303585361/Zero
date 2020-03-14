# 成员方法中的self详解
'''
self
    1.在方法中只是一个形参，并不是关键字
    2.在方法中代表的是当前这个对象自己
    3.在方法中代表对象，可以去操作成员，可以使用self在类的内部访问成员
    4. 单词本身的意思    自己
    5. 在类的方法中 代表 当前这个对象
    6. 代表调用这个方法的对象,谁调用了这个方法，self就代表谁
    7. 可以在类的内部代替对象进行各种操作
方法的分类
    含有self或者可以接受对象作为参数的方法：非绑定类方法
    不含self或者不能接受对象作为参数的方法：绑定类方法

    非绑定类方法：只能使用对象去访问
    绑定类方法：只能通过类去访问
'''
class Person():
    # 成员属性
    name = '名字'
    age = '年龄'
    sex = '性别'

    # 成员方法
    def sing(self):
        print('会唱。。。')
    def dance(self):
        print('会跳。。。')
    def rap(self):
        print(f'我是{self.name}我会rap...')

    def func(self):
        # 测试，在类的内部是否可以像类的外部一样，去访问和操作成员
        # print(self)
        # print(self.name)    # 访问对象的属性
        # self.name = '张三三'   # 修改对象的属性
        # self.sanwei = '80 80 80'    # 添加对象的属性
        # print(self.sanwei)
        self.rap()
        # 只要是对象能干的事儿，self 都可以代表对象去完成
        # 比如：成员属性的所有操作（添加、删除、更新、访问、调用...）
    # 定义不含self的方法   绑定类方法   （不接受
    def func2(self):
        print('我是一个没有self的方法')

# 实例化对象
zs = Person()
# zs.name = '张三'
# 通过类实例化的对象，可以在类的外部去访问成员属性和成员方法 对象.成员
# print(zs)
# zs.func()
# zs.rap()

# zs.func2()
Person.func2()































































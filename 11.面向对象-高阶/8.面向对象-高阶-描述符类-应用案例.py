
'''
要求：学员的分数只能在0——100范围中
解决方法：
    1. __init__ 方法中检测当前分数范围
        这个解决方案只能在对象初始化时有效
    2. 定义一个 __setattr__ 魔术方法来检测
        检测如果给 score 分数进行赋值时，进行分数的检测判断
    3.假如 学员的分数不止一个时，怎么办？比如：语文分数、数学分数、英语分数
      另外类中的代码是否比较多？
      可以使用描述符类代理我们的分数这个属性
      ①. 定义Socre描述符类
      ②. 把学生类中的score这个成员交给描述符类进行代理
      ③. 只要在代理的描述符类中对分数进行赋值和获取就ok
'''

# 定义一个学生类，记录学员的ID，名字（name），分数（score）
# class Student():
#     def __init__(self,id,name,score):
#         self.id = id
#         self.name = name
#         self.score = score
#         # 检测分数范围
#         # if score >= 0 and score <= 100:
#         #     self.score = score
#         # else:
#         #     print('当前分数不正确')
#
#     def returnMe(self):
#         info =  f'''
# 学员编号：{self.id}
# 学员姓名：{self.name}
# 学员分数：{self.score}
#         '''
#         print(info)
#
#     def __setattr__(self, key, value):
#         # 在方法中检测是否是给 score 进行赋值操作
#         if key == 'score':
#             if value >= 0 and value <= 100:
#                 object.__setattr__(self,key,value)
#             else:
#                 print('当前分数不正确')
#         else:
#             object.__setattr__(self,key,value)


# 使用描述符代理分数属性
# 描述符类
class Score():
    __score = 0
    def __get__(self, instance, owner):
        return self.__score
    def __set__(self, instance, value):
        if value >= 0 and value <= 100:
            self.__score = value
        else:
            print('分数不符合要求')
# 学生类
class Student():
    score = Score()
    def __init__(self,id,name,score):
        self.id = id
        self.name = name
        self.score = score

    def returnMe(self):
        info =  f'''
学员编号：{self.id}
学员姓名：{self.name}
学员分数：{self.score}
        '''
        print(info)

# 实例化对象
zs = Student('1','张三',99)
zs.returnMe()
zs.score = -20
zs.returnMe()
zs.score = 88
zs.returnMe()



























































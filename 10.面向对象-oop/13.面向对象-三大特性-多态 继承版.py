# 多态 继承版

'''
定义一个接口规范类，其它类都继承这个类，并实现（重写）父类中的方法
由于每个对象实现父类方法的方式或者过程都不相同，最后结果是不一样的形态
'''
# 定义 USB
class Usb():
    '''
    当前类的说明：
        这个类是一个接口规范类，需要子类继承并实现 start 方法
        start方法 不做任何具体功能的实现
    '''
    # 在USB类中定义一个规范的接口方法，但是不实现任何功能
    def start(self):
        pass
# 定义鼠标类
class Mouse(Usb):
    def start(self):
        print('鼠标启动成功，可以双击单击')

# 定义键盘类
class KeyBord(Usb):
    def start(self):
        print('键盘启动成功了')

# 定义U盘类
class Udisk(Usb):
    def start(self):
        print('U盘启动了')

# 实例化对象
m = Mouse() # 鼠标对象
k = KeyBord()   # 键盘对象
u = Udisk() # U盘对象

m.start()
k.start()
u.start()































































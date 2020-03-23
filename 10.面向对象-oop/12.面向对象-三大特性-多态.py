# 多态
'''
多态：
    对于同一个方法，由于调用对象不同（传入的对象不同），实现了不同的结果

'''
# 定义电脑类
class Computer():
    # 在电脑类中定义一个USB的规范接口方法
    def usb(self, obj):
        obj.start()

# 定义鼠标类
class Mouse():
    def start(self):
        print('鼠标启动成功，可以双击单击')

# 定义键盘类
class KeyBord():
    def start(self):
        print('键盘启动成功了')

# 定义U盘类
class Udisk():
    def start(self):
        print('U盘启动了')

c = Computer()  # 电脑对象
m = Mouse()     # 鼠标对象
k = KeyBord()   # 键盘对象
u = Udisk()     # U 盘对象

# 把不同的设备插入到电脑的usb的接口中
c.usb(m)
c.usb(k)
c.usb(u)


























































# 练习题：使用数据写入文件的方式，完成一个注册和登录

'''
实现功能：
    1.用户输入用户名和密码以及确认密码
    2.用户名不能重复
    3.两次密码要一致
    4.可以用已经注册的账户登录
    5.密码如果输错3次，则锁定，不能登录

注册功能：
    1.需要用户输入注册的用户名和密码以及确认密码
    2.注册时，如果用户名已经存在，则不能再次注册
登陆功能：
    1.需要使用已经注册的用户信息登录
    2.密码输入错误3次后，锁定账户信息（不能再使用这个账户进行登录操作）
'''
cz = int(input('欢迎来到XXX，请选择你要的功能：\n0 注册\n1 登录\n'))
# 注册功能的实现
if cz == 0:
    dataname = open('G:\Code\-.test\dataname.txt','a+',encoding='utf-8')
    username = input('请输入你想注册的用户名：\n')
    dataname.write(username)
    user = dataname.read()
    for i in user:
        if username == i:
            print('你输入的用户名已存在，请重新输入！')
        else:
            data = dict()
            pw1 = input('请输入密码：\n')
            pw2 = input('请确认密码：\n')
            while pw1 == pw2:
                data.username = pw2
                print('恭喜你，注册成功')
                exit()
            print('请重新输入密码')






























































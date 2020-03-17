# 文件操作相关函数

'''
1.open()  打开文件
    格式：open(文件路径，打开方式，[字符集])

2.write()   写入内容
    格式：文件对象.write(字符串)  只能写字符串
3.writelines()  写入容器类型数据
    格式：文件对象.writelines(容器类型数据)
    注意：容器类型数据中的元素也必须时可写入的字符串类型

4.read()    读取内容
    格式： 文件对象.read()  从当前指针位置读取到最后
           文件对象.read(读取的字节数)    可以读取指定长度的字符
5.readline()    读取一行内容
    格式： 文件对象.readline() 一次读取一行
           文件对象.readline(字节数)
6.readlines()   读取所有行内容
    格式： 文件对象.readlines()     读取所有行，每一行作为一个元素，返回一个列表
           文件对象.readlines(6)    按照行进行读取，可以设置读取的字节数，设置的字节数不足一行按一行算
7.seek()    设置指针位置

8.truncate()    截取文件内容
    格式：

9.close()   关闭文件
    格式： 文件对象.close()    关闭打开的文件，方便资源回收

10.文件的便捷写法
    格式：with open(文件路径，打开方式） as 变量：
            变量.操作()
'''
##  写入相关函数
# vars = 5211 # int类型无法写入
# vars = ['hello','world','1','2','3']
# vars = {'name':'zs','age':'123'}
# with open('G:\Code\-.test/1.txt','w',encoding='utf-8') as fp:
    # fp.write(vars)  # 只能写入字符串类型数据
    # fp.writelines(vars) # 可以写入容器类型数据，注意容器中的元素也必须时字符串类型

##  读取相关函数
# with open('G:/Code/-.test/1.txt','r',encoding='utf-8') as fp:
    # fp.seek(2)  # 设置指针的位置
    # res = fp.read() # 默认从当前指针开始读取到最后
    # res = fp.read(7)    # 设置读取的字节长度
    # res = fp.readline() # 一次只读取一行内容
    # print(res,end="")
    # res = fp.readline(30)   # 可以读取当前行中的指定字节长度
    # res = fp.readlines()    #一次去读多行数据，每一行作为一个元素，返回一个列表
    # res = fp.readlines(6)   # 按照行进行读取，可以设置读取的字节数，设置的字节数不足一行按一行算
    # print(res,end='')

## seek()   设置文件指针位置
# with open('G:/Code/-.test/1.txt','r+',encoding='utf-8') as fp:
    # a+模式，指针默认在文件的最后面，所以直接读是读取不到内容的
#     fp.seek(0)  # 把文件指针设置到文件的开头位置
#     fp.seek(0,2)    # 把文件指针设置在文件的末尾
#     fp.seek(10) # 设置文件指针的位置
    # fp.write('\n0000')
#     res = fp.read()
# print(res)

## truncate()   截取文件内容
# with open('G:/Code/-.test/1.txt','r+',encoding='utf-8') as fp:
#     res = fp.truncate(5)
    # 默认从文件的首行的首个字符开始进行截断，截断的长度为 size 个字节数。
    # size 如果为0，则从当前位置直接截断到最后
# print(res)

# 练习题：使用数据写入文件的方式，完成一个注册和登陆。










































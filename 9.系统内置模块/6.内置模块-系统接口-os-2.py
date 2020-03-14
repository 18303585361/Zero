# 系统接口模块 os
'''
    1.  os.rmdir()  删除 空 文件夹
        os.removedirs() 递归删除 空 文件夹
            在mac 系统中，连续创建了abc目录后又在里面创建def，又在def里面创建aaa
            此时，使用os.removedirs('./abc/def/aaa') 删除时，只删除了aaa
            因为 mac 系统中的文件夹只要被使用过，都会默认创建一个隐藏文件，因此这个文件夹不是空文件夹

    2.  os.remove() 删除文件
    3.  os.rename(参数一，参数二) 修改文件或文件夹的名字
            例：os.remove('./a','./AAA')    # 把 a 修改成 AAA
    4.  os.system() 执行操作系统中的命令
            该函数有返回值，需要定义变量接收

'''
import os

# os.rmdir('./a') # a 是一个空文件夹
# os.rmdir('./b') # b 是含有一个文件夹的 目录    OSError：
# os.rmdir('./c') # c 是含有一个文件的 目录     OSError：
# os.rmdir('./b/c')   # 只是删除了 b 文件夹里面的 c 文件夹

# os.removedirs('./abc/def/aaa')  # 递归删除了 abc def aaa 三个文件夹

# os.remove('./a','./AAA')    # 把 a 修改成 AAA

# os.rename('')

res = os.system('ipconfig')






















































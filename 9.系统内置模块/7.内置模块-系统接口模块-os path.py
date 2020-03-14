# os.path   系统模块中的路径模块
import os


# 将相对路径转化为绝对路径  ***
# res = os.path.abspath('./') # G:\Code\9.系统内置模块

# 获取路径中的主体部分（返回路径中的最后一部分）
# res = os.path.basename('G:\Code\9.系统内置模块')  # 9.系统内置模块

# 获取路径中的路径部分（返回路径中最后一部分之前的内容）
# res = os.path.dirname('G:\Code\9.系统内置模块')   # G:\Code

# join()    连接多个路径，组成一个新的路径
# res = os.path.join('./a/b/c','2.jpg')   # ./a/b/c/2.jpg

# split()   拆分路径，把路径拆分为路径和主体部分
# res = os.path.split('./abc/def/aaa')    # ('./abc/def/','aaa')

# splitext()    拆分路径，可以拆分文件后缀名
# res = os.path.splitext('./a/b/c/2.jpg') # ('./a/b/c/2','.jpg')

# 获取文件的大小   返回文件字节数
# res = os.path.getsize('./a/b/c/2.jpg')

# 检测是否是一个文件夹,是否存在
# res = os.path.isdir('')

# 检测文件是否存在  ***
# res = os.path.isfile('./6.内置模块-系统接口-os-2.py')   # True

# exists() **** 检测路径是否存在,既可以检测文件，也可以检测路径
# res = os.path.exists('')

# 检测两个path路径是否同时指向了一个目标位置（两个路径必须真实）
# a = './6.内置模块-系统接口-os-2.py'
# b = './6.内置模块-系统接口-os-2.py'
# res = os.path.samefile(a,b)

# 返回文件或文件夹的创建时间
# res = os.path.getctime('./6.内置模块-系统接口-os-2.py')

# 返回文件或文件夹的最后访问时间
# res = os.path.getatime('./6.内置模块-系统接口-os-2.py')

















































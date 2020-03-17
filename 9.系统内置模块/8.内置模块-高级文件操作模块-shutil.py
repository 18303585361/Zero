# 高级文件操作模块 shutil
import shutil

# 1.copy(文件的来源路径，文件的目标路径)  复制文件
# shutil.copy('./data.json','./a/da.json')

# 2.copy2 和 copy方法一样，可以拷贝文件到指定目录，保留了源文件的信息（操作时间和权限等）

# copyfile 拷贝文件的内容（打开文件，读取内容，写入到新的文件中）

# copytree()    可以把整个目录结构和文件全部拷贝到指定目录中
#               但是要求指定的目标文件夹必须不存在
# shutil.copytree('./a','./b')

# rmtree()      删除整个文件夹
# shutil.rmtree('./b')

# move()    移动文件或文件夹到指定目录，也可以用于修改文件或文件夹的名称
# shutil.move('./b','../abc')






















































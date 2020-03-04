# 文件操作的步骤和方式

# 写入文件操作
    ## 1.打开文件
    # fb = open('./1.txt','a',encoding='utf-8')
    ## 2.写入/读取文件
    # fb.write('\n你好')
    ## 3.关闭文件
    # fb.close()

# 读取文件操作
    ## 1. 打开文件
    # fb = open('./1.txt','r',encoding='utf-8')
    ## 2. 读取文件
    # res = fb.read()
    ## 3. 关闭文件
    # fb.close()
    # print(res)

# 文件操作的高级写法
'''
with open(文件路径，打开方式，字符集) as 变量:
    变量.操作()
'''
# r+ 既可读，又可写
# w+ 既可读，又可写    注意 w模式的特点，是打开文件后直接清空了文件
# a+ 既可读，又可写    追加写读
# x+ 异或
with open('./1.txt','a+',encoding='utf-8')as fp:

    # 设置指针的位置
    fp.seek(20)  # 设置当前指针的位置 seek(0) 最开始的位置
    fp.write('cc')
    fp.seek(0)

    res = fp.read()
    print(res)

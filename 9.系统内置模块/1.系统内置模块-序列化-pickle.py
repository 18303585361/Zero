# 系统内置模块
'''
系统内置模块就是安装python解释器后，系统给提供的模块
在需要时可以导入后使用。例如：json,re,os...
'''

## 序列化
'''
序列化
    1.指可以把 Python 中的数据，以文本或二进制的方式进行转换，并且还能反序列化为原来的数据
    2.文本序列化模块 json 
    3.二进制序列化模块 pickle
为什么需要序列化？
    一般情况，数据在程序与网络中进行传输和存储时，需要以更加方便的形式进行操作
    因此需要对数据进行序列化
    
'''
import pickle
### pickle 序列化
'''
pickle模块提供的函数
    dump(需要序列化的对象变量名，需要存放的文件名)  序列化，把一个数据对象进行序列化并写入到文件中
        1.dump() 在调用时需要填入参数。
            1.参数一为需要序列化的对象变量名
            2.参数二为需要存放的文件名
        2.调用格式：
            a = 1
            with open('文件路径','打开方式') as 文件变量名：
                pickle.dump(a,文件变量名)
    dumps() 序列化，可以把一个python的任意对象序列化成为一个二进制
        有返回值，需要变量接收 例如：a=1  res=pickle.dumps(a)
        可以转换任何数据类型的对象
    load()  反序列化，在一个文件中读取序列化的数据，并且完成一个反序列化
        1.load函数在调用时需要填入参数
            1.参数为打开的文件变量名
        2.调用格式：
            with open('文件路径','打开方式') as 文件变量名：
                pickle.load(文件变量名)
    loads() 反序列化，可以把一个序列化后的二进制数据反序列化为python的对象
        有返回值，需要变量接收 例如：a=1  res=pickle.loads(a)
        可以反序列化通过 dumps()函数序列化的二进制对象
    
'''
#### 基本的序列化与反序列化操作
##### dumps()的使用
# str1 = 'i love you'
# list1 = [1,2,3,4,5]
# dict1 = {'name':'张三','age':20,'sex':'m'}
# res1 = pickle.dumps(str1) #   b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\ni love you\x94.' <class 'bytes'>
# res2 = pickle.dumps(list1)  # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.' <class 'bytes'>
# res3 = pickle.dumps(dict1)  # b"\x80\x04\x95'\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x06\xe5\xbc\xa0\xe4\xb8\x89\x94\x8c\x03age\x94K\x14\x8c\x03sex\x94\x8c\x01m\x94u." <class 'bytes'>
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))

##### loads()的使用
# res_1 = pickle.loads(res1)
# res_2 = pickle.loads(res2)
# print(res_1,type(res_1))    # i love you <class 'str'>
# print(res_2,type(res_2))    # [1, 2, 3, 4, 5] <class 'list'>

#### 序列化与文件结合使用
'''
如何把一个python数据进行序列化后写入文件？并且再次读取出来？
使用 dump() load() 方法完成
'''
##### 序列化后存入文件的第一种方法
# dict1 = {'name':'张三','age':20,'sex':'m'}    # 1.定义数据
# res1 = pickle.dumps(dict1)  # 2.进行序列化
# with open('../-.test/pickle.txt','wb') as txt:    # 3.存入文件
#     txt.write(res1)
#     print(res1)
##### 把存有序列化数据的文件反序列化后再次存入的第一种方法
# with open('../-.test/pickle.txt','rb')  as txt:
#     res_1 = txt.read()
#     res_2 = pickle.loads(res_1)
#     print(res_2)

##### 序列化后存入文件的第二种方法
# dict1 = {'name':'张三','age':20,'sex':'m'}
# with open('../-.test/pickle1.txt','wb') as pickle1:
    # 在此处调用pickle模块的方法
    # pickle.dump(dict1,pickle1)
##### 把存有序列化数据的文件反序列化后再次存入的第二种方法
# dict1 = {'name':'张三','age':20,'sex':'m'}
# with open('../-.test/pickle1.txt','rb') as pickle1:
    # 在此处调用pickle模块的方法
#     newres = pickle.load(pickle1)
#     print(newres)
































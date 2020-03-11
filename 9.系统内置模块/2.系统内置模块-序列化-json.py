# 序列化模块 json
'''
什么是json？
    JSON (JavaScript Object Notation)
    JSON 是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式
    JSON 在js语言中是一个对象的表示方法，和Python中的字典的定义规则和语法都很像
    JSON 在互联网中又是一种通用的数据交换、数据传输、数据定义的一种数据格式

Python中提供的 json 模块，可以把一些符合转换的python数据对象，转为json格式的数据

可以转换的格式：
    字典类型、列表类型、元组类型、整型类型、字符串类型、浮点数类型
不可以转换的格式：
    集合类型

json 的方法：
    json.dumps()

    json.loads()

    json.dump() 写入文件

    json.load()

'''
import json
## 以下语法格式定义的是一个 字典 的数据类型
# dict1 = {'name':'admin','age':20,'sex':'男'}
# list1 = [1,2,3]
# str1 = '1234543'  # 只是转为了字符串
# int1 = 123453 # 只是转为了数字
set1 = {1,2,3,4,'1','a','b','c','c','d'}  # 集合不能转
print(set1,type(set1))
## 使用 json模块的 dumps方法进行 json格式的转换
res1 = json.dumps(set1)
print(res1,type(res1))

## 使用 json模块中的 loads方法进行反序列化
# res2 = json.loads(res1)
# print(res2,type(res2))


# dict1 = {'name':'admin','age':20,'sex':'男'}
# with open('../-.test/json1.txt','w') as json1:
#     json.dump(dict1,json1)
#
# with open('../-.test/json1.txt','r') as json1:
#     new = json.load(json1)
#     print(new)




















































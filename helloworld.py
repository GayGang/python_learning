#!/usr/bin/env python3

# 告诉解释器用 utf-8编码去读取源码,因为可能有中文
# -*- coding: utf-8 -*-
print("hello world again")

answer = 42
name = "DengXiaoBai"

print(answer)

#  ----------------print---------------
print('string1','string2','string3')
print(111.222222)
print('print can print number without \'\',like this:',1111)
print('print can print any var',3333,3232.1,-1232323)

# r''里面的内容不转义
print(r'///n//')
print(r'""""')

# '''...''' 表示多行内容
print('''第一行
第二行
第三行''')

# 地板除, 只会取整数部分, 结果一定是整形
print(11 // 3)

# / 结果一定是 浮点型, 即使两个能够除尽的整数
print(9 / 3)
print(11 / 3)


# --------------input-------------
# name=input('plz input your name:')
# print('your name {0}'.format(name))


# 对象概念的 test
# 在 OC/Swift 中, 基本数据类型是直接赋值的, 对象则是传递引用
# 在 py 中, 一切皆对象, 没有什么基本类型之分
testIntA = 22
testIntB = testIntA
testIntA = 33
print(testIntB)


# 布尔值 True / False




# --------------String------------
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

ord('中') #返回 unicode 编码对应的十进制数
chr(66)   #返回 unicode 编码十进制数对应的字符(串)

# bytes 类型, 类似 data 类型
# 中文用 utf8 encode / decode 英文用ascii encode / decode
# 一般统一使用 utf8, 因为 utf8兼容 ascii

chineseStr = "我要学习"
chineseBytes = chineseStr.encode('utf-8') # encode to bytes
decodeChinese = chineseBytes.decode('utf-8',errors='ignore') # decode to string, 'ignore'忽略下部分无效字节
charsCount = decodeChinese.__len__() # 字符数
bytesCount = chineseBytes.__len__()  # 字节数
print('str:{0},bytes:{1},decodeStr:{2},charsCount:{3},bytes:{4}'.format(chineseStr,chineseBytes,decodeChinese,charsCount,bytesCount))

enStr = "I'm learning py"
enBytes = enStr.encode('utf-8')
decodeEnStr = enBytes.decode('utf-8',errors='ignore')
enCharCount = enStr.__len__()
enBytesCount = enBytes.__len__()
print('str:{0},bytes:{1},decodeStr:{2},charsCount:{3},bytes:{4}'.format(enStr,enBytes,decodeEnStr,enCharCount,enBytesCount))

# 字符串格式化输出, 不知道什么类型就用字符串类型 %s
percentNum = (85 - 72) * 100 / 72
print('{0} 比去年多考了 {1:.1f}%'.format('小白', percentNum))


# Boolean and None


# if statement, using : replace {} enrolling block
# true and false values,just like OC
if 0:
    print("0 is true")
else:
    print("0 is false")

if 0 and 1:
    print("0 and 1 is true")

if 0 or 1:
    print("0 or 1 is true")

if not 0 and 1:
    print("0 and 1 is not true")



# for loops
# 实际上 range(arg1,arg2,arg3)会被转换成一个 List
for index in range(10):
    print("index is {0}".format(index))

print("--------")
for index in range(5, 10):
    print("index is {0}".format(index))

print("--------")

for index in range(5, 10, 2):
    print("index is {0}".format(index))

# Dictionary
# 为不存在的key 设置默认值,避免KeyError

student = {
    "name": "DengXiaoBai",
    "age": 11
}

print(student.get("last_name", "Idiot"))

# exceptions
try:
    lastName = student["aa"]
except KeyError:
    print("Error finding aa")
except TypeError as error:
    print("Type Error")
    print("error message same as not handled {0}".format(error))

except Exception:  # 不推荐这么做,因为我们总是想知道具体的exception
    print("handle all exceptions")


# Other Date Types


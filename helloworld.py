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
# None 和 False 不一样



# --------------String------------

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
print('空格:{0:4d},添0:{1:04d}'.format(22,22))


# ------------list 和 tuple-------------
# 元素可以是不同类型
# list : 有序的数组, 元素的指向是可以变的,即可变的
# tuple : 元素的指向是不能变的, 即不可变 , 如果想要定义一个完全不能变的 tuple, 那么他的元素也不能变化

firstList = ['Ford',3000,True]
# 操作
firstList.append('凯迪拉克')
firstList.insert(0,'通用')
popElement = firstList.pop()
print('popElement is {0}'.format(popElement))

popElement = firstList.pop(0)
print('popElement is {0}'.format(popElement))
print('the last element is %s' % firstList[-1])


firstTuple = ('Honda',2000,False)
secTuple = ('Mazzida',) # 定义单个元素的tuple 记得加上 ,
thrTuple = ('Club',['man_city',1])

print('the tuple is : {0}'.format(thrTuple))

# thrTuple[-1] = ['kdb'] 这个是不行的 TypeError: 'tuple' object does not support item assignment 意味着元素指向是不变的
thrTuple[-1][1] = 'Champion'
print('after changing the tuple is : {0}'.format(thrTuple))



# ------------if statement, using : replace {} enrolling block-----------
# true and false values,just like OC

if '':
    print('空字符串')
else:
    print('空字符是 False')

if []:
    print('空数组')
else:
    print('空数组是 False')

if ():
    print('空元组')
else:
    print('空元组是 False')

if None:
    print('None')
else:
    print('None是 False')



# --------------- for loops for x in range / list --------------
# 实际上 range(start,stop,interval) 从 start 开始(会等于 start),在 stop 前停止(不会等于 stop)
listFromRange = list(range(5,15,4))
print('list from range is :{0}'.format(listFromRange))

for index in range(4):
    print("index is {0}".format(index))
print("--------")

for index in range(1, 3):
    print("index is {0}".format(index))

print("--------")
for index in range(5, 10, 6):
    print("index is {0}".format(index))





# --------- Dictionary  Set ------------
# Dictionary : key-value, 空间换时间,因为既要存储key 也要存储 value
#              为了保证 hash 的正确性, key 一定要保证是不可变的.例如 String / Int
# set 无序 无重复的集合 , 为了保证元素的无重复性, 加入的元素一定要是不可变的
# 避免 KeyError

student = {
    "name": "DengXiaoBai",
    "age": 11
}

# 删除某个 key, 对应的 value 也会被删除
testKey = 'name'
student.pop(testKey)
print('after pop student is {0}'.format(student))
# 判断有没有这个 key

if testKey in student:
    print(student[testKey])

# 设置默认值 , 默认是 None
print('name is {0}'.format(student.get(testKey)))


# set 无序 无重复的集合 , 为了保证元素的无重复性, 加入的元素一定要是不可变的
set1 = set(['1',True,3333])  # 把里面的元素加入 set
set2 = set(('1',True,6666))
# set1.add(('KDB',['python'])) TypeError: unhashable type: 'list'

# 交集
print('交集: {0}'.format(set1 & set2))

# 合集
print('合集: {0}'.format(set1 | set2))
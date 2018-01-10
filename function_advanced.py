from collections import Iterable


# string 和 tuple 可以看成一种 list
# range(start, end, interval), 一定注意不包括 end

# slice
def trim(s):
  print('before: s is --{0}--'.format(s))
  while s[0] == ' ':
      count = len(s)
      s = s[1:count]

  while s[-1] == ' ':
      count = len(s)
      s = s[:count - 1]
      print('--{0}--'.format(s))

  print('after: s is --{0}--'.format(s))
  if s[0] == ' ' or s[-1] == ' ':
      print('FAILD')
  else:
      print('SUCCESS')


trim(' fffffff   hllow    fff')


# Iteration


if isinstance([1,2,3],Iterable): # 判断是否可迭代
    print('可迭代')


# 迭代时多个参数


for item in {'a': 'aaa', 'b': 'bbbb'}.items():
    print(item)

for index, value in enumerate([111, 222, 333]):
    print(index, value)

for x, y in [(1, 111), (2, 222), (3, 333)]:
    print( x, y)


# list comprehensions, 列表生成

l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [e.lower() for e in l1 if isinstance(e,str)]
print(l2)


# generator 生成器

def fib(top):
    n, a, b = 0, 0, 1
    while n < top:
        yield b    # 每次执行这里就返回, 下次执行从这里开始
        a, b = b, a + b
        n = n + 1
    return 'done'


g = fib(7)
while True:
    try:
        result = next(g)
        print('g:', result)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

for item in fib(7):
    print(item)


# Iterator 有序惰性数据流, 存储的是算法, 需要的时候才计算. 我们不知道它的长度
# Iterable 知道长度
# 可以把 Iterable -> Iterator
# 利用 isInstance 判断

l3 = [1, 2, 3, 4, 5]
i = iter(l3)
while True:
    try:
        print('value:', next(i))
    except StopIteration:
        break


for i in l3:
    print(i)

from functools import reduce

# map 把 fn 作用到集合的每一个元素上面, 返回一个新的 Iterator (集合)
# reduce 会把函数的结果 作为下一次的参数 传入, 返回新的值


def add(x, y):
    print('x:',x, 'y:', y)
    return x + y


reduce(add, [1, 3, 5, 7, 9])


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        print('x:', x, 'y:', y)
        return x * 10 + y

    def char2num(c):
        return DIGITS[c]

    return reduce(fn, list(map(char2num, s)))


print(str2int('14354253'))


def str2float(s):
    def pos_fn(x, y):
        return x * 10 + y

    def nag_fn(x, y):
        return x / 10 + y

    def char2int(c):
        return DIGITS[c]

    L = s.split('.')
    print(L[1][::-1]) # reverse a list
    # print and retrun
    return print(reduce(pos_fn, map(char2int, L[0])) + reduce(nag_fn, map(char2int, L[1][::-1])) / 10)


print(str2float('123.456'))


# TODO: 如果不知道是字符串, 难道就一定没有提示了????
def normalize(name):
    return name[0].upper() + name[1:].lower()


names = ['adam', 'LISA', 'barT']
print(list(map(normalize, names)))


def prod(l):
    def mul(x, y):
        return x * y
    return reduce(mul, l)


print(prod([1, 2, 3, 5]))


# filter

# 求素数
# 返回奇数的 generator
def _odd_iter():
    odd_num = 1
    while True:
        odd_num = odd_num + 2
        yield odd_num


def primes():
    yield 2
    it = _odd_iter()
    while True:
        p = next(it)
        yield p
        # 排除p的倍数
        it = filter(lambda x: x % p > 0, it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


# sort 排序


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print(sorted(students, key=by_score))
print(sorted(students, key=by_name))


# 函数作为返回值
# 最好不要引用之后会变的参数, 因为不知道什么时候会调用返回的函数


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


fs = count()
print(fs[0](), fs[1](), fs[2]())


def diff_count():
    fs = []

    def g(j):
        def f():
            return j * j
        return f

    for i in range(1, 4):
        fs.append(g(i))
    return fs


fs2 = diff_count()
print(fs2[0](), fs2[1](), fs2[2]())


# 装饰器, 用来拓展函数
def log(func):
    def wrapper(*args, **kw):
        print('call begin: %s():' % func.__name__)
        result = func(*args, **kw)
        print('call end: %s():' % func.__name__)
        return result
    return wrapper


@log
def test():
    print('I\'m testing!!!')


test()



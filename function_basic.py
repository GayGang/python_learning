
# 函数定义
# 函数即使没有返回值, 执行完会自动返回 return None, 可以直接简写成 return
# 自定义函数不会自动做参数检查,要自己处理


def hello_function(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    print('输入的参数是:{0}'.format(x))


# 空函数, 占位函数


def nothing():
    pass


hello_function(333)


# ## 各种参数顺序如下# ###


# 位置参数


# 默认参数 , 位置和定义的时候一样是可以省略参数名, 如果不一样的时候要写参数名. value 一定要是不可变的类型, 否则每次调用默认值都会改变

# wrong usage
def add_end(l=[]):
    l.append('end')
    return l


print('wrong result is : {0}'.format(add_end()))
print('wrong result is : {0}'.format(add_end()))
print('wrong result is : {0}'.format(add_end()))


# normal usage, using string / None as default value
def add_end_right(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print('right result is : {0}'.format(add_end_right()))
print('right result is : {0}'.format(add_end_right()))
print('right result is : {0}'.format(add_end_right()))


# 可变参数, *args,函数内部自动转为tuple. 传参数的时候可以一个一个传, 也可以*tuple/*list, 相当于把所有的元素当做参数一个一个传入进去


# 命名关键字参数, *, arg1, arg2. 前面有 * 隔开  如果前面跟的是*args 的话可以省略 * , 可以设置默认值
def person(name, age, *args, job='programmer', hometown='GanZhou'):
    print('name:{0}, age:{1}, other:{2}, job:{3}, hometown:{4}'.format(name, age, args, job, hometown))


person('XiaoBai', 26, 'football')


# 关键字参数, **kw. 参数名和 value 都是自己定义. 内部自动转换为 dict. 可以一个一个参数传入, 可以**dict, 相当于 copy 一份 dict


# 因为这些规则, 所有的函数都可以通过 fuction_name(*args, **kw)来调用, 参数一个一个排列进去


def f1(a, b, c=0, *args, **kwargs):
    print('a:{0}, b:{1}, c:{2}, args:{3}, kwargs:{4}'.format(a, b, c, args, kwargs))


args_tuple = ('aaaa', 'bbbb', 666, 'focus')
short_tuple = ('aaaaa')  # 如果传入的是 string, 参数不够会把string 拆分
kwargs_dict = {'name':'XiaoBai', 'hobby':'football'}
f1(*args_tuple, **kwargs_dict)
f1(*short_tuple, **kwargs_dict)
from types import MethodType


class Student(object):
    name = "STUDENT"


sa = Student()
sb = Student()
print('name of sa :{0}, name of sb: {1}, name of Student: {2}'.format(sa.name, sb.name, Student.name))


# 增加了一个实例属性, 并不是类属性, 可以为实例增加任意属性
# sa.name = 'sa STUDENT'
Student.name = 'CANGED'
print('name of sa :{0}, name of sb: {1}, name of Student: {2}'.format(sa.name, sb.name, Student.name))


# 动态给某一个实例绑定方法, 对别的实例不起作用
def set_sex(self, s):
    self.sex = s
    print(s)


sa.set_sex = MethodType(set_sex, sa)
sa.set_sex('male')


# 动态给类绑定方法, 所有实例都可以用. 相当于在 class 声明
def set_score(self, score):
    self.score = score
    print(score)


Student.set_score = set_score
sa.set_score(100)
sb.set_score(11)


# __slots__ 限制实例属性添加, 值对本类的实例起作用
class TestClass(object):
    __slots__ = ('name')


# 如果子类也有 __slots__ ,包括了父类的
class TestClass2(TestClass):
    __slots__ = ('score')


ts = TestClass()
ts.name = 'HHHHHH'

ts2 = TestClass2()
ts2.name = 'JJJJJJ'


# @property, 把方法变为属性调用, 相当于 getter/setter
class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


    @property
    def resolution(self):
        return self.__width / self.__height


screen = Screen()
screen.height = 667
screen.width = 375
print(screen.resolution)


# python 中的多类继承,用来给类添加额外的功能.
# 继承主线不变, 通过 mixIn 类类增加功能
# mixIn 功能类似 Swift/OC 中的协议


# override 已有的方法
class TestClass3(object):
    # 如果自定义该方法, 调用没有的属性/方法, 会默认返回 None
    # 只有当没有被调用的属性和方法时, 才会调用该方法
    # 可以用该方法实现动态链式调用
    def __getattr__(self, item):
        if item == 'score':
            return 100


ts3 = TestClass3()
print(ts3.score)
print(ts3.hh)


class Chain(object):
    def __init__(self, path = 'http://api.server'):
        self.path = path

    def __getattr__(self, path):
        return Chain('{0}/{1}'.format(self.path, path))

    # 自定义打印, 调用 print 的时候调用
    def __str__(self):
        return self.path

    __repr__ = __str__


# http://api.server/user/friends
# http://api.server/user/timeline/list
chain = Chain()
print(chain.user.timeline.list)


# 实现 __iter__() , __next__() 用于 for in loops
# __getItem__(), 用于下标取值, key 取值, slice
# __call__(), 直接是对对象进行调用



# 枚举
from enum import Enum, unique


# 从1 开始赋值
Month = Enum('Month',
             ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 自定义, 成员直接比较


@unique
class Workday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Workday.Sun)
print(Workday.Sun.value)
print(Workday(0))
print(Workday['Sun'])

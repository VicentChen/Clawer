# ============================
# ----- Input and Output -----
# ============================

# ===== Notes =====
# Python会自动为','分隔的内容添加' '
# 与Python2不同，未添加'#-*- coding:utf-8 -*-'也能够正常输出中文
# Python3中默认使用Unicode进行编码
# 
# Python输入时会对程序进行阻塞
# Python输入的值为字符串
# 
# Python不支持数字与字符串相加
# =================

# ##### Output Literials #####
"""
print("Hello, World") # OUTPUT: Hello, World
print("Hello", "World") # OUTPUT: Hello World
print("Hello" + "World") # OUTPUT: HelloWorld
print("你好") # OUTPUT: 你好
print(100 + 200) # OUTPUT: 300
"""

# ##### Input #####
"""
name = input()
print("Hello", name) # OUTPUT: Hello %name%
number = input()
print("Hello" + number) # OUTPUT: Hello%number%
"""

# ##### Errors #####
# 
# OUTPUT: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(100 + 200 + "Number: Hello") 
# 
# OUTPUT: TypeError: must be str, not int
# number = input()
# print("Hello" + number) # OUTPUT: Hello%number%
#

# -------------------------------------------------------------------------------------

# =================
# ----- Basis -----
# =================

# ===== Notes =====
# Python中字符串可以用''或""表示
# 禁用转义: r'' r""
# 
# Python中变量无固定类型(弱类型)
# 
# Python中仅会人为大写变量名当作常量
# =================

# ##### Types #####
"""
print('"Hello World!"') # OUTPUT："Hello World!"
print("'Hello World!'") # OUTPUT: 'Hello World!'
print('\'Hello World!\'') # OUTPUT: 'Hello World!'
print(r'\'Hello World!\'') # OUTPUT: \'Hello World!\'
print('''
=====line1=====
=====line2=====
=====line3=====
''') # OUTPUT is 3 lines
print(1 == 1) # OUTPUT: True
print(1 == 2) # OUTPUT: False
"""

# ##### Variables #####
"""
var1 = 1
print(var1) # OUTPUT: 1
var1 = "str"
print(var1) # OUTPUT: str
print(var1[:1]) # OUTPUT: s
print(var1[1:]) # OUTPUT: tr
var2 = var1
var1 = "new str"
print(var1) # OUTPUT: new str
print(var2) # OUTPUT: str
PI = 3.1415926535
print(PI)
"""

# ##### Operations #####
"""
print(10 / 3)
print(10 // 3)
"""

# ===============================
# ----- String and Encoding -----
# ===============================

# ***** 此处以Unicode进行编码，UTF-8编码输出的值会有所不同 *****

# ===== Notes =====
# Python3默认以Unicode进行编码
# len(str)可用于计算字符串中的字符个数
# 使用%后字符才会被转义
# %格式化字符串会对数字长度自动要求
# format格式化字符串对数字长度无要求
# 
# decode('utf-8', errors="ignore") 可忽略解码错误 
# =================

# ##### String #####
"""
print(ord("A")) # OUTPUT: 65
print(ord("中")) # OUTPUT: 20013
print(chr(65)) # OUTPUT: A
print(chr(20013)) # OUTPUT: 中
print(b"ABC") # OUTPUT: b'ABC'
print(len(b"ABC")) # OUTPUT: 3
print(len("ABC")) # OUTPUT: 3
print(len("中文")) # OUTPUT: 2
"""

# ##### Encoding #####
"""
print("ABC".encode("ascii")) # OUTPUT: b'ABC'
print("ABC".encode("utf-8")) # OUTPUT: b'ABC'
print("中文".encode("utf-8")) # OUTPUT: b'\xe4\xb8\xad\xe6\x96\x87'
print(b"ABC".decode("utf-8")) # OUTPUT: ABC
print(b"ABC".decode("ascii")) # OUTPUT: ABC
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8")) # OUTPUT: 中文
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors="ignore")) # OUTPUT: 中
"""

# ##### Format #####
"""
print("Hello %% %s X %d = %f" % ("World", 10, 3.1415926)) # OUTPUT: Hello % World X 10 = 3.141593
print("Hello %% {0} X {1} = {2}".format("World", 10, 3.1415926)) # OUTPUT: Hello %% World X 10 = 3.1415926
"""

# ===== Errors =====
# print(ord("中文")) # OUTPUT: TypeError: ord() expected a character, but string of length 2 found
# str = b"中文" # OUTPUT: SyntaxError: bytes can only contain ASCII literal characters.
# "中文".encode("ascii") # OUTPUT: UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# print(b"\xe4\xb8\xad\xe6\x96\x87".decode("ascii")) # OUTPUT: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
# print(b'\xe4\xb8\xad\xff'.decode('utf-8')) # OUTPUT: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte

# ==========================
# ----- List and Tuple -----
# ==========================

# ===== Notes =====
# 索引为负数时逆序输出
# 索引为负数时计数由-1开始
# 推测append()无返回值
# insert()将插入在元素前面，可以将index理解为插入后的位置
# pop() 将pop最后一个元素，或者pop索引的元素
# list中可以包含不同的元素
# list中可以进行嵌套，[a][b]可以理解为: 获取list中第a个元素，获取第a个元素中第b个元素
#
# Tuple初始化后不可修改
# 元素获取方法与List一致
# Tuple中仅含一个元素必须如下定义: (x, )
# 可以用x, y = Tuple进行赋值, List亦如此
# =================

# ##### List #####
"""
print(["Vicent", "_", "Chen"]) # OUTPUT: ['Vicent', '_', 'Chen']
print(len(["Vicent", "_", "Chen"])) # OUTPUT: 3
print(["Vicent", "_", "Chen"][0]) # OUTPUT: Vicent
print(["Vicent", "_", "Chen"][-1]) # OUTPUT: Chen
print(["Vicent", "_", "Chen"][-3]) # OUTPUT: Vicent

username = ["Vicent", "_", "Chen"]
username.append("@yeah.net")
print(username) # OUTPUT: ['Vicent', '_', 'Chen', '@yeah.net']
print(["Vicent", "_", "Chen"].append("@yeah.net")) # OUTPUT: None
username.insert(2, "###")
print(username) # OUTPUT: ['Vicent', '_', '###', 'Chen', '@yeah.net']
print(username.pop()) # OUTPUT: @yeah.net
print(username.pop(2)) # OUTPUT: ###
print(username) # OUTPUT: ['Vicent', '_', 'Chen']
username[1] = "@"
print(username) # OUTPUT: ['Vicent', '@', 'Chen']

varylist = ["Vicent", "_", "Chen", "@", 163, ".com"]
print(varylist) # OUTPUT: ['Vicent', '_', 'Chen', '@', 163, '.com']
print(len(["Vicent", "_", "Chen", "@", ["163.com", "126.com", "yeah.net"]])) # OUTPUT: 5
print(["Vicent", "_", "Chen", "@", [["163", "126"], ".com", "yeah.net"]][4][0][1]) #OUTPUT: 126
"""

# ##### Tuple #####
"""
print(("Vicent", "_", "Chen")) # OUTPUT: ('Vicent', '_', 'Chen')
print(("Vicent", "_", "Chen")[0]) # OUTPUT: Vicent
print(("Vicent", "_", "Chen")[-3]) # OUTPUT: Vicent
print((1)) # OUTPUT: 1
print((1, )) # OUTPUT: (1,)
x, y = (-0.5328330203333975, -0.8462204041751706)
print(x, y) # OUTPUT: -0.5328330203333975 -0.8462204041751706
"""

# ##### Errors #####
# print(["Vicent", "_", "Chen"][-4]) # OUTPUT: IndexError: list index out of range
# print(["Vicent", "_", "Chen"][3]) # OUTPUT: IndexError: list index out of range
# print(("Vicent", "_", "Chen")[-4]) # OUTPUT: IndexError: tuple index out of range
# print(("Vicent", "_", "Chen")[3]) # OUTPUT: IndexError: tuple index out of range

# =====================
# ----- Condition -----
# =====================

# ===== Notes =====
# Python使用缩进判断代码块
# if, else后记得添加':'
#
# int() 可用于parse整数
# =================

# ##### If #####
"""
if 10 > 20: # OUTPUT: Normal World
    print("Crazy World")
elif 10 > 15:
    print("Another Crazy World")
else:
    print("Normal World")

# ##### Input #####
num = int(input("Input a number"))
if num > 10:
    print("Good Boy")
else:
    print("Good Girl")
"""

# ================
# ----- Loop -----
# ================

# ===== Notes =====
# =================

# ##### Loop #####
"""
username = ["Vicent", "_", "Chen"]
# OUTPUT: 
#   Vicent
#   _
#   Chen
for fragment in username:
    print(fragment)
print(range(10)) # OUTPUT: range(0, 10)

# OUTPUT is 0 to 9
for i in range(10):
    print(i)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n -= 1
print(sum) # OUTPUT: 4950
# ignore break and continue
"""

# ========================
# ----- Dict and Set -----
# ========================

# ===== Notes =====
# get()第二个参数可用于返回查找失败时的值
# 
# Set 自动过滤重复元素
# =================

# ##### Dict #####
"""
d = {"Vicent": 1, "_": 0, "Chen": 5}
print(d) # OUTPUT: {"Vicent": 1, "_": 0, "Chen": 5}
print(d["Vicent"]) # OUTPUT: 1
print(d.get("_")) # OUTPUT: 0
print(d.get("Unknown", "Chen")) # OUTPUT: Chen
print(d.pop("_")) # OUTPUT: 0
print(d) # OUTPUT: {'Vicent': 1, 'Chen': 5}
"""

# ##### Set #####
"""
print(set([1, 2, 3])) # OUTPUT: {1, 2, 3}
print(set([1, 2, 3, 3, 4, 2, 2, 1, 1]))  # OUTPUT: {1, 2, 3, 4}
print(set([1, 2]) & set([2, 3])) # OUTPUT: {2}
print(set([1, 2]) | set([2, 3])) # OUTPUT: {1, 2, 3}
print(set([1, 2]) - set([2, 3])) # OUTPUT: {1}
"""

# ##### Errors #####
# print(d["Unknown"]) # OUTPUT: KeyError: 'Unknown'

# -------------------------------------------------------------------------------------

# ====================
# ----- Function -----
# ====================

# ===== Notes =====
# 发生错误后若不进行处理会使程序直接中断
# Python可返回多个值
# import不强制放在头部
# 多次import不会报错
#
# 默认参数必须指向不变对象
# 可变参数理解为Tuple
# 为可变参数传入一个List或Tuple等价于传入一个List或Tuple作为参数，即参数个数为1
#
# 关键字参数在函数内部自动组装成为dict
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# =================

# ##### Library #####
"""
print(abs(-100)) # OUTPUT: 100
print(hex(100)) # OUTPUT: 0x64
"""

# ##### Define Functinos #####
"""
import math
def printHello(num):
    if not isinstance(num, int):
        raise TypeError("num must be int")
    if num > 10: 
        print("Hello")
    else:
        pass
    return num
num = int(input("Input a number"))
print(printHello(num)) # OUTPUT: (Hello\n) %num%

def multiReturn(x):
    if not isinstance(x, (int, float)):
        raise TypeError("X must be int or float")
    return math.cos(x), math.sin(x), x
print(multiReturn(num)) # OUTPUT: (%cos(num)%, %sin(num)%, %num%)
"""

# ##### Parameters #####
"""
import math
def defaultValue(x = 2):
    print(x)
defaultValue() # OUTPUT: 2
defaultValue(3) # OUTPUT: 3

def errorDefaultValue(L = []):
    L.append("END")
    print(L)
errorDefaultValue([1,2,3]) # OUTPUT: [1, 2, 3, 'END']
errorDefaultValue() # OUTPUT: ['END']
errorDefaultValue() # OUTPUT: ['END', 'END']

def varyValue(*nums):
    print(nums)

varyValue(1,2,3) # OUTPUT: (1, 2, 3)
varyValue((1,2,3)) # OUTPUT: ((1, 2, 3),)
varyValue(*[2,3,4]) # OUTPUT: (2, 3, 4)

def keyWordValue(**kw):
    print(kw)
keyWordValue(Vicent=1, Chen=3) # OUTPUT: {'Vicent': 1, 'Chen': 3}
"""

# ##### Recursive #####
# ignore

# ##### Errors #####
# print(int("1.2345")) # OUTPUT: ValueError: invalid literal for int() with base 10: '1.2345'
# print(printHello("10")) # OUTPUT: TypeError: num must be int
# keyWordValue("Vicent", 1, "Chen", 3) # OUTPUT: TypeError: keyWordValue() takes 0 positional arguments but 4 were given
# keyWordValue("Vicent"=1, "Chen"=3) # OUTPUT: SyntaxError: keyword can't be an expression

# -------------------------------------------------------------------------------------

# ====================
# ----- Features -----
# ====================

# ===== Notes =====
# Slicing末端参数不会被访问
# 字符串亦可被切片
# 
# enumerate()返回可迭代元素的索引与值
#
# 列表生成器理解为循环
#
# 生成器不一次性计算所有值，在访问时才进行计算
# yield会将函数停止在当前位置
# =================

# ##### Slicing #####
"""
print(["Vicent", "_", "Chen", "@", "yeah.net"][0:]) # OUTPUT: ['Vicent', '_', 'Chen', '@', 'yeah.net']
print(["Vicent", "_", "Chen", "@", "yeah.net"][0:3]) # OUTPUT: ['Vicent', '_', 'Chen']
print(["Vicent", "_", "Chen", "@", "yeah.net"][-5:-2]) # OUTPUT: ['Vicent', '_', 'Chen']
print("Vicent_Chen@yeah.net"[:11]) # OUTPUT: Vicent_Chen
"""
# ##### Iteration #####
"""
for index, value in enumerate(["A", "B", "C"]):
    print(index, ":", value) # OUTPUT: %index% : %value%
"""

# ##### List Generator #####
"""
print([x*x for x in range(10)]) # OUTPUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# OUTPUT: [0, 0, 0, 0, 0, 2, 6, 10, 14, 18, 4, 12, 20, 28, 36, 6, 18, 30, 42, 54, 8, 24, 40, 56, 72]
print([x*y for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0])
"""
# ##### Generator #####
"""
g = (x*x for x in range(3))
for i in range(3):
    print(next(g)) # OUTPUT: %i*i%
ng = (x*x for x in range(3))
for i in ng:
    print(i) # OUTPUT: %i*i%

def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
for num in fib(3):
    print(num) # OUTPUT: 1\n 2\n 3
"""

# ##### Iterator #####
# ignore

# ##### Errrors #####
# print(next(g)) # OUTPUT: StopIteration

# -------------------------------------------------------------------------------------

# ==================================
# ----- Funcitonal Programming -----
# ==================================

# ===== Notes =====
# map(f, l): 将f作用于l上
# reduce(f, l): 依次调用f，最终返回一个值
#
# 偏函数用于设定参数默认值
# =================

# ##### High-order Function #####
"""
from functools import reduce
print(list(map(abs, [-4, 7, -8, 2, -5, 1]))) # OUTPUT: [4, 7, 8, 2, 5, 1]
print(reduce(min, [4, 7, 8, 2, 5, 1])) # OUTPUT: 1

def N():
    n = 1
    while True:
        n += 2
        yield n

def F(x):
    return lambda x: x % n > 0

def R():
    yield 2

    it = N()
    while True:
        n = next(it)
        yield n
        it = filter(F(n), it)

for n in R():
    if n < 20:
        print(n)
    else:
        break
"""

# ##### Closure #####
"""
def lazySum(a, b):
    def sum(x):
        return a*x+b
    return sum
f = lazySum(1, 2)
print(f(3)) # OUTPUT: 5
"""

# ##### Lambda #####
"""
f = lambda x : x * x
print(f(3)) # OUTPUT: 9
"""

# ##### Decorator #####
"""
def log(func):
    def wrapper(*args, **kw):
        print("%s" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def function():
    print("2018-4-6")

function()
"""

# ###### Partial #####
"""
import functools
int2 = functools.partial(int, base=2)
print(int2("10101010"))
"""

# -------------------------------------------------------------------------------------

# ==================================
# ----- Funcitonal Programming -----
# ==================================

# ===== Notes =====
# =================

# -------------------------------------------------------------------------------------

# =======================================
# ----- Object Oriented Programming -----
# =======================================

# ===== Notes =====
# 所有类继承自Object类
# 类中的方法会自动传入self
# 正常函数名与变量为public, __xxx__为特殊变量, _xxx/__xxx为private
# 实例的变量名如果以__开头，就变成了一个私有变量(private)
# 实例的变量名如果以_开头，提示用户将其当作私有变量
# 私有变量仍然可以访问 obj._Clz__privateVar
# 
# dir() 可用于获取对象的所有属性和方法
#
# 不使用self为属性赋值即为类属性
# 类属性与对象属性名字相同时，对象属性覆盖类属性
#
# 为一个实例绑定的对象和方法对另一个实例不起作用
# =================

# ##### Class ######
"""
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__privateVar = 100.0
    
    def printScore(self):
        print(self.name, self.score)
    
    def printPrivate(self):
        print(self.name, self.score, self.__privateVar)

student = Student("Vicent_Chen", 100)
print(student.name, student.score) # OUTPUT: Vicent_Chen 100
student.printScore() # OUTPUT: Vicent_Chen 100
student.printPrivate() # OUTPUT: Vicent_Chen 100 100.0
print(student._Student__privateVar) # OUTPUT: 100.0
"""

# ##### Inheritance #####
"""
class Clazz():
    def toString(self):
        print("Origin Class")
class GoodClass(Clazz):
    def toString(self):
        print("Good Class")
goodClass = GoodClass()
goodClass.toString() # OUTPUT: Good Class
"""

# ##### Access #####
"""
class People(object):
    pass
class Student(People):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__privateVar = 100.0
    def toString(self):
        print(self.name, self.score)
    def toStringWithPrivate(self):
        print(self.name, self.score, self.__privateVar)
student = Student("Vicent_Chen", 100)
print(type(1234)) # OUTPUT: <class 'int'>
print(type(student)) # OUTPUT: <class '__main__.Student'>
print(type(student) == Student) # OUTPUT: True
print(dir(student)) # OUTPUT: ['_Student__privateVar', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'score', 'toString', 'toStringWithPrivate']

print(hasattr(student, "NO")) # OUTPUT: False
setattr(student, "NO", "NO")
print(hasattr(student, "NO")) # OUTPUT: True
print(getattr(student, "NO")) # OUTPUT: NO
"""

# ##### Property #####
"""
class Student(object):
    name = "Student"
student = Student()
print(Student.name) # OUTPUT: Student
print(student.name) # OUTPUT: Student
student.name = "Vicent"
print(Student.name) # OUTPUT: Student
print(student.name) # OUTPUT: Vicent
Student.name = "Chen"
print(Student.name) # OUTPUT: Chen
print(student.name) # OUTPUT: Vicent
"""

# ##### Errors #####
# print(student.__privateVar) # OUTPUT: AttributeError: 'Student' object has no attribute '__privateVar'
# print(student.NoSuch) # OUTPUT: AttributeError: 'Student' object has no attribute 'NoSuch'

# -------------------------------------------------------------------------------------

# ===============================================
# ----- Advance Object Oriented Programming -----
# ===============================================

# ===== Notes =====
# __slots__用于限制能够添加至类中的属性
# __slots__对继承的子类不起作用
# 若子类中亦有__slots__语句，子类可添加的属性=父类可添加属性+语句中规定属性
#
# @property 将方法变成属性进行使用(此方法为getter)
# @%name%.setter 为转变后的属性的setter
# 事实上%name%应为有@property装饰器的方法的名字，实际get/set的属性可以不为score
#
# __str__()输出用户字符串，__repr__()输出程序开发者字符串
#
# __getattr__()仅在未找到属性时调用
#
# __call__()用于调用实例方法
# 
# type() 可用于获取类型，也可用于创建新的类型
#
# MetaClass总以MetaClass结尾以表示其为MetaClass
# =================

# ##### __slots__ #####
"""
class People(object):
    __slots__ = ("ID")
class Student(People):
    __slots__ = ("name", "age")
    pass
class Primary(Student):
    pass
student = Student()
student.ID = "123456"
primary = Primary()
primary.GG = "GG"
"""

# ##### @property #####
"""
class Student(object):
    @property
    def score(self):
        return self.__gg
    
    @score.setter
    def score(self, score):
        self.__gg = score

student = Student()
student.score = 1000
print(student.score) # OUTPUT: 
"""
# ##### Multi-Inherit #####
# ignore

# ##### Customize #####
"""
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    __repr__ = __str__
    def __iter__(self):
        return self
    def __getattr__(self, attr):
        return 100
    def __call__(self):
        print("Hello" + self.name)
print(Student("Vicent_Chen")) # OUTPUT: Vicent_Chen
print(getattr(Student("Vicent"), "name")) # OUTPUT: 100
print(getattr(Student("Vicent"), "score")) # OUTPUT: 100
Student("Vicent_Chen")() # OUTPUT: HelloVicent_Chen

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if (self.a > 1000):
            raise StopIteration("A > 1000")
        return self.a
    def __getitem__(self, n):
        if isinstance(n, slice):
            start, stop = n.start, n.stop
            a, b = 0, 1
            L = []
            for i in range(n.start):
                a, b = b, a + b
            for i in range(n.stop - n.start):
                L.append(a)
                a, b = b, a + b
            return L

        if isinstance(n, int):
            a, b = 0, 1
            for x in range(n):
                a, b = b, a + b
            return a

for num in Fib():
    print(num) # OUTPUT is Fib array
print(Fib()[10]) # OUTPUT: 55
print(Fib()[1:5]) # OUTPUT: 
"""

# ##### Enumrate #####
"""
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Apr) # OUTPUT: Month.Apr
print(Month.Apr.value) # OUTPUT: 4
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)
"""

# ##### Meta Class #####
"""
def f(self, name="World"):
    print("Hello", name)
Hello = type("Hello", (object, ), dict(hello=f))
Hello().hello() # OUTPUT: Hello World
print(type(Hello)) # OUTPUT: <class 'type'>
print(type(Hello())) # OUTPUT: <class '__main__.Hello'>

class Field(object):
    def __init__(self, name, columnType):
        self.name = name
        self.columnType = columnType
    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name=="Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found model : %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value;
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "INSERT INTO %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
"""

# ##### Errors #####
# student.score = 100 # OUTPUT: AttributeError: 'Student' object has no attribute 'score'

# -------------------------------------------------------------------------------------

# ==============
# ----- IO -----
# ==============

# ===== Notes =====
# VSCode下Python文件运行于.vscode同级目录下
#
# StringIO用于在内存中写字符串
# BytesIO 用于在内存中操作Bytes
#
# uname()函数在Windows上不提供
# os模块相关
# os.path.join()可正确处理不同操作系统的路径分隔符
# shutil提供copyfile()函数
#
# 序列化：把变量从内存中编程可存储或传输的过程
# Python中的序列化依赖于方法实现
# =================

# ##### File #####
"""
try:
    file = open("Readme.md", "r", encoding="utf-8")
    print(file.read()) # OUTPUT is content in Readme.md
finally:
    file.close()

with open("Readme.md", "r", encoding="utf-8") as file:
    print(file.read()) # OUTPUT is content in Readme.md

# ignore binary read, wirte and text write
"""

# ##### StringIO and BytesIO #####
"""
from io import StringIO
str = StringIO()
print(str.write("Hello")) # OUTPUT: 5
print(str.write(" World!")) # OUTPUT: 7 
print(str.getvalue()) # OUTPUT: Hello World!

str = StringIO("Hello \n World! \n")
for line in str.readlines():
    print(line.strip())

# ignore BytesIO
"""

# ##### File and Directory #####
"""
import os
print(os.name) # OUTPUT: "nt"
print(os.environ) # OUTPUT is all environments in dict(?)
print(os.path.abspath(".")) # OUTPUT is current absolute path of %Clawer%
print(os.path.join(".", "osTest")) # OUTPUT: .\osTest
print(os.path.splitext("C:\\path\\to\\osTest.text")) # OUTPUT: ('C:\\path\\to\\osTest', '.text')

print([x for x in os.listdir(".") if os.path.isdir(x)]) # OUTPUT: ['.git', '.vscode', 'Learn']
print([x for x in os.listdir(".") if os.path.isfile(x)]) # OUTPUT: ['.gitignore', 'Readme.md']
"""

# ##### Serialize #####
"""
import pickle
obj = dict(name="Vicent", age=20, score=38)
print(pickle.dumps(obj)) # OUTPUT: b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00Vicentq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04K&u.'
reObj = pickle.loads(pickle.dumps(obj))
print(reObj) # OUTPUT: {'name': 'Vicent', 'age': 20, 'score': 38}

import json
print(json.dumps(obj)) # OUTPUT: {"name": "Vicent", "age": 20, "score": 38}
print(json.dumps(["Vicent", "_", "Chen"])) # OUTPUT: ["Vicent", "_", "Chen"]

class Student(object):
    def __init__(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends
student = Student("Vicent_Chen", 100, ["V", "Vic", "Vicent"])
print(json.dumps(student, default=lambda obj: obj.__dict__)) # OUTPUT: {"name": "Vicent_Chen", "age": 100, "friends": ["V", "Vic", "Vicent"]}
def dict2Student(d):
    return Student(d["name"], d["age"], d["friends"])
print(json.loads('{"name": "Vicent_Chen", "age": 100, "friends": ["V", "Vic", "Vicent"]}', object_hook=dict2Student)) # OUTPUT: <__main__.Student object at 0x05E97D50>
"""

# ##### Errors #####
# file = open("../Readme.md", "r")  # OUTPUT: FileNotFoundError: [Errno 2] No such file or directory: '../Readme.md'
# print(os.uname()) # OUTPUT: AttributeError: module 'os' has no attribute 'uname'

# -------------------------------------------------------------------------------------

# ==============================
# ----- Process and Thread -----
# ==============================

# ===== Notes =====
# fork()仅在类UNIX下生效
# 推测Python多进程会将当前进程完全复制并运行
# Pool在join()之前必须close()
# queue可用于进程间通信
# =================

# ##### MultiProcessing #####
"""
from multiprocessing import Process
import os
# print("Process %s" % os.getpid()) # OUTPUT: Process 12548 / Process 38092
# 
# def runProcess(name):
#     print("Child Process %s - %s" % (name, os.getpid())) # OUTPUT: Child Process child-1 - 38092
# 
# if __name__ == "__main__":
#     print("Parent Process Parent - %s" % os.getpid()) # OUTPUT: Parent Process Parent - 12548
#     p = Process(target=runProcess, args=("child",))
#     p.start()
#     p.join()

from multiprocessing import Pool
import time, random

def longProcess(name):
    print("Child Process %s - %s" % (name, os.getpid())) # OUTPUT: Child Process %name% - %pid%
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Child Process %s - %s : %0.2fs" % (name, os.getpid(), end - start)) # OUTPUT: Child Process %name% - %pid% : %time%

if __name__ == "__main__":
    print("Parent Process Parent - %s" % os.getpid()) # OUTPUT: Parent Process Parent - %pid%
    p = Pool(4)
    for i in range(5):
        p.apply_async(longProcess, args=(i,))
    p.close()
    p.join()

import subprocess
print(subprocess.call(["nslookup", "www.baidu.com"])) # OUTPUT: 0

# ignore queue
"""

# ##### MultiThread #####
"""
import time, threading
def loop():
    print("Thread %s" % threading.current_thread().name) # OUTPUT: Thread LoopThread
    for i in range(5):
        print("Thread %s >> %d" % (threading.current_thread().name, i)) # OUTPUT is loop
print("Thread %s" % threading.current_thread().name) # OUTPUT: Thread MainThread
thread = threading.Thread(target=loop, name="LoopThread")
thread.start()
thread.join()

count = 0
lock = threading.Lock()
def lockThread():
    for i in range(10000):
        lock.acquire()
        try:
            global count
            count = count + 1
        finally:
            lock.release()
thread1 = threading.Thread(target=lockThread)
thread2 = threading.Thread(target=lockThread)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(count) # OUTPUT: 20000
"""

# ##### ThreadLocal #####
"""
import threading
localVar = threading.local()

def threadF(name):
    localVar.student = name
    print("%s %s" % (threading.current_thread().name, name))

t1 = threading.Thread(target=threadF, args=("Vicent",), name="ThreadA")
t2 = threading.Thread(target=threadF, args=("Chen",), name="ThreadB")
t1.start() # OUTPUT: ThreadA Vicent
t2.start() # OUTPUT: ThreadB Chen
t1.join()
t2.join()
"""

# -------------------------------------------------------------------------------------

# ====================
# ----- Database -----
# ====================

# ===== Notes =====
# =================

# ##### MySQL #####
import mysql.connector

# TODO: change info
conn = mysql.connector.connect(user="root", password="Vicent960829", database="dull_ip_pool")
cursor = conn.cursor()
cursor.execute("SELECT * FROM user_agent")
values = cursor.fetchall()
print(len(values))
conn.commit()
cursor.close()
conn.close()
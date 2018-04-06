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


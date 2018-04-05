# ============================
# ----- Input and Output -----
# ============================

# ===== Notes =====
# 
# Python会自动为','分隔的内容添加' '
# 与Python2不同，未添加'#-*- coding:utf-8 -*-'也能够正常输出中文
# 
# Python输入时会对程序进行阻塞
# Python输入的值为字符串
# 
# Python不支持数字与字符串相加
# 

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

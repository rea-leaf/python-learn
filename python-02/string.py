# string 字符类型
#标准数据类型
#Python3 中有六个标准的数据类型：
#
#Number（数字）
#String（字符串）
# List（列表）
#Tuple（元组）
#Set（集合）
#Dictionary（字典）
#Python3 的六个标准数据类型中：
#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
#
#string 数字
#String（字符串）
#Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
#
#字符串的截取的语法格式如下：
#
#变量[头下标:尾下标]
#索引值以 0 为开始值，-1 为从末尾的开始位置。
#加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：

str='abcdef'
#与字符串
print(str)
#第一个字符串
print(str[0])
#第三个到第五个
print(str[2:5])
#第三个到所有
print(str[2:])
# 输出第一个到倒数第二个的所有字符
print (str[0:-1])
print(str*2)
print(str+"你好")



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
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
#与Python字符串不一样的是，列表中的元素是可以改变的：
# 将对应的元素值设置为 []
list[2:4]=[]
print(list)
#List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
#
#注意：
#
#1、List写在方括号之间，元素用逗号隔开。
#2、和字符串一样，list可以被索引和切片。
#3、List可以使用+操作符进行拼接。
#4、List中的元素是可以改变的。
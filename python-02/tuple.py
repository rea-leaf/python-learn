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
tuple=('a','b','c','d')
sectuple = (123, 'asdfg')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组第一个元素
print(tuple[1:3])  # 从第二个开始输出到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(sectuple * 2)  # 输出两次元组
print(tuple + sectuple)  # 连接元组
## 元组 元素不可以修改
#tuple[2]=11
print(tuple)
#空元组
tuple1=()
#一个元素
tuple2=(10,)
print(tuple1)
print(tuple2)
#string、list和tuple都属于sequence（序列）。
#注意：
#1、与字符串一样，元组的元素不能修改。
#2、元组也可以被索引和切片，方法一样。
#3、注意构造包含0或1个元素的元组的特殊语法规则。
#4、元组也可以使用+操作符进行拼接。
#python 语法
#多行语句 需要使用反斜杠(\)
str1='one '
str2='two'
str =str1+\
        str2
print(str)
print(str1+str2)
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#用户输入
#input("\n\n按下 enter 键后退出")

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys;x='tom';sys.stdout.write(x+'\n 你好')
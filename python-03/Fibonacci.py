# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a=0
b=1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
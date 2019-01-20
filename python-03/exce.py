#异常
while True:
    try:
        x=int(input("请输入一个整数:"))
        break
    except ValueError:
        print("请输入整数")
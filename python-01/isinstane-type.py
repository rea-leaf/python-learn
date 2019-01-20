#isinstance 和 type 的区别在于：
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
#
class A:
    print("A")

class B(A):
    print('B(A)')

print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)
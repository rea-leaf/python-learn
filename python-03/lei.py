#定义一个类
class people:
    #基本属性
    name="name"
    age=20
    #私有属性
    _weight=0
    #构造方法
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self._weight=weight
    def speek(self):
        print("%s 说：我%d 岁"%(self.name,self.age))
#实例化类
p=people('tom',10,20)
p.speek()
print(p.name)
print(p.age)
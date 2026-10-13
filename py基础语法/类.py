class MyClass:
    i = 12345
    def f(self):
        return 'hello world'
x = MyClass()  # 实例化类
print("MyClass 类的属性 i 为：", x.i)  # 访问类的属性和方法
print("MyClass 类的方法 f 输出为：", x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

class MyClass:
    def __init__(self, value):
        self.value = value
    def display_value(self):
        print(self.value)
# 创建一个类的实例
obj = MyClass(42)
# 调用实例的方法
obj.display_value()

class people:
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
# 实例化类
p = people('runoob', 10, 30)
p.speak()
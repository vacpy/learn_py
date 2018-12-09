#！/usr/bin/env python3
#_*_ coding:utf-8 _*_

class DefaultInit():
    def __init__(self):
        print("实体化时执行我，我是__init__方法。")
    def show(self):
        print("我是类中定义的方法，需要通过实例化对象调用。")
test = DefaultInit()
print("类实体化结束")
test.show()

#上面的代码等同下面的代码，即可定义__init__方法，也可不定义，不定义时，默认调用该构造方法
class DefaultInit():
    def show(self):
        print("我是类中定义的方法，需要通过实例化对象调用。")
test = DefaultInit()
print("\n类实体化结束")
test.show()
print()

#在一个类中定义多个构造方法
print("#" * 80)
class MyCla(object):
    def __init__(self):
        print("我是不带参数的构造方法。")

    def __init__(self, param):                 # 第二个构造方法，而且带参数
        self.param = param
        print("\n我是带一个参数的__init__方法,参数值为：‘param’")

MyCla('hello')                                 # 在此要给参数“hello”,而且只能个一个参数
print('实体化结束。')
print("实体化结果。")
print( '#' * 80)






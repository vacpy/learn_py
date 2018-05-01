# /usr/bin/python
# _*_coding:UTF-8_*_
class MyStuff(object):                         # MyStuff 至少第一个字母要大写（类名称），
    def __init__(self):
        self.abc = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()                               #实例化
thing.apple()
print(thing.abc)


                                            ######输出结果
'''                                            I AM CLASSY APPLES!
                                               And now a thousand years between    '''


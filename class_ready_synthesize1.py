# /usr/bin/python
# _*_coding:UTF-8_*_
############################   获取某样东西里包含的东西   ####################

#dict style
mystuff('apples')              #从字典中获取'apples'的key的值

#module style
mystuff.apple()                #访问模块中的'apple'函数，获取函数中的内容
print(mystuff.tangerine)

#class style                    #对类实例化，获取类中（迷你导入），获取类中对应的属性
thing = MyStuff()
thing.apple()
print(thing.tangerine)
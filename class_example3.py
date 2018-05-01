#！/usr/bin/env python3
#_*_ coding:utf-8 _*_

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def sit(self):
        print(self.name.title()+ "is now sitting")
    def roll_over(self):
        print(self.name.tital()+ "rolled over")

little_dog = Dog("willie",6)

print("little_dog's name is "+little_dog.name.title()+ ".")
print("little_dog's age is "+str(little_dog.age) +" years old")


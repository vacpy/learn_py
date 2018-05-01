# /usr/bin/python
# _*_coding:UTF-8_*_
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get used",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        "with pockets fill of shells "])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

#歌词大意：
'''
祝你生日快乐
我不想被人利用
我就讲到这里
他们在家庭中团结起来
口袋里装满了贝壳
'''
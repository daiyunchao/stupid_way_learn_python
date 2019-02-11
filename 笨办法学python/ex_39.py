#coding=utf-8
# 字典, 可爱的字典

class Song(object):

  def __init__(self,lyrics):
    self.lyrics=lyrics

  def sing_me_a_song(self):
    for line in self.lyrics.keys():
      print line

# list版
happy_bday= Song(["Happy birthday to you",
                  "I,don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade=Song(["They rally around the family","With pockets full of shells"])

# dicts版
# happy_bday=Song({1:"Happy birthday to you",2:"I,don't want to get sued",3:"So I'll stop right there"})
# bulls_on_parade=Song({1:"They rally around the family",2:"With pockets full of shells"})

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# 学习了class的声明 class class_name(object):
# 学习了class的初始化方法 __init__(self,args)
# 学习了 class的实例化 variable =class_name(params)
# for in 遍历dicts的 for variable in dicts.values()-获取values dicts.keys() -获取全部的key dicts.items() 获取key+value的
# dicts 的 声明方式 {"name":"zhangsan","age":18,1:12}
# dicts的删除 del dicts_name['key_name']
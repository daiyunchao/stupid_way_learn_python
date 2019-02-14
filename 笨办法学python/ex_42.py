#coding=utf-8
# 对象、类、以及从属关系
# 因为 pdf的原因 42节的练习代码出现在了41节中
# 下面是我的一个小练习
class Person(object):
  def __init__(self,name):
    self.name=name
    self.pet=None
  
  def set_pet(self,pet):
    self.pet=pet

  def person_speak(self):
    print "Hi, my name is %s" %self.name
  def pet_sound(self):
    if (self.pet != None):
      self.pet.sound()

class Employee(Person):
  def __init__(self,name):
    super(Employee,self).__init__(name)

class Animal(object):
  def __init__(self,name,_sound):
    self.name=name
    self._sound=_sound
    
  def sound(self):
    print "I'm a pet ,my name is: %s, this is my sound %s" %(self.name,self._sound)

class Cat(Animal):
  def __init__(self,name,_sound):
    super(Cat,self).__init__(name,_sound)

small_cat=Cat("smail cat","miao miao miao")
zhangsan=Employee("zhangsan")
zhangsan.person_speak()
zhangsan.set_pet(small_cat)
zhangsan.pet_sound()  

# 学习了class的概念 属性 继承 和执行父类的方法
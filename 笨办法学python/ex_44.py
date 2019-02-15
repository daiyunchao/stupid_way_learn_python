#coding=utf-8
#  继承(Inheritance) VS 合成

# 继承
class Parent (object):
  def override(self):
    print "Parent override()"

  def implicit(self):
    print "Parent implicit()"

  def altered(self):
    print "Parent altered()"

class Child(Parent):
    def override(self):
      print "Child override()"

    def altered(self):
      print "Child, Before parent altered()"
      super(Child,self).altered()
      print "Child, After parent altered()"

dad=Parent()
son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print "="*40
# 合成
class Other(object):

  def override(self):
    print "Other override()"

  def implicit(self):
    print "Other implicit()"

  def altered(self):
    print "Other altered()"

class Child_2(object):

  def __init__(self):
    self.other=Other()

  def implicit(self):
    self.other.implicit()

  def override(self):
    print "Child override()"

  def altered(self):
    print "Child,Before altered()"
    self.other.altered()
    print "Child,After altered()"

  
son2=Child_2()
son2.override()
son2.implicit()
son2.altered()      
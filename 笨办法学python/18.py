#coding=utf-8
# 命名、变量、代码、函数

# this one is like your scripts with argv
def print_two(*args):
  arg1,arg2=args
  print "arg1: %r, arg2: %r" % (arg1,arg2)

# ok, that *args is actually pointless, we can just do this 
def print_two_again(arg1,arg2):
  print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument
def print_one(arg1):
  print "arg1: %r" % arg1

#this one takes on arguments
def print_none():
  print "I got nothin'."


print_two('Zed','Shaw')
print_two_again('Zed','Shaw')
print_one("Frist")
print_none()

# python .\18.py

# 学到的东西
# 函数的定义 def 函数名(参数):
# 复习了解包 参数定义:*args arg1,arg2=args


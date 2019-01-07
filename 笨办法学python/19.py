#coding=utf-8
# 函数和变量

#定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
  print "You have %d cheese!" %cheese_count
  print "You have %d boxes of crackers!" %boxes_of_crackers
  print "Man that's enough for party!"
  print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# 调用函数使用number
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
# 申明两个变量
amount_of_cheese=10
amount_of_crackers=50

# 调用函数使用变量的方式
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "And we can combine the two, variables and math:"
# 调用函数(使用计算的方式)
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

# 学到的东西
# 复习了定义函数的方法 def 函数名(参数列表):
# 学习了调用函数传递参数的不同方式
# 可以是纯粹的值(20,30) 
# 可以是变量(amount_of_cheese,amount_of_crackers)
# 可以是计算表达式(amount_of_cheese+100,amount_of_crackers+1000)

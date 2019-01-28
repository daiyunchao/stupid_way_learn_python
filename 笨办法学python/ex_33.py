#coding=utf-8
# while循环

i=0
numbers=[]

while i<6:
  print "At the top i is %d " %i
  numbers.append(i)

  i=i+1
  print "Numbers now:",numbers
  print "At the bottom i is %d" %i

print "The numbers:"
for num in numbers:
  print num

# 学习了while循环的使用方法,和其他程序的while使用方法相同
# 复习了for in 循环

# def while_fn(max_number):
#   k=0
#   while k<max_number:
#     print "Now k value is =>%d" % k
#     k+=1

# while_fn(10)
#coding=utf-8
# 循环和列表

the_count=[1,2,3,4,5]
fruits=['apple','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
  print "This is count %d " %number

# same as above
for fruit in fruits:
  print "A fruit of type: %s" %fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
  print "I got :%r" %i

# we can also build lists, first start with an empty one
elements=[]

# then use the range function to do 0 to 5 counts
for i in range(0,6):
  print "Adding %d to the list." %i
  # append is a function that lists understand
  elements.append(i)

# now we can print them out too
for i in elements:
  print "Element was: %d" %i

# 学习了 for in 循环 list 数组 就像js一样可混合各种类型到同一个数组中 学习了数组中的append追加元素的方法
# 学习了 range的使用,但值得注意的是 range(0,6) 只是0-5 range 返回的本身就是一个数组
# elements=range(0,5) 等价于 上面的range append的循环
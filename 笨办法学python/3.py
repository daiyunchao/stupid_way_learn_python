#!/usr/bin/python
# encoding:UTF-8
print "I will now count my chickens:"
# 计算表达式直接跟着 print后面
print "Hens,",25+30/6

# 优先级别
print "Roosters",100-25*3%4

print "Now I will count the eggs:"

# %是取余数 4%2 =0 1/4=0
print 3+2+1-5+4%2-1/4+6

print "Is it true that 3+2<5-7?"

# ><>=<= 优先级低于 +-*/
print 3+2<5-7

print "What is 3+2?",3+2
print "What is 5-7",5-7

print "Oh, that's why it's False."

print "How about some more"

#打印True or False
print "Is it greater?",5-2
print "Is it greater or equal?",5>=-2
print "Is it less or equal?",5<=-2
print float(1) / 8
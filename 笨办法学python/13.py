#coding=utf-8
# 参数 解包 变量
from sys import argv
script,first,second,third=argv

print "The script is called:",script
print "Your first variable is: ",first
print "Your second variable is:",second
print "Your third variable is:",third

# 学习了 import 功能 从xx地方导入到变量中来
# 学习了 从变量中将对应的值解包到另外一组变量
# 通过衍生,可以得到下面这段代码:
# arr=[1,2,3,4]
# one,two,three,four=arr
# print one

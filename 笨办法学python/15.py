#coding=utf-8
# 读取文件

from sys import argv

script,filename=argv

txt=open(filename)

print "Here's your file %r:" %filename
print txt.read()

txt.close()

print "Type the filename again:"
file_again=raw_input("> ")

txt_again=open(file_again)

print txt_again.read()

txt_again.close()

# 用open 打开一个文件获取一个file对象
# 用read 读取file对象中的内容
# 用close 关闭file文件流?
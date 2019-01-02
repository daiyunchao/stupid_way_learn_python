#coding=utf-8
# 读写文件

#导入argv
from sys import argv

#从argv中导出参数 script filename
script,filename=argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that ,hit RETURN."

raw_input("?")

print "Opening the file..."
#打开文件
target=open(filename,'w')

print "Truncating the file. Goodbye!"
#清空文件
target.truncate()

print "Now I'm going to ask you fore three lines."
#获取输入信息并保存到变量中
line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

print "I'm going to write these to the file."

#写入文件
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally ,we close it."
#关闭文件
target.close()

# 更多练习: read读取刚创建的文件
newFile=open(filename)
print newFile.read()
newFile.close()

###### 
# 打开文件的方法:open
# 读取文件的方法:read
# 写入文件的方法:write
# 关闭文件的方法:close
# 清空文件的方法:truncate
# 文件的几种模式: w r a w+ r+ a+
# w 重写文件内容(原来内容将会被清空) a 追加内容 原来内容不会被清空 所以 如果是 w模式 则truncate 可有可无

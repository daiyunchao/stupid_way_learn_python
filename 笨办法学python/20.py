#coding=utf-8
# 函数和文件

from sys import argv

script,input_file=argv

# 定义打印文件全部内容的函数
def print_all(f):
  print f.read()

# 定义 将读取文件放到文件的开始位置的函数
def rewind(f):
  f.seek(0)

# 定义 打印一行内容的函数
def print_a_line(line_count,f):
  print line_count,f.readline()

# 打开文件
current_file=open(input_file)

print "First let's print the whole file:\n"

# 打印全部内容
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# 将文件设置到文件的最开始位置
rewind(current_file)

print "Let's print three lines:"

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)


# python .\20.py .\ex15_sample.txt
# 学习到的内容
# 学习了 file 的seek方法,设置读取文件的位置
# 学习了 file.readline方法,用于读取文件的单独行
# 复习了 打开文件方法 file.open
# 复习了 文件读取方法 file.read
# 复习了 定义函数方法 def 函数名(参数...):
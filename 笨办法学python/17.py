#coding=utf-8
# 更多文件操作

from sys import argv
from os.path import exists

script,from_file,to_file =argv

print "Copying from %s to %s" %(from_file,to_file)

#we could do these two on one line too, how?
in_file=open(from_file)
in_data=in_file.read()

print "The input file is %d bytes long" %len(in_data)

print "Does the output file exists? %r" %exists(to_file)
print "Ready,hit RETURN to continue , CTRL-C to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()
in_file.close()

# python .\17.py .\ex16_sample.txt .\ex17_sample.txt 


# 一行版
# open(to_file,'w').write(open(from_file).read())

# 学习了新的导入:
# from os.path import exists
# len 可取出字节数
# 判断一个文件是否存在:
# exists(to_file)
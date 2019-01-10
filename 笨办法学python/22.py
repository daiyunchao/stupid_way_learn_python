# 总结目前为止学到的内容


# print 打印内容到终端
# print "Some string ",var,"other string" 混合打印
# print "%d %r %s"  %(var_num,var_all,var_str) 格式化输出 打印数值 字符串和 打印原始信息
# print "*"*10 打印10次字符串的内容
# print """
# """ 原始打印?

# True False python中的bool类型是首字母大写的

# str1+str2+str3 字符串的累加

# \n 换行符号
# \t 制表符
# \ 是python中的转义符


# raw_input() 该方法获取用户输入的信息
# var =raw_input() 用一个变量接收用户输入的值

# python -m pydoc raw_input 查看文档的方式

# from sys import argv 从sys库中导出argv对象,用于获取执行脚本时携带的参数
# from os.path import exists 从os.path中导出 exists方法 用于判断文件是否存在

# script,first,second,third=argv 解包

# file=open(filepath) 打开文件
# file.read() 读取文件的全部内容
# file.readline() 读取文件的一行内容
# file.close() 关闭文件流
# open(filepath,'w') 打开一个可写流的文件对象 文件的几种模式: w r a w+ r+ a+
#  w 重写文件内容(原来内容将会被清空) a 追加内容 原来内容不会被清空 所以 如果是 w模式 则truncate 可有可无
# file.truncate() 清空文件
# file.write('str') 将内容写入文件
# file.seek(0) 指定文件的读取开始位置
# exists(filepath) 判断文件是否存在,返回true或false

# float(1) 将整数和字符串转换成浮点数
# int(str) 转换成整数
# len(str) 获取内容的字节数

# def function_name (args): 函数的定义
# def function_name (*args): 将全部参数放到args数组中 使用时: arg1,arg2=args 解包使用
# function_name(args) 函数的调用







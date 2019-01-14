#coding=utf-8
# 更多练习

print "Let's practice everything."
# 使用转义符号 \
print "You\'d need to know \'about escapes with \\ that do \n newlines and \t tabs."

# 使用""" 格式化数据 ,在格式化数据中也可用使用\ 
# 常见 \t 制表符 \n 换行
poem="""
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------------"
print poem
print "--------------------"

five =10-2+3-6
# % 占位符
print "This should be five :%s" %five

# 函数定义
def secret_formula(started):
  jelly_beans=started*500
  jars=jelly_beans/1000
  crates=jars/100
  # 函数的返回值,可返回多个值
  return jelly_beans,jars,crates

start_point=10000

#解包函数返回值
beans,jars,crates=secret_formula(start_point)

# %d 数值占位符
print "With a starting point of: %d" %start_point

# 多个%占位符 使用%()
print "We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates)

start_point=start_point/10

print "We can also do that this way:"

# 占位符 可使用调用函数的方式,将自动解包函数的返回值
print "We'd have %d beans, %d jars, and %d crates. " % secret_formula(start_point)

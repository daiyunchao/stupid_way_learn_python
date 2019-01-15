#coding=utf-8
# 更多更多的练习

def break_word(stuff):
  """ This function will break up words for us."""
  words=stuff.split(' ')
  return words

def sort_words(words):
  """ Sorts the words."""
  return sorted(words)

def print_first_word(words):
  """Prints the first word after popping it off."""
  word=words.pop(0)
  print word

def print_last_word(words):
  """Print the last word after popping it off."""
  word=words.pop(-1)
  print word

def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words."""
  words=break_word(sentence)
  return sort_words(words)

def print_first_and_last(sentence):
  """Print the first and last words of the sentence."""
  words=break_word(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """Sorts the words then prints the first and last one."""
  words=sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)


# 执行:
# import 导入模块 脚本的名称 名字不能是纯数字 不加后缀
# 导入模块中的方法 可以直接被调用
# import ex_25

# 执行模块中的方法 文件名.方法名(参数)
# ex_25.break_word(sentence)

# 学习到的方法:
# str.split(' ') 字符串通过 ' '分隔,分隔后的成为一个数组
# array.sorted() 数组排序
# array.pop(0) 移除数组中的一个值,并返回
# array.pop(-1) 移除数组中的最后一个值,并返回
# 导入自定义模块到python中 import 文件名
# 执行自定义模块的方法 文件名.方法名(参数)
# 退出python exit()

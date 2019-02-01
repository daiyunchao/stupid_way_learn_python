#coding=utf-8
# 复习关键字
keys=[
  {
    "key":"and",
    "desc":"multi logic and like javascript &&"
  },
  {
    "key":" del",
    "desc":"delete variable object"
  },
  {
    "key":"from",
    "desc":"from sys import exit"
  },
  {
    "key":"not",
    "desc":"denied like javascript !"
  },
  {
    "key":"while",
    "desc":"one of loop"
  },
  {
    "key":"as",
    "desc":"with as  with open('filepath') as file:"
  },
  {
    "key":"elif",
    "desc":"like javascript else if"
  },
  {
    "key":"global",
    "desc":"global layer be used call variable eg: global user_name ='zhangsan'"
  },
  {
    "key":"or",
    "desc":"like javascript ||"
  },
  {
    "key":"with",
    "desc":"with open('filepath') as file:"
  },
  {
    "key":"assert",
    "desc":"assert condition ,if this condition is False will output a excpet Message"
  },
   {
    "key":"else",
    "desc":"like javascript else"
  },
   {
    "key":"if",
    "desc":"like javascript if"
  },
   {
    "key":"pass",
    "desc":"nothing to do"
  },
   {
    "key":"yield",
    "desc":""
  },
  {
    "key":"break",
    "desc":"like javascript break"
  },
  {
    "key":"except",
    "desc":"try except finally"
  },
  {
    "key":"import",
    "desc":"from sys import exit"
  },
   {
    "key":"print",
    "desc":"output some message to screen"
  },
   {
    "key":"class",
    "desc":"call a class"
  },
   {
    "key":"exec",
    "desc":"like javascript eval eg: i=10 j=20 exec('var=i+j') print var"
  },
  {
    "key":"in",
    "desc":"test str or element exists in string or array"
  },
  {
    "key":"raise",
    "desc":"user throw except and stop "
  },
  {
    "key":"continue",
    "desc":"like javascript continue"
  },
  {
    "key":"finally",
    "desc":"try except finally"
  },
  {
    "key":"is",
    "desc":"like javascript ==="
  },
  {
    "key":"return",
    "desc":"like javascript return"
  },
  {
    "key":"def",
    "desc":"call a function"
  },
  {
    "key":"for",
    "desc":"for item in items:"
  },
  {
    "key":"lambda",
    "desc":"def function_name(): lambda s:s*n"
  },
  {
    "key":"try",
    "desc":"try except finally"
  }
]

def print_keys():
  for item in keys:
    print "\n"
    print "key name: %s" % (item["key"])
    print "key desc: %s" % (item["desc"])
    print "--"*20
    print "\n"

print_keys()
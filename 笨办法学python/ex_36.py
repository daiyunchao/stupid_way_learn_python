#coding=utf-8
# 设计和调试

# 设计一个 包含 逻辑判断 循环 函数 的小游戏
# 答题小游戏: 从数组中获取题目(每次一题)
# 回答问题并记录正确错误数量
# 最后显示用户的回答情况
from sys import exit
questions=[
  {
    "title":"what's my hegiht?",
    "answer":"A",
    "opinions":["A 100","B 200","C 300","D 400"]
  },
  {
    "title":"How many eyes do you have?",
    "answer":"B",
    "opinions":["A 1","B 2","C 3","D 4"]
  },
  {
    "title":"How many legs do you have?",
    "answer":"B",
    "opinions":["A 1","B 2","C 3","D 4"]
  },
  {
    "title":"How many brain do you have?",
    "answer":"A",
    "opinions":["A 1","B 2","C 3","D 4"]
  },
  {
    "title":"How many wives do WeiXiaoBao have?",
    "answer":"C",
    "opinions":["A 1","B 5","C 7","D 9"]
  }
  ]
  
def singQuestion(question):
  print "Title:",question["title"]
  print "Opinions:"
  for opinion in question["opinions"]:
    print opinion
  user_answer=raw_input("Please answer: ")
  if user_answer==question["answer"]:
    print "Conguatulations! Good job! You are right!"
    return True
  else:
    print "Sorry, your answer is wrong! fighting go on!"
    return False

number=0
right_count=0
wrong_count=0
while number<len(questions):
  answer_result=singQuestion(questions[number])
  if answer_result==True:
    right_count+=1
  else:
    wrong_count+=1  
  number+=1
print "Already,All question answered. question answer result :"
print "Right Answer :%d" %right_count
print "Wrong Answer :%d" %wrong_count
if right_count==len(questions):
  print "Conguatulations! all questions are right"
else:
  print "Fighting go on!!!"
  exit(0)
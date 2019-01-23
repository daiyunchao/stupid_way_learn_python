#coding=utf-8
# ELESE and IF

people=30
cars=45
buses=15

if cars>people:
  print "We should take the cars."
elif cars<people:
  print "We should not take the cars."
else:
  print "We can't decide."

if buses>cars:
  print "That's too many buses."
elif buses<cars:
  print "Maybe we could take the buses."
else:
  print "We still can't decide."

if people>buses:
  print "Alright, let's just take the buses."
else:
  print "Fine, let's stay home then."

# 完整的学习了 if 条件表达式 if elif else
#coding=utf-8
# 作出决定

print "You enter a drak room with two doors. Do you go through door #1 or door #2?"

door=raw_input("> ")

if door=="1":
  print "There's a giant bear here eating a cheese cake. What do you do? "
  print "1. Take the cake."
  print "2. Scream at the bear."

  bear=raw_input("> ")

  if bear=="1":
    print "The bear eats your face off. Good job!"
  elif bear=="2":
    print "The bear eats your legs off. Good job!"
  else:
    print "Well, doing %s is probably better. Bear runs away." %bear
elif door=="2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolevers yelling melodies."

  insanity=raw_input("> ")

  # 1<=int(insanity)<=2
  # int(insanity) in range(1,2)
  if insanity=="1" or insanity=="2":
    print "Your body survives powered by a mind of jello. Good job!"
  else:
    print "The insanity rots your eyes into a pool of muck. Good job!"
else:
  print "You stumble around and fall on a knife and die. Good job!"

# 复习了:raw_input 从用户终端中输入获取输入信息
# 复习了 if elif else 
# 学习了 嵌套条件判断
# 学习了 两个数字范围判断的方式 1<=int(insanity)<=2 & int(insanity) in range(1,2)
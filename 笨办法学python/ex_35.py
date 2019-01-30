#coding=utf-8
# 分支和函数

from sys import exit

def gold_room():
  print "This room is full of gold. How much do you take?"

  next=raw_input("> ")
  if "0" in next or "1" in next:
    how_much=int(next)
  else:
    dead("Man, learn to type a number.")

  if how_much<50:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy hastard!")     

def bear_room():
  print "There is a bear here."
  print "The bear has a bunch of honey."
  print "The fat bear is in front of another door."
  print "How are you going to move the bear?"
  bear_move=False
  while True:
    next=raw_input("> ")
    print next
    print not bear_move
    if next=="take honey":
      dead("The bear looks at you then slaps your face off.")
    elif next=="taunt bear" and (not bear_move):
      print "The bear has moved from the door. You can go through is now."
      bear_move=True
    elif next=="taunt bear" and bear_move:
      gold_room()
    elif next=="open door" and bear_move:
      gold_room()
    else:
      print "I got no idea what tha means."

def cthulhu_room():
  print "Here you see the great evil Cthulhu."
  print "He, it. whatever stares at you and you go insane."
  print "Do you flee for your life or eat your head?"

  next=raw_input("> ")
  if "flee" in next:
    start()
  elif "head" in next:
    dead("Well that was tasty!")
  else:
    cthulhu_room()          

def dead(why):
  print why, "Good job!"
  exit(0)

def start():
  print "You are in a dark room."
  print "There is a door to your right and left."
  print "Which one do you take?"

  next=raw_input("> ")
  if next=="left":
    bear_room()
  elif next=="right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

# start()   



# 退出 from sys import exit exit(0)
# 字符串包含值 print "1" in "100" 
# print why, "Good job!"
# 其他的就是一些逻辑

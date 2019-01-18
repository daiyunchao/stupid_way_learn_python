#coding=utf-8
# 布尔表达式练习

print "True And True: ", (True and True) # true
print "False And True: ", (False and True) # false
print "1==1 and 2==1: ",(1==1 and 2==1) #false
print "test == test: ",("test"=="test") #true
print "1==1 or 2!=1: ",(1==1 or 2!=1) #true
print "True and 1==1: ",(True and 1==1) #true
print "False and 0!=0: ",(False and 0!=0) #false
print "True or 1==1: ",(True or 1==1) #true
print "test==testing: ",("test"=="testing") #false
print "1 !=0 and 2==1: ",(1 !=0 and 2==1) # false
print "test!=testing: ",("test"!="testting") #true
print "test==1: ",("test"==1) # false
print "not(True and False): ",(not(True and False)) #true
print "not (1==1 and 0!=1): ", (not(1==1 and 0!=1)) #false
print "not (10==1 or 1000==1000): ", (not(10==1 or 1000==1000)) # false
print "not (1!=10 or 3==4): ", (not(1!=10 or 3==4)) # false
print "not (testing == testting and Zed==Cool Guy): ", (not ("testting"=="testting" and "Zed"=="cool Guy")) #true
print "1==1 and not(testing==1 or 1==0): ", (1==1 and not("testting"==1 or 1==0)) # true
print "chunky==bacon and not (3==4 or 3==3): ",("chunky"=="bacon" and not(3==4 or 3==3)) # false
print "3==3 and not(testing == testing or Python == Fun): ",(3==3 and not("testing"=="testing" or "Python"=="Fun")) #false


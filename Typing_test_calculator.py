from time import *
import random as r
def mistake(paratest,user):
  error = 0
  for i in range(len(paratest)):
    try:
      if paratest[i]!=user[i]:
        error=error+1
    except:
      error = error + 1
  return error
def speed_time(time_s,time_e,userinput):
  time_delay = time_e-time_s
  time_Roundoff=round(time_delay,2)
  speed = len(userinput)/time_Roundoff
  return round(speed)


test = ["A paragraph is a self_containend unit of discourse inwrite.","My name is shubham.","welcome to my project.","How is typing Test going on."]
test1 = r.choice(test)
print("*****typing speed*****")
print(test1)
print()
print()
time_1 = time()
testinput=input(str("Enter the sentence:"))
time_2 = time()
print("Speed:",speed_time(time_1,time_2,testinput),"w/sec")
print("Error : ",mistake(test1,testinput))



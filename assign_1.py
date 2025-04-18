import math
import random

def exponential_random(lmb):

     r = random.random()
     exp = -(1/lmb) * math.log(1 - r)
     return exp


def normal_random(var1, var2):

     n = 600

     z = 0
     for i in range(n):
          z += random.random()
     z -= n / 2
     z /= math.sqrt(n / 12)
     norm = z * var2 + var1

     return norm


def queryManager(interTime, eventTime, eventName):
     global s, q, q_tasks, n, h, loadFactor, q_op_time, downtime
     loadFactor += eventTime
     if(s == 0):
          downtime += eventTime
          s = 1
          h = eventTime
     else:
          q.append(interTime)
          q_tasks.append(eventName)
          q_op_time.append(eventTime)
          n += 1
     return 



s = 0
n = 0
total_time = 0

max_length = 0
downtime = 0
loadFactor = 0

q = []
q_tasks = []
q_op_time = []

j1 = exponential_random(1.5)
j2 = exponential_random(4)

h = 0
counter = 0
logs = []
print("\n")


print(" |||  event  |||  nextTask  |||  j1  |||  j2  |||  h  |||  s  |||  n  |||  q")
print(f"|||  start  |||  0  |||  {j1}  |||  {j2}  |||  {h}  |||  {s}  |||  {n}  |||  {q}")

while(total_time <= 500):
     eventName = ""
     nextTask = min(j1, j2, h)
     if(nextTask <= 500):
          if(j1 == nextTask):
               eventName = "j1"
               # total_time  = j1
               time = exponential_random(1.5)
               j1 += time
               queryManager(j1, normal_random(2, 0.3), eventName)
               # print("event 1")
          
          elif(j2 == nextTask):
               eventName = "j2"
               # total_time  = j2
               j2 += exponential_random(4)
               queryManager(j2, normal_random(2.5, 0.1), eventName)
               # print("event 2")
          else: 
               eventName = "E"
               s = 0
               # total_time = nextTask
               if(len(q) != 0):
                    next = q_tasks[0]
                    q.pop(0)
                    q_tasks.pop(0)
                    n -= 1
                    h += q_op_time[0]
                    q_op_time.pop(0)
                    s = 1
               else:
                    nr = 500
                    h += nr
                    
     total_time = nextTask

     if (n > max_length):
          max_length = n

     if(nextTask > 500):
          eventName = "end"
     # if(counter <= 20):
     counter += 1
     logs.append(f"{counter}|||  {eventName}  |||  {nextTask}  |||  {j1}  |||  {j2}  |||  {h}  |||  {s}  |||  {n}  |||  {q_tasks[:6]}") 

     # print(f"|||  {eventName}  |||  {nextTask}  |||  {j1}  |||  {j2}  |||  {h}  |||  {s}  |||  {n}  ||| ") #{q_tasks}")
     # print(total_time)
     

size = len(logs)
# print(size)

for i in range(20):
     print(logs[i])

print(".......")

for i in range(20):
     print(logs[size - i - 1])



print(f"downtime: {downtime}")
print(f"max queue length: {max_length}")
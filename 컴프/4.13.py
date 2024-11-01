'''
#while문

n=1
while n<=5: #1,2,3,4,5,6(x)
    print("No:",n,"안녕하세요")
    n=n+1
    
print("수고하세요")

#sum구하기

n=1
sum=0
while n<=10: #1,2,3,4,5,6(x)
    sum=sum+n
   # print("No:",n,"sum:",sum)
    print("No:%2d, 합계: %d"%(n,sum))
    n=n+1
    
print("수고하세요")

#구구단 구하기 7단

n=1

while n<=9:
    print("7x%d=%d"%(n,7*n))
    n=n+1
print("end")
'''
'''
#import

import turtle as t

t.color("red")
s1=t.textinput("손효지", "도형을 입력해")
s2=int(s1)

for i in range(s2):
    t.forward(50)
    t.left(360/s2)


'''
import time

x=7
while True:
    print(x)
    time.sleep(1)

print("end")

#리스트의 연산





























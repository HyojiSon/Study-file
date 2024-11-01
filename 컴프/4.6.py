'''
#if문

a=10

a=int(input("정수를 입력해:"))
if a>10:
    print("안녕")
elif a<8:
    print("hello")
print("수고하셨습니다")
'''
'''
#turtle 삼각형 그리기

import turtle as t

t.shape("turtle")

t.forward(200)
t.left(360/3)

t.forward(200)
t.left(360/3)

t.forward(200)
t.left(360/3)

#사각형 그리기

import turtle as t

t.shape("turtle")

t.forward(200)
t.left(360/4)

t.shape("turtle")

t.forward(200)
t.left(360/4)

t.shape("turtle")

t.forward(200)
t.left(360/4)

t.shape("turtle")

t.forward(200)
t.left(360/4)

t.shape("turtle")

t.forward(200)
t.left(360/4)

'''
'''
#원 그리기

import turtle as t

t.shape("turtle")
t.color("blue")
t.shapesize(1)
t.bgcolor("black")

t.circle(100)
t.forward(200)
t.circle(100)

'''
'''
#홀수 짝수 구하기

n=int(input("정수를 입력해"))

if n%2==0:
    print("짝수")
else:
    print("홀수")
print("수고하셨습니다")

'''
'''
#for문

for k in range(1,5,1):
    print(k,"안녕")

for k in range(10, 50+1,5): #0부터 시작
    print(k,"안녕")

#
import turtle as t

t.shape("turtle")

for k in range(10): #반복 4번
    t.circle(100)
    t.forward(50)

'''
'''
#for문

for k in range(1,5,1):
    print("번호:%d"%k)

'''

#다수개의 원 그리기
import turtle as t

t.shape("turtle")
t.color("yellow")
t.bgcolor("black")
t.speed(0) #1-10까지

    
for k in range(30): 
    t.circle(100)
    t.left(360/30)
  





























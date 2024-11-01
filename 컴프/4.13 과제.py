#터틀 모듈 삼각형 그리기

#1

import turtle
turtle.shape("turtle")

turtle.forward(200)
turtle.left(120) #360/3=120
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

#2

import turtle as t

t.color("red")
s1=t.textinput("손효지", "도형을 입력해")
s2=int(s1)

for i in range(s2):
    t.forward(50)
    t.left(360/s2)

#3

import turtle as t
t.shape("turtle")

turtle.forward(200)
turtle.right(144) 
turtle.forward(200)
turtle.right(144) 
turtle.forward(200)
turtle.right(144) 
turtle.forward(200)
turtle.right(144) 
turtle.forward(200)
turtle.right(144) 

#4

import turtle as t
t.shape("turtle")
t.shapesize(3)
t.color("blue")

t.circle(100)
t.forward(200)
t.circle(100)

#5

import turtle
turtle.shape("turtle")

turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90) 
turtle.forward(200)
turtle.left(90) 
turtle.forward(200)
turtle.left(90) 



    



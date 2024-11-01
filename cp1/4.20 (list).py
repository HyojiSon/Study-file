'''
import turtle as t
t.shape("turtle")

color_list=["yellow","red","blue","green"]

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()
t.forward(50)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()
'''

'''
import turtle as t
t.shape("turtle")

color_list=["yellow","red","blue","green"]

for i in range(4):

        t.fillcolor(color_list[i])
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        i+=1
        t.forward(50)

'''
'''
import random

print("동전 던지기 게임을 시작합니다")
coin=random.randrange(2) #0,1
if coin==0:
    print("앞면입니다.")    
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다")
'''



import turtle as t

colors=["red","purple","blue","green","yellow","orange"]

t.speed(0)
t.width(3)
t.bgcolor("black")

length=10

while length<1000:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.left(91)
    length += 5











































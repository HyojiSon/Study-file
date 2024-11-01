'''
#전체 주석처리
# input () 함수 배우기, int(정수) float(실수)

name=input("이름을 입력하세요")
major=input("전공을 입력해")
year=int(input("출생년도를 입력해"))
age=2020-year+1

print("안녕")
print("자기소개")
print("내 이름은 %s이야" %name)
print("나는 %s전공이야" %major)
print("나는 %d살이야" %age)

'''
#논리 연산자
x=10
print(x<5 and x<10) # 10<5 and 10<10
print(x<5 or x<14) # 10<5 or 10<14 ->T
print(not(x<5 and x<10)) #error _true


#if 함수
a=99
if a>90:
    print("손효지 학생은 장학생입니다")
else:
    print("장학생이 아닙니다")    
print("끝")

#if함수
a=33
b=33

if b>a:
    print("b가 a보다 크다")
elif a==b:
    print("a와b는 같다")
print("종료")

#터틀 모듈 삼각형 그리기 360도 기준

import turtle
turtle.shape("turtle")

turtle.forward(200)
turtle.left(120) #360/3=120
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)


















    



















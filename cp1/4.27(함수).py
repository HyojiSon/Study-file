# 함수 사용하기

def f(x):
    y=2*x+1
    return y

print("f(10)=",f(10)) 
print("f(20)=",f(20))

#함수 응용

def sum(a,b): #a,b는 매개변수
    c=a+b
    return c
print(sum(3,4)) #3,4 인수

#인수 없는 유형

def hello():
    print("안녕 파이썬")
    print("즐거운 코딩시간이야")
    return 0
def goodbye():
    print("함수 어렵지 않아요")
    print("다음에 또 만나요")
    return 0

print("==============")
hello()
goodbye()
print("==============")

#
def sum(a,b):
    print(a,b,a+b,a*b) #3,5,3+5,3*5

a=sum(3,5)
print(a)

#
num=10
def increase(num):
    num=num+1 # num+=1
    return num

result =increase(num)
print(num) #10
print(result) #11

#응용
import turtle as t
t.shape("turtle")
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
def square1(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

square(50)
square1(100)
square(150)

































    

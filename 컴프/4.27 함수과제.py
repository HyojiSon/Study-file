#함수란
def sum(a,b):  #def 함수명(매개변수 a,b)
    c=a+b      #7=3+4
    return c    #return 결과값 (변수 c)

s=sum(3,4)    # s=변수 함수(인수 3,4)
print(s)         # print(sum(3,4)) 호출

#함수 응용하기
def f(x):        #f함수(매개변수)
    y=2*x+1  #y=2x+1
    return y   # return 결과값 y

print("f(10)=",f(10)) #f(10)=21
print("f(20)=",f(20)) #f(20)=41
print("f(30)=",f(30)) #f(30)=61

#인수 없는 유형
def hello():                    #인수를 받지 않고 hello 라는 함수 호출
    print("안녕 파이썬")    
    print("즐거운 코딩시간이야")
    return 0                   #변수가 없어서 전달받은 값은 0
                                  #생략해도 error는 발생하지 않음
def goodbye():              #인수를 받지 않고 goodbye 라는 함수 호출
    print("함수 어렵지 않아요")
    print("다음에 또 만나요")
    return 0                   #변수가 없어서 전달받은 값은 0

print("==============")   #print("메세지 아무거나")
hello()                                   #hello라는 함수 선
goodbye()                              #goodbye라는 함수 선언
print("==============")   #print("메세지 아무거나")









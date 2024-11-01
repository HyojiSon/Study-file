
import tkinter as tk

def click(text):
    #test값이 =인 경우
    if text=="=":
        try:
            #결과값을 계산한다
            result=str(round(eval(display.get()),2)) #display에 있는 글자를 가져와서 값을 계산하고 자리수를 2자리로 끊고 문자열 상태로 변환
            #메인 디스플레이를 지우고
            display.delete(0,tk.END)
            #결과값을 추가한다
            display.insert(tk.END,result)
        except:
            display.insert(tk.END,"->오류")
    #text값이 C인 경우
    elif text=="C":
        #메인 디스플레이를 지운다
        display.delete(0,tk.END)
    elif text=="AC":
        #메인 디스플레이를 지운다
        display.delete(0,tk.END)
    else:
        #그 외의 버튼을 누르면 그 버튼의 text 값을 Entry에 출력
        display.insert(tk.END,text)
    
#윈도우 생성
window=tk.Tk()
window.title("calculator")

#Display 생성
display=tk.Entry(window, width=35, bg="light green")
display.grid(row=0,column=0,columnspan=2) #dispay 빈칸이 생기지 않기 위함

#숫자 버튼을 넣을 프레임(row: 행, column: 렬)
num_frame=tk.Frame(window)
num_frame.grid(row=1,column=0) 

#숫자 버튼을 넣어봄
num_list=['7','8','9','4','5','6','1','2','3','0','.','=']
r=0
c=0
for btn_text in num_list:
    def cmd(x=btn_text):
         click(x)
    tk.Button(num_frame, text=btn_text, width=5,height=5,command=cmd).grid(row=r, column=c)
    c=c+1
    if c>2:
        c=0
        r=r+1

#연산자 버튼을 넣을 프레임
op_frame=tk.Frame(window)
op_frame.grid(row=1,column=1)

#연산자 버튼 넣어보기
op_list=['*', '/', '+', '-', '(', ')', 'C', 'AC']
r=0
c=0

for btn_text in op_list:
    def cmd(x=btn_text):
         click(x)
    tk.Button(op_frame,text=btn_text,width=5,height=5,command=cmd).grid(row=r,column=c)
    c=c+1
    if c>1:
        c=0
        r=r+1











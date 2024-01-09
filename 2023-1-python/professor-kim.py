import tkinter as tk
from tkinter import ttk
import tkinter.font
from PIL import ImageTk, Image


TITLE=("Neo둥근모 Code", 35, "bold")
BTEXT=("Neo둥근모 Code",20,"bold")
TEXT=("Neo둥근모 Code", 14)
STEXT=("Neo둥근모 Code",12)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        # controller 변수
        self.ShScoreBM1=0
        self.ShScoreBM2=0
        self.ShScoreBM3=0
        self.ShScoreGS1=0
        self.ShScoreGS2=0
        self.ShScoreGS3=0
        self.ShScoreDG1=0
        self.ShScoreDG2=0
        self.ShScoreDG3=0
        self.ShExam=0
        self.ShHidden=0

        
        self.title("두근두근 김교수님과 데이트")
    
        self.geometry("1000x750")
        self.resizable(width=False, height=False)
        
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"+{x}+{y-35}")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        
        # 프레임 추가-> for문 () 안에도 추가
        for F in (StartPage, Intro, BM1script, BM1choice, BM1react1, BM1react2, BM1react3, BM2script, BM2choice, BM2react1, BM2react2, BM3script1, BM3script2, BM3choice,
                  GSintro, GS1choice, GS1react1, GS1react2, GS2script1, GS2script2, GS2choice, GS2react1, GS2react2, GS2react3, GS3script, GS3choice, GS3react1, GS3react2, GS3react3,
                  DG1script1, DG1script2, DG1choice, DG1react1, DG1react2, DG2choice, DG2react, DG3choice, DG3react1, DG3react2, DG3react3,
                  BMa1script, BMa1exam, BMa2script, BMa2choice, BMa2react1, BMa2react2, Ending_aplus, Ending_f, HEnding_aplus, HEnding_f, Ending_hidden):
            frame=F(container, self)

            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

# 시작 페이지 - 시작 화면/이름 입력
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label=ttk.Label(self,text="두근두근 김교수님과 데이트",font=TITLE)
        label.pack(anchor="n", pady=50)

        self.name_var = tk.StringVar()
        
        self.entry=ttk.Entry(self, textvariable=self.name_var, font=TEXT)
        self.entry.pack()
        self.entry.bind("<Return>", lambda event:
                        self.button_input_callback(event, controller))
        
        self.entry.focus_set()

        button_input=tk.Button(self, text="입력", font=TEXT, command=lambda:
                                self.button_input_callback(None, controller))
        button_input.pack(anchor="center", pady=10)

    def get_name(self): 
        name = self.name_var.get()
        return name

    def change_page(self, controller, page): 
        name=self.get_name()
        # 프레임 추가 시 for 문 안에 class 이름 추가
        for F in (BM1react1, GS2script1, GS2script2, GS3react1,
                  DG1react2, DG2react, DG3react1,
                  BMa1exam, BMa2react2, Ending_aplus, Ending_f,HEnding_aplus, HEnding_f, Ending_hidden):
            controller.frames[F].update_name_label(name)
            # 제외 : choice 페이지 -  BM1choice, BM2choice, BM3choice, GS1choice, GS2choice, GS3choice, DG1choice, DG2choice, DG3choice, BMa1exam, BMa2choice
        
        controller.show_frame(page)
            
    def button_input_callback(self, event, controller):
        self.change_page(controller, Intro)

    


# Intro - 교수님 소개
class Intro(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=400, height=600, bg="light gray")
        frame1.place(x=550, y=80)

        label=ttk.Label(self, text="김완섭 교수님", font=BTEXT)
        label.place(x=570, y=120)
        label2=ttk.Label(self, text="30대 초중반 추정", font=STEXT)
        label2.place(x=570, y=150)

       
      
        LabelIntro1=tk.Label(self, text="- 숭실대학교 베어드교양대학 소속", font=STEXT, bg="light gray")
        LabelIntro1.place(x=570, y=200)
        LabelIntro2=tk.Label(self, text="- <컴퓨팅적사고와 코딩기초> 강좌", font=STEXT, bg="light gray")
        LabelIntro2.place(x=570, y=240)
        LabelIntro6=tk.Label(self, text="  선택율 1위에 기여하는 1등 공신 교수님", font=STEXT, bg="light gray")
        LabelIntro6.place(x=570, y=260)
        LabelIntro3=tk.Label(self, text="- 운동을 즐겨하심", font=STEXT, bg="light gray")
        LabelIntro3.place(x=570, y=300)
        LabelIntro4=tk.Label(self, text="- 벌레를 정말 싫어하심", font=STEXT, bg="light gray")
        LabelIntro4.place(x=570, y=340)
        LabelIntro5=tk.Label(self, text="- 음악 장르 중 발라드를 가장 좋아하심", font=STEXT, bg="light gray")
        LabelIntro5.place(x=570, y=380)

        self.image=Image.open("교수님채색.png")
        self.intro_image=ImageTk.PhotoImage(self.image)
        label_pic=tk.Label(self, image=self.intro_image, width=450)
        label_pic.place(x=80, y=80)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM1script))
        button1.place(x=873, y=700)

        

# 백마관(BM) ep1. 교문
class BM1script(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("정문_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=ttk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)
        
        # 대화 내용
        # 줄 간격 y 40, x=50 고정
        LabelScript1=tk.Label(self, text="낯선 사람이 말을 건다.", font=TEXT, bg="light gray")
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="학생! 혹시 백마관이 어디인지 아나? 내가 오늘 첫 출근이라서 말이야.", font=TEXT, bg="light gray")
        LabelScript2.place(x=50, y=580)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM1choice))
        button1.place(x=873, y=700)
        

# 백마관 ep1. 대답 선택
class BM1choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("정문_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelQ1=tk.Label(self, text="수업 시작 5분 전. 나의 대답은?", font=TEXT, bg="light gray")
        LabelQ1.place(x=45, y=480)

        button1=tk.Button(self, text="저도 처음인데... 한 번 찾아볼게요.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(30), print(self.controller.ShScoreBM1), controller.show_frame(BM1react1)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="무시한다.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShScoreBM1), controller.show_frame(BM1react2)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="아니 뭐 그런 것도 모르세요...?", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(-50), print(self.controller.ShScoreBM1), controller.show_frame(BM1react3)])
        button3.place(x=45, y=620)

    def update_score(self, points):
        self.controller.ShScoreBM1 = points


# 백마관 ep1. 친절하게 대답 반응
class BM1react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지 -> 교문
        self.image=Image.open("정문_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM2script))
        button1.place(x=873, y=700)

        # 대화 내용 중 이름
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=500)
        LabelScript1=tk.Label(self, text="고마워요!", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=540)

    def update_name_label(self, name):
        self.name_label.config(text=f"{name}학생!")


# 백마관 ep1. 무시 반응
class BM1react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("정문_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
        
        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM2script))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="내 말이 안 들리나...?", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)


# 백마관 ep1. 욕 반응
class BM1react3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("정문_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM2script))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="뭐요?!", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)


# 백마관 ep2. 자판기
class BM2script(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("백마관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM2choice))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="언덕을 한참 올라오니 목이 마르다.", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)
        
# 백마관 ep2. 자판기 선택
class BM2choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

  
        self.image=Image.open("자판기_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="자판기다. 지금 시간은 8시 59분. 이대로면 지각이다!", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=500)
        LabelScript2=tk.Label(self, text="목이 마른데 음료를 뽑을까?", bg="light gray", font=TEXT)
        LabelScript2.place(x=45, y=540)

        button1=tk.Button(self, text="자판기에서 음료 뽑는다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(-10), print(self.controller.ShScoreBM2), controller.show_frame(BM2react1)])
        button1.place(x=45, y=600)

        button2=tk.Button(self, text="안 뽑고 그냥 간다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreBM2), controller.show_frame(BM2react2)])
        button2.place(x=45, y=650)

    def update_score(self, points):
        self.controller.ShScoreBM2 = points


# 백마관 ep2. 자판기/지각
class BM2react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

      
        self.image=Image.open("자판기_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM3script1))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="9시 2분... 첫 수업부터 지각이다.", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)
        

# 백마관 ep2. 자판기/지각x
class BM2react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

      
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM3script1))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="9시 정각... 다행히 제 시간에 도착했다.", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)
        
    
# 백마관 ep3. 수업
class BM3script1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        
         
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM3script2))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="어...? 저 사람은? 정문 길치...?", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)


class BM3script2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        
         # 배경 이미지 -> 강의실
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BM3choice))
        button1.place(x=873, y=700)

        LabelScript1=tk.Label(self, text="수업 중", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="- 파이썬은...", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=560)
        
        


class BM3choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript=tk.Label(self, text="이번 수업은 여기서 마칠게요. 질문 있는 학생?", bg="light gray", font=TEXT)
        LabelScript.place(x=45, y=500)

        button1=tk.Button(self, text="질문 한다.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(30), print(self.controller.ShScoreBM3), controller.show_frame(GSintro)])
        button1.place(x=45, y=560)

        button2=tk.Button(self, text="질문 안 한다.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShScoreBM3), controller.show_frame(GSintro)])
        button2.place(x=45, y=610)
    
    def update_score(self, points):
        self.controller.ShScoreBM3 = points


# 경상관 intro
class GSintro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS1choice))
        button1.place(x=873, y=700)

# 경상관 ep1. 인사
class GS1choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

       

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelQ=tk.Label(self, text="교수님 세 분이 동시에 다가온다. 누구에게 인사할까?", bg="light gray", font=TEXT)
        LabelQ.place(x=45, y=480)

        button1=tk.Button(self, text="경제학과 교수님", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShScoreGS1), controller.show_frame(GS1react1)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="글로벌통상학과 교수님", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShScoreGS1), controller.show_frame(GS1react1)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="김완섭 교수님", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(30), print(self.controller.ShScoreGS1), controller.show_frame(GS1react2)])
        button3.place(x=45, y=620)

    def update_score(self, points):
        self.controller.ShScoreGS1 = points



# 경상관 ep1. 인사 반응(타과)
class GS1react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript=tk.Label(self, text="쳇 -_-", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS2script1))
        button1.place(x=873, y=700)


# 경상관 ep1. 인사 반응
class GS1react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS2script1))
        button1.place(x=873, y=700)
        
        LabelScript1=tk.Label(self, text="⸜(*ˊᗜˋ*)⸝", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="정말 반가워요", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=540)


# 경상관 ep2. 학과
class GS2script1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS2script2))
        button1.place(x=873, y=700)
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=500)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"{name}학생은 어떤 학과인가요?")


class GS2script2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        
         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS2choice))
        button1.place(x=873, y=700)
        
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=500)

        LabelScript=tk.Label(self, text="- 뭐야 내 이름을 어떻게 알지?", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=540)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"- {name}학생?")
    

class GS2choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript=tk.Label(self, text="교수님이 학과를 물어보신다. 뭐라고 대답할까?", bg="light gray", font=TEXT)
        LabelScript.place(x=45, y=480)

        button1=tk.Button(self, text="컴퓨터학부", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(-40), print(self.controller.ShScoreGS2), controller.show_frame(GS2react1)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="컴퓨터학부 복수전공", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(50), print(self.controller.ShScoreGS2), controller.show_frame(GS2react3)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="경제학과", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(20), print(self.controller.ShScoreGS2), controller.show_frame(GS2react2)])
        button3.place(x=45, y=620)
        
        button4=tk.Button(self, text="글로벌통상학과", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(20), print(self.controller.ShScoreGS2), controller.show_frame(GS2react2)])
        button4.place(x=45, y=670)

    def update_score(self, points):
        self.controller.ShScoreGS2 = points


class GS2react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS3script))
        button1.place(x=873, y=700)
        
        LabelScript=tk.Label(self, text="거짓말 하지 말게", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)


class GS2react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        
         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS3script))
        button1.place(x=873, y=700)

        LabelScript=tk.Label(self, text="그렇군요", bg="light gray", font=TEXT)
        LabelScript.place(x=50, y=500)
        

class GS2react3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("숭덕경상관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS3script))
        button1.place(x=873, y=700)
        
        LabelScript1=tk.Label(self, text="⸜(*ˊᗜˋ*)⸝", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="아주 좋아요. 도움이 필요하면 언제든 찾아오세요", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=540)


# 경상관 ep3. 쿱스켓
class GS3script(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("쿱스켓_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(GS3choice))
        button1.place(x=873, y=700)
        
        LabelScript=tk.Label(self, text="1+1 상품을 샀다!", bg="light gray", font=TEXT)
        LabelScript.place(x=45, y=500)


class GS3choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("쿱스켓_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript=tk.Label(self, text="교수님과 눈이 마주쳤다. 어떻게 하겠는가?", bg="light gray", font=TEXT)
        LabelScript.place(x=45, y=480)

        button1=tk.Button(self, text="교수님께 하나 드린다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(30), print(self.controller.ShScoreGS3),controller.show_frame(GS3react1)])
        button1.place(x=45, y=520)
        button2=tk.Button(self, text="그냥 친구한테 준다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreGS3), controller.show_frame(GS3react2)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="교수님과 친구가 보는 앞에서 버린다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(-10), print(self.controller.ShScoreGS3),controller.show_frame(GS3react3)])
        button3.place(x=45, y=620)

    def update_score(self, points):
        self.controller.ShScoreGS3 = points


class GS3react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("쿱스켓_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
        
        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="⸜(*ˊᗜˋ*)⸝", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="내가 달달한 음료 좋아하는 건 어떻게 알고.", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=540)
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=580)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG1script1))
        button1.place(x=873, y=700)

    def update_name_label(self, name): 
        self.name_label.config(text=f"{name}학생 정말 고마워요!")


class GS3react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("쿱스켓_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="-_- 학생 나도 달달한 음료 좋아하는데..", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG1script1))
        button1.place(x=873, y=700)

        
class GS3react3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("쿱스켓_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)
        
        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG1script1))
        button1.place(x=873, y=700)

        LabelScript1=tk.Label(self, text="(ꐦ •᷄ࡇ•᷅)", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="정말 무례하군!", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=540)


class DG1script1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="치킨을 시켰다", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG1script2))
        button1.place(x=873, y=700)

       
class DG1script2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG1choice))
        button1.place(x=873, y=700)
        
        LabelScript1=tk.Label(self, text="악!!!!", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="- 뭐지?", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=560)


class DG1choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="교수님이 벌레가 무서워서 소리를 지르신다.", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=500)

        button1=tk.Button(self, text="같이 소리를 지른다.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShScoreDG1), controller.show_frame(DG1react1)])
        button1.place(x=45, y=560)

        button2=tk.Button(self, text="멋있게 잡아준다.", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(20), print(self.controller.ShScoreDG1), controller.show_frame(DG1react2)])
        button2.place(x=45, y=610)

    def update_score(self, points):
        self.controller.ShScoreDG1 = points


class DG1react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG2choice))
        button1.place(x=873, y=700)
        
        LabelScript1=tk.Label(self, text="-_-", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="어딘가 실망스러운데요...", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=540)


class DG1react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG2choice))
        button1.place(x=873, y=700)
        
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=500)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"{name}학생 멋있게 잡아줘서 고마워요.")


class DG2choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="교수님 치킨 드실래요??", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=480)

        button1=tk.Button(self, text="치킨 다리를 드린다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreDG2), controller.show_frame(DG2react)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="치킨 날개를 드린다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreDG2), controller.show_frame(DG2react)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="치킨의 퍽퍽살을 드린다", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(50), print(self.controller.ShScoreDG2), controller.show_frame(DG2react)])
        button3.place(x=45, y=620)

    def update_score(self, points):
        self.controller.ShScoreDG2 = points


class DG2react(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(DG3choice))
        button1.place(x=873, y=700)
        
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=500)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"{name}학생 고마워요")


class DG3choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="교수님 이따가 공연 보러 오세요!", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=480)

        button1=tk.Button(self, text="6시예요.(성시경 공연)", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(30), print(self.controller.ShScoreDG3), controller.show_frame(DG3react1)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="7시예요.(박재범 공연)", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreDG3), controller.show_frame(DG3react2)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="8시예요.(싸이 공연)", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(10), print(self.controller.ShScoreDG3), controller.show_frame(DG3react2)])
        button3.place(x=45, y=620)

        button4=tk.Button(self, text="10시예요.(공연 종료 9시 30분)", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(-30), print(self.controller.ShScoreDG3), controller.show_frame(DG3react3)])
        button4.place(x=45, y=670)

    def update_score(self, points):
        self.controller.ShScoreDG3 = points


class DG3react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("성시경.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BMa1script))
        button1.place(x=873, y=700)

        LabelScript1=tk.Label(self, text="⸜(*ˊᗜˋ*)⸝", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=540)
        LabelScript2=tk.Label(self, text="최고의 공연이었어요", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=580)

    def update_name_label(self, name):
        self.name_label.config(text=f"{name}학생 정말 고마워요")


class DG3react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("싸이박재범.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="좋은 공연이네요", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BMa1script))
        button1.place(x=873, y=700)
        
        
class DG3react3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("돌계_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="(이미 공연이 종료되었다. 텅 빈 학교)", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        LabelScript2=tk.Label(self, text="(ꐦ •᷄ࡇ•᷅)", bg="light gray", font=TEXT)
        LabelScript2.place(x=50, y=580)
        LabelScript3=tk.Label(self, text="뭐야!", bg="light gray", font=TEXT)
        LabelScript3.place(x=50, y=620)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BMa1script))
        button1.place(x=873, y=700)


class BMa1script(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BMa1exam))
        button1.place(x=873, y=700)
        
        LabelScript1=tk.Label(self, text="시간이 흘러 기말고사...", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)


class BMa1exam(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("실습실_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="<기말고사>", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=480)
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=45, y=510)
        LabelScript2=tk.Label(self, text="다음 중 수열을 만들 때 사용하는 함수는 무엇인가?", bg="light gray", font=STEXT)
        LabelScript2.place(x=45, y=540)

        button1=tk.Button(self, text="range", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(70), print(self.controller.ShExam), controller.show_frame(BMa2script)])
        button1.place(x=45, y=570)

        button2=tk.Button(self, text="math", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShExam), controller.show_frame(BMa2script)])
        button2.place(x=45, y=620)

        button3=tk.Button(self, text="random", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShExam), controller.show_frame(BMa2script)])
        button3.place(x=45, y=670)

    def update_name_label(self, name):
        self.name_label.config(text=f"이름: {name}")

    def update_score(self, points):
        self.controller.ShExam = points


class BMa2script(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("백마관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        button1=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(BMa2choice))
        button1.place(x=873, y=700)

        LabelScript1=tk.Label(self, text="교수님과 마주쳤다.", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        
        

class BMa2choice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("백마관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=280, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="교수님 이거 드세요", bg="light gray", font=TEXT)
        LabelScript1.place(x=45, y=480)

        button1=tk.Button(self, text="아메리카노", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShHidden), controller.show_frame(BMa2react1)])
        button1.place(x=45, y=520)

        button2=tk.Button(self, text="카라멜 마끼야또", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(1), print(self.controller.ShHidden), controller.show_frame(BMa2react2)])
        button2.place(x=45, y=570)

        button3=tk.Button(self, text="레몬에이드", font=TEXT, width=90, height=1,
                           command=lambda: [self.update_score(0), print(self.controller.ShHidden), controller.show_frame(BMa2react1)])
        button3.place(x=45, y=620)

    def update_score(self, points):
        self.controller.ShHidden = points


class BMa2react1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("백마관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)
        
        LabelScript1=tk.Label(self, text="고마워요", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=480)

        #결말
        button=tk.Button(self, text="결말 보기", font=TEXT, width=10, height=1,
                           command=lambda: [self.if_ending(), print(self.total_score)])
        button.place(x=873, y=700)

    def switch_frame(self, ending):
        self.controller.show_frame(ending)

    def if_ending(self):
        self.total_score = (self.controller.ShScoreBM1 + self.controller.ShScoreBM2 + self.controller.ShScoreBM3 +
                            self.controller.ShScoreGS1 + self.controller.ShScoreGS2 + self.controller.ShScoreGS3 +
                            self.controller.ShScoreDG1 + self.controller.ShScoreDG2 + self.controller.ShScoreDG3 +
                            self.controller.ShExam)
        if self.total_score>=320:
            self.switch_frame(Ending_aplus)
        else:
            self.switch_frame(Ending_f)


class BMa2react2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

         # 배경 이미지
        self.image=Image.open("백마관_ill.png")
        resized_image=self.image.resize((self.controller.winfo_width(), self.controller.winfo_height()), Image.LANCZOS)
        self.background_image=ImageTk.PhotoImage(resized_image)
        background_label=tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")

        frame1=tk.Frame(self, width=965, height=250, bg="light gray")
        frame1.place(x=17, y=440)

        LabelScript1=tk.Label(self, text="⸜(*ˊᗜˋ*)⸝", bg="light gray", font=TEXT)
        LabelScript1.place(x=50, y=500)
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=TEXT)
        self.name_label.place(x=50, y=540)

        #결말
        button=tk.Button(self, text="결말 보기", font=TEXT, width=10, height=1,
                           command=lambda: [self.if_ending(), print(self.total_score)])
        button.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"{name}학생 이걸 기억해주다니 정말 감동이에요!")

    def switch_frame(self, ending):
        self.controller.show_frame(ending)

    def if_ending(self):
        self.total_score = (self.controller.ShScoreBM1 + self.controller.ShScoreBM2 + self.controller.ShScoreBM3 +
                            self.controller.ShScoreGS1 + self.controller.ShScoreGS2 + self.controller.ShScoreGS3 +
                            self.controller.ShScoreDG1 + self.controller.ShScoreDG2 + self.controller.ShScoreDG3 +
                            self.controller.ShExam)
        if self.total_score>=320:
            self.switch_frame(HEnding_aplus)
        else:
            self.switch_frame(HEnding_f)
            
# 엔딩: A+
class Ending_aplus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=965, height=650, bg="light gray")
        frame1.place(x=17, y=30)

        LabelScript1=tk.Label(self, text="          성적 조회", bg="light gray", font=TITLE)
        LabelScript1.place(x=50, y=50)
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=50, y=120)

        LabelScript2=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript2.place(x=50, y=200)
        LabelScript3=tk.Label(self, text="                    과목                    |     과목학점     |     성적     ", bg="light gray", font=STEXT)
        LabelScript3.place(x=50, y=235)
        LabelScript6=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript6.place(x=50, y=270)
        LabelScript4=tk.Label(self, text="      [컴퓨팅적사고]컴퓨팅적사고와코딩기초             2.0              A+      ", bg="light gray", font=STEXT)
        LabelScript4.place(x=50, y=305)
        LabelScript5=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=340)

        button2=tk.Button(self, text="처음으로", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(StartPage))
        button2.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"이름: {name}")


# 엔딩: F
class Ending_f(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=965, height=650, bg="light gray")
        frame1.place(x=17, y=30)

        LabelScript1=tk.Label(self, text="          성적 조회", bg="light gray", font=TITLE)
        LabelScript1.place(x=50, y=50)
        
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=50, y=120)

        LabelScript2=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript2.place(x=50, y=200)
        LabelScript3=tk.Label(self, text="                    과목                    |     과목학점     |     성적     ", bg="light gray", font=STEXT)
        LabelScript3.place(x=50, y=235)
        LabelScript6=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript6.place(x=50, y=270)
        LabelScript4=tk.Label(self, text="      [컴퓨팅적사고]컴퓨팅적사고와코딩기초             2.0               F      ", bg="light gray", font=STEXT)
        LabelScript4.place(x=50, y=305)
        LabelScript5=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=340)

        button2=tk.Button(self, text="처음으로", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(StartPage))
        button2.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"이름: {name}")


# 엔딩: A+
class HEnding_aplus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=965, height=650, bg="light gray")
        frame1.place(x=17, y=30)

        LabelScript1=tk.Label(self, text="          성적 조회", bg="light gray", font=TITLE)
        LabelScript1.place(x=50, y=50)
        # 이름 표시 라벨
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=50, y=120)

        LabelScript2=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript2.place(x=50, y=200)
        LabelScript3=tk.Label(self, text="                    과목                    |     과목학점     |     성적     ", bg="light gray", font=STEXT)
        LabelScript3.place(x=50, y=235)
        LabelScript6=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript6.place(x=50, y=270)
        LabelScript4=tk.Label(self, text="      [컴퓨팅적사고]컴퓨팅적사고와코딩기초             2.0              A+      ", bg="light gray", font=STEXT)
        LabelScript4.place(x=50, y=305)
        LabelScript5=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=340)

        button2=tk.Button(self, text="계속하기", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(Ending_hidden))
        button2.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"이름: {name}")



# 엔딩: F
class HEnding_f(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=965, height=650, bg="light gray")
        frame1.place(x=17, y=30)

        LabelScript1=tk.Label(self, text="          성적 조회", bg="light gray", font=TITLE)
        LabelScript1.place(x=50, y=50)
        # 이름 표시 라벨
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=50, y=120)

        LabelScript2=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript2.place(x=50, y=200)
        LabelScript3=tk.Label(self, text="                    과목                    |     과목학점     |     성적     ", bg="light gray", font=STEXT)
        LabelScript3.place(x=50, y=235)
        LabelScript6=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript6.place(x=50, y=270)
        LabelScript4=tk.Label(self, text="      [컴퓨팅적사고]컴퓨팅적사고와코딩기초             2.0               F      ", bg="light gray", font=STEXT)
        LabelScript4.place(x=50, y=305)
        LabelScript5=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=340)

        button2=tk.Button(self, text="처음으로", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(StartPage))
        button2.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"이름: {name}")




# 엔딩: 대학원
class Ending_hidden(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame1=tk.Frame(self, width=965, height=650, bg="light gray")
        frame1.place(x=17, y=30)

        LabelScript2=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript2.place(x=50, y=100)
        LabelScript1=tk.Label(self, text="보낸 사람  |  김완섭 (ws****2@ssu.ac.kr)  ", bg="light gray", font=STEXT)
        LabelScript1.place(x=50, y=140)
        LabelScript3=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript3.place(x=50, y=180)
        self.name_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name_label.place(x=50, y=230)
        LabelScript4=tk.Label(self, text="한 학기동안 수업에 최선을 다하는 모습 보기 좋았어요.", bg="light gray", font=STEXT)
        LabelScript4.place(x=50, y=290)
        self.name2_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name2_label.place(x=50, y=320)
        LabelScript5=tk.Label(self, text="혹시 대학원에 진학하여 함께 연구해볼 생각 있나요? ", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=380)
        LabelScript6=tk.Label(self, text="관심이 있다면 언제든지 연락 주세요. ", bg="light gray", font=STEXT)
        LabelScript6.place(x=50, y=410)
        self.name3_label=tk.Label(self, text="", bg="light gray", font=STEXT)
        self.name3_label.place(x=50, y=470)
        LabelScript7=tk.Label(self, text="김완섭 드림 ", bg="light gray", font=STEXT)
        LabelScript7.place(x=50, y=530)
        LabelScript5=tk.Label(self, text="-----------------------------------------------------------------------------", bg="light gray", font=STEXT)
        LabelScript5.place(x=50, y=580)

        LabelScript8=tk.Label(self, text="- 뭐지?", bg="light gray", font=STEXT)
        LabelScript8.place(x=50, y=630)


        button2=tk.Button(self, text="처음으로", font=TEXT, width=10, height=1,
                           command=lambda: controller.show_frame(StartPage))
        button2.place(x=873, y=700)

    def update_name_label(self, name):  # 이름 불러오기
        self.name_label.config(text=f"안녕하세요 {name}학생")
        self.name2_label.config(text=f"{name}학생의 학문적 열정과 성과가 정말 놀라웠어요.")
        self.name3_label.config(text=f"{name}학생의 무궁한 발전을 기원합니다.")


# Driver Code
app=tkinterApp()
app.mainloop()

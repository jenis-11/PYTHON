##Import Libraries

from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox as mb

##New Window

quiz = Tk()
quiz.title("Guess Their Types")
quiz.geometry("1532x790")
quiz.config(bg = "RoyalBlue")

img_00 = PhotoImage(file = "./GUESS-THEIR-TYPES.png")
img_lbl_00 = Label(quiz, text = "", image = img_00)
img_lbl_00.pack()

##Icon

quiz.wm_iconbitmap("./projimg16.ico")

##Right Answer Statement

def right_answer():
    r_ans = Label(quiz, text = "", bg = "Yellow")
    r_ans.place(x = 750, y = 480)
    r_ans.configure(text = "The answer is Right", font = ("OCR A Extended", 20, "bold"), width = 35, height = 1)
    r_ans.configure(bg = "Green")

##Empty Label

def empty_label():
    lbl_00 = Label(quiz, bg = "RoyalBlue", font = ( "OCR A Extended", 20, "bold"), width = 35, height = 1)
    lbl_00.place(x = 750, y = 480)

##Quit Game 

def quit_game():
    quiz.destroy()

##Change Game
    
def change_game():
    quiz.destroy()
    import PROJECT_GAME_OPTION

##Score

score_counter_GTT = IntVar()
score_counter_GTT = 0

def increment():
    global score_counter_GTT
    score_counter_GTT = score_counter_GTT + 1

def view_score():   
    
    score_label = Label(quiz, text = score_counter_GTT, bg = "Black", fg = "White", font = ("OCR A Extended", 30), width = 65, height = 15) 
    score_label.pack()

    score_label_0 = Label(quiz, text = "Your Score is: ", bg = "Black", fg = "White", font = ("OCR A Extended", 30), width = 65, height = 5) 
    score_label_0.place(x = 0, y = 0)

    quit_but = Button(quiz, text = "QUIT", bg = "Black", fg = "White", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 5, height = 1, command = quit_game)
    quit_but.place(x = 1462, y = 735)

    change_g_but = Button(quiz,text = "CHANGE GAME", bg = "Black", fg = "White", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 12, height = 1, command = change_game)
    change_g_but.place(x = 1380, y = 695)
    
##Question Image

q_image_01 = Image.open('./Answer_Image/pokemon_01.1.png')
resized = q_image_01.resize((500,400))
q_image_02 = ImageTk.PhotoImage(resized)
lbl_1 = Label(quiz, text = "", image = q_image_02).place(x = 145, y = 300)

class QUEST_IMG():
    def question_image_02(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_02.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_02.rb_P_02()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_02)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_02())

    def question_image_03(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_03.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_03.rb_P_03()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_03)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_03())

    def question_image_04(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_04.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_04.rb_P_04()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_04)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_04())

    def question_image_05(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_05.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_05.rb_P_05()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_05)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_05())

    def question_image_06(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_06.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_06.rb_P_06()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_06)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_06())

    def question_image_07(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_07.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_07.rb_P_07()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_07)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_07())

    def question_image_08(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_08.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_08.rb_P_08()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_08)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_08())

    def question_image_09(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_09.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_09.rb_P_09()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_09)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_09())

    def question_image_10(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_10.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_10.rb_P_10()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_10)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_10())

    def question_image_11(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_11.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_11.rb_P_11()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_11)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_11())

    def question_image_12(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_12.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_12.rb_P_12()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_12)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_12())

    def question_image_13(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_13.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_13.rb_P_13()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_13)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_13())

    def question_image_14(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_14.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_14.rb_P_14()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_14)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_14())

    def question_image_15(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_15.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_15.rb_P_15()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_15)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_15())

    def question_image_16(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_16.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_16.rb_P_16()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_16)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_16())

    def question_image_17(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_17.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_17.rb_P_17()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_17)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_17())

    def question_image_18(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_18.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_18.rb_P_18()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_18)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_18())

    def question_image_19(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_19.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_19.rb_P_19()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_19)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_19())

    def question_image_20(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_20.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_20.rb_P_20()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_20)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_20())

    def question_image_21(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_21.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_21.rb_P_21()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_21)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_21())

    def question_image_22(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_22.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_22.rb_P_22()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_22)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_22())

    def question_image_23(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_23.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_23.rb_P_23()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_23)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_23())

    def question_image_24(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_24.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_24.rb_P_24()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_24)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_24())

    def question_image_25(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_25.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_25.rb_P_25()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_25)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_25())

    def question_image_26(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_26.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_26.rb_P_26()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_26)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_26())

    def question_image_27(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_27.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_27.rb_P_27()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_27)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_27())

    def question_image_28(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_28.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_28.rb_P_28()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_28)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_28())

    def question_image_29(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_29.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_29.rb_P_29()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_29)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_29())

    def question_image_30(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_30.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_30.rb_P_30()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_30)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_30())

    def question_image_31(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_31.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_31.rb_P_31()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_31)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_31())

    def question_image_32(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_32.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_32.rb_P_32()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_32)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_32())

    def question_image_33(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_33.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_33.rb_P_33()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_33)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_33())

    def question_image_34(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_34.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_34.rb_P_34()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_34)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_34())

    def question_image_35(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_35.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_35.rb_P_35()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_35)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_35())

    def question_image_36(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_36.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_36.rb_P_36()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_36)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_36())

    def question_image_37(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_37.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_37.rb_P_37()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_37)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_37())

    def question_image_38(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_38.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_38.rb_P_38()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_38)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_38())

    def question_image_39(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_39.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_39.rb_P_39()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_39)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_39())

    def question_image_40(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_40.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_40.rb_P_40()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_40)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_40())

    def question_image_41(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_41.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_41.rb_P_41()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_41)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_41())

    def question_image_42(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_42.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_42.rb_P_42()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_42)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_42())

    def question_image_43(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_43.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_43.rb_P_43()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_43)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_43())

    def question_image_44(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_44.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_44.rb_P_44()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_44)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_44())

    def question_image_45(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_45.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_45.rb_P_45()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_45)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_45())

    def question_image_46(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_46.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_46.rb_P_46()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_46)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_46())

    def question_image_47(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_47.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_47.rb_P_47()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_47)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_47())

    def question_image_48(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_48.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_48.rb_P_48()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_48)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_48())

    def question_image_49(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_49.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_49.rb_P_49()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_49)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_49())

    def question_image_50(self):
        q_image_01 = Image.open("./Answer_Image/pokemon_50.1.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        rb_50.rb_P_50()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_50)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_50())
        
QI = QUEST_IMG()
    
##Radiobuttons

a_01 = StringVar()
a_02 = StringVar()
a_03 = StringVar()
a_04 = StringVar()
a_05 = StringVar()
a_06 = StringVar()
a_07 = StringVar()
a_08 = StringVar()
a_09 = StringVar()
a_10 = StringVar()
a_11 = StringVar()
a_12 = StringVar()
a_13 = StringVar()
a_14 = StringVar()
a_15 = StringVar()
a_16 = StringVar()
a_17 = StringVar()
a_18 = StringVar()
a_19 = StringVar()
a_20 = StringVar()
a_21 = StringVar()
a_22 = StringVar()
a_23 = StringVar()
a_24 = StringVar()
a_25 = StringVar()
a_26 = StringVar()
a_27 = StringVar()
a_28 = StringVar()
a_29 = StringVar()
a_30 = StringVar()
a_31 = StringVar()
a_32 = StringVar()
a_33 = StringVar()
a_34 = StringVar()
a_35 = StringVar()
a_36 = StringVar()
a_37 = StringVar()
a_38 = StringVar()
a_39 = StringVar()
a_40 = StringVar()
a_41 = StringVar()
a_42 = StringVar()
a_43 = StringVar()
a_44 = StringVar()
a_45 = StringVar()
a_46 = StringVar()
a_47 = StringVar()
a_48 = StringVar()
a_49 = StringVar()
a_50 = StringVar()

rad_1_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_01, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
rad_1_1.place(x = 920, y = 350)

rad_1_2 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_01, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
rad_1_2.place(x = 920, y = 400)

rad_1_3 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_01, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
rad_1_3.place(x = 920, y = 450)

rad_1_4 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_01, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
rad_1_4.place(x = 920, y = 500)

class radbutton_02():
    def rb_P_02(self):
        self.rad_2_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_02, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_2_1.place(x = 920, y = 350)

        self.rad_2_2 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_02, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_2_2.place(x = 920, y = 400)

        self.rad_2_3 = Radiobutton(quiz, text = "Dragon", value = "Dragon", variable = a_02, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_2_3.place(x = 920, y = 450)

        self.rad_2_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_02, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_2_4.place(x = 920, y = 500)

    def rb_D_02(self):
        self.rad_2_1.destroy()
        self.rad_2_2.destroy()
        self.rad_2_3.destroy()
        self.rad_2_4.destroy()
rb_02 = radbutton_02()

class radbutton_03():
    def rb_P_03(self):
        self.rad_3_1 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_03, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_3_1.place(x = 920, y = 350)

        self.rad_3_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_03, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_3_2.place(x = 920, y = 400)

        self.rad_3_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_03, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_3_3.place(x = 920, y = 450)

        self.rad_3_4 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_03, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_3_4.place(x = 920, y = 500)

    def rb_D_03(self):
        self.rad_3_1.destroy()
        self.rad_3_2.destroy()
        self.rad_3_3.destroy()
        self.rad_3_4.destroy()
rb_03 = radbutton_03()

class radbutton_04():
    def rb_P_04(self):
        self.rad_4_1 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_04, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_4_1.place(x = 920, y = 350)

        self.rad_4_2 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_04, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_4_2.place(x = 920, y = 400)

        self.rad_4_3 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_04, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_4_3.place(x = 920, y = 450)

        self.rad_4_4 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_04, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_4_4.place(x = 920, y = 500)

    def rb_D_04(self):
        self.rad_4_1.destroy()
        self.rad_4_2.destroy()
        self.rad_4_3.destroy()
        self.rad_4_4.destroy()
rb_04 = radbutton_04()

class radbutton_05():
    def rb_P_05(self):
        self.rad_5_1 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_05, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_5_1.place(x = 920, y = 350)

        self.rad_5_2 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_05, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_5_2.place(x = 920, y = 400)

        self.rad_5_3 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_05, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_5_3.place(x = 920, y = 450)

        self.rad_5_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_05, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_5_4.place(x = 920, y = 500)

    def rb_D_05(self):
        self.rad_5_1.destroy()
        self.rad_5_2.destroy()
        self.rad_5_3.destroy()
        self.rad_5_4.destroy()
rb_05 = radbutton_05()

class radbutton_06():
    def rb_P_06(self):
        self.rad_6_1 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_06, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_6_1.place(x = 920, y = 350)

        self.rad_6_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_06, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_6_2.place(x = 920, y = 400)

        self.rad_6_3 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_06, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_6_3.place(x = 920, y = 450)

        self.rad_6_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_06, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_6_4.place(x = 920, y = 500)

    def rb_D_06(self):
        self.rad_6_1.destroy()
        self.rad_6_2.destroy()
        self.rad_6_3.destroy()
        self.rad_6_4.destroy()
rb_06 = radbutton_06()

class radbutton_07():
    def rb_P_07(self):
        self.rad_7_1 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_07, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_7_1.place(x = 920, y = 350)

        self.rad_7_2 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_07, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_7_2.place(x = 920, y = 400)

        self.rad_7_3 = Radiobutton(quiz, text = "Weedle", value = "Weedle", variable = a_07, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_7_3.place(x = 920, y = 450)

        self.rad_7_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_07, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_7_4.place(x = 920, y = 500)

    def rb_D_07(self):
        self.rad_7_1.destroy()
        self.rad_7_2.destroy()
        self.rad_7_3.destroy()
        self.rad_7_4.destroy()
rb_07 = radbutton_07()

class radbutton_08():
    def rb_P_08(self):
        self.rad_8_1 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_08, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_8_1.place(x = 920, y = 350)

        self.rad_8_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_08, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_8_2.place(x = 920, y = 400)

        self.rad_8_3 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_08, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_8_3.place(x = 920, y = 450)

        self.rad_8_4 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_08, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_8_4.place(x = 920, y = 500)

    def rb_D_08(self):
        self.rad_8_1.destroy()
        self.rad_8_2.destroy()
        self.rad_8_3.destroy()
        self.rad_8_4.destroy()
rb_08 = radbutton_08()

class radbutton_09():
    def rb_P_09(self):
        self.rad_9_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_09, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_9_1.place(x = 920, y = 350)

        self.rad_9_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_09, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_9_2.place(x = 920, y = 400)

        self.rad_9_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_09, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_9_3.place(x = 920, y = 450)

        self.rad_9_4 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_09, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_9_4.place(x = 920, y = 500)

    def rb_D_09(self):
        self.rad_9_1.destroy()
        self.rad_9_2.destroy()
        self.rad_9_3.destroy()
        self.rad_9_4.destroy()
rb_09 = radbutton_09()

class radbutton_10():
    def rb_P_10(self):
        self.rad_10_1 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_10, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_10_1.place(x = 920, y = 350)

        self.rad_10_2 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_10, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_10_2.place(x = 920, y = 400)

        self.rad_10_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_10, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_10_3.place(x = 920, y = 450)

        self.rad_10_4 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_10, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_10_4.place(x = 920, y = 500)

    def rb_D_10(self):
        self.rad_10_1.destroy()
        self.rad_10_2.destroy()
        self.rad_10_3.destroy()
        self.rad_10_4.destroy()
rb_10 = radbutton_10()

class radbutton_11():
    def rb_P_11(self):
        self.rad_11_1 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_11, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_11_1.place(x = 920, y = 350)

        self.rad_11_2 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_11, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_11_2.place(x = 920, y = 400)

        self.rad_11_3 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_11, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_11_3.place(x = 920, y = 450)

        self.rad_11_4 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_11, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_11_4.place(x = 920, y = 500)

    def rb_D_11(self):
        self.rad_11_1.destroy()
        self.rad_11_2.destroy()
        self.rad_11_3.destroy()
        self.rad_11_4.destroy()
rb_11 = radbutton_11()

class radbutton_12():
    def rb_P_12(self):
        self.rad_12_1 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_12, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_12_1.place(x = 920, y = 350)

        self.rad_12_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_12, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_12_2.place(x = 920, y = 400)

        self.rad_12_3 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_12, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_12_3.place(x = 920, y = 450)

        self.rad_12_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_12, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_12_4.place(x = 920, y = 500)

    def rb_D_12(self):
        self.rad_12_1.destroy()
        self.rad_12_2.destroy()
        self.rad_12_3.destroy()
        self.rad_12_4.destroy()
rb_12 = radbutton_12()

class radbutton_13():
    def rb_P_13(self):
        self.rad_13_1 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_13, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_13_1.place(x = 920, y = 350)

        self.rad_13_2 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_13, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_13_2.place(x = 920, y = 400)

        self.rad_13_3 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_13, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_13_3.place(x = 920, y = 450)

        self.rad_13_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_13, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_13_4.place(x = 920, y = 500)

    def rb_D_13(self):
        self.rad_13_1.destroy()
        self.rad_13_2.destroy()
        self.rad_13_3.destroy()
        self.rad_13_4.destroy()
rb_13 = radbutton_13()

class radbutton_14():
    def rb_P_14(self):
        self.rad_14_1 = Radiobutton(quiz, text = "Ghost", value = "Ghost", variable = a_14, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_14_1.place(x = 920, y = 350)

        self.rad_14_2 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_14, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_14_2.place(x = 920, y = 400)

        self.rad_14_3 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_14, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_14_3.place(x = 920, y = 450)

        self.rad_14_4 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_14, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_14_4.place(x = 920, y = 500)

    def rb_D_14(self):
        self.rad_14_1.destroy()
        self.rad_14_2.destroy()
        self.rad_14_3.destroy()
        self.rad_14_4.destroy()
rb_14 = radbutton_14()

class radbutton_15():
    def rb_P_15(self):
        self.rad_15_1 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_15, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_15_1.place(x = 920, y = 350)

        self.rad_15_2 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_15, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_15_2.place(x = 920, y = 400)

        self.rad_15_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_15, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_15_3.place(x = 920, y = 450)

        self.rad_15_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_15, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_15_4.place(x = 920, y = 500)

    def rb_D_15(self):
        self.rad_15_1.destroy()
        self.rad_15_2.destroy()
        self.rad_15_3.destroy()
        self.rad_15_4.destroy()
rb_15 = radbutton_15()

class radbutton_16():
    def rb_P_16(self):
        self.rad_16_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_16, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_16_1.place(x = 920, y = 350)

        self.rad_16_2 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_16, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_16_2.place(x = 920, y = 400)

        self.rad_16_3 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_16, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_16_3.place(x = 920, y = 450)

        self.rad_16_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_16, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_16_4.place(x = 920, y = 500)

    def rb_D_16(self):
        self.rad_16_1.destroy()
        self.rad_16_2.destroy()
        self.rad_16_3.destroy()
        self.rad_16_4.destroy()
rb_16 = radbutton_16()

class radbutton_17():
    def rb_P_17(self):
        self.rad_17_1 = Radiobutton(quiz, text = "Ghost", value = "Ghost", variable = a_17, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_17_1.place(x = 920, y = 350)
        
        self.rad_17_2 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_17, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_17_2.place(x = 920, y = 400)

        self.rad_17_3 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_17, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_17_3.place(x = 920, y = 450)

        self.rad_17_4 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_17, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_17_4.place(x = 920, y = 500)

    def rb_D_17(self):
        self.rad_17_1.destroy()
        self.rad_17_2.destroy()
        self.rad_17_3.destroy()
        self.rad_17_4.destroy()
rb_17 = radbutton_17()

class radbutton_18():
    def rb_P_18(self):
        self.rad_18_1 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_18, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_18_1.place(x = 920, y = 350)
        
        self.rad_18_2 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_18, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_18_2.place(x = 920, y = 400)

        self.rad_18_3 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_18, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_18_3.place(x = 920, y = 450)

        self.rad_18_4 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_18, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_18_4.place(x = 920, y = 500)

    def rb_D_18(self):
        self.rad_18_1.destroy()
        self.rad_18_2.destroy()
        self.rad_18_3.destroy()
        self.rad_18_4.destroy()
rb_18 = radbutton_18()

class radbutton_19():
    def rb_P_19(self):
        self.rad_19_1 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_19, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_19_1.place(x = 920, y = 350)
        
        self.rad_19_2 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_19, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_19_2.place(x = 920, y = 400)

        self.rad_19_3 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_19, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_19_3.place(x = 920, y = 450)

        self.rad_19_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_19, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_19_4.place(x = 920, y = 500)

    def rb_D_19(self):
        self.rad_19_1.destroy()
        self.rad_19_2.destroy()
        self.rad_19_3.destroy()
        self.rad_19_4.destroy()
rb_19 = radbutton_19()

class radbutton_20():
    def rb_P_20(self):
        self.rad_20_1 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_20, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_20_1.place(x = 920, y = 350)
        
        self.rad_20_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_20, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_20_2.place(x = 920, y = 400)

        self.rad_20_3 = Radiobutton(quiz, text = "Dragon", value = "Dragon", variable = a_20, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_20_3.place(x = 920, y = 450)

        self.rad_20_4 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_20, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_20_4.place(x = 920, y = 500)

    def rb_D_20(self):
        self.rad_20_1.destroy()
        self.rad_20_2.destroy()
        self.rad_20_3.destroy()
        self.rad_20_4.destroy()
rb_20 = radbutton_20()

class radbutton_21():
    def rb_P_21(self):
        self.rad_21_1 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_21, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_21_1.place(x = 920, y = 350)
        
        self.rad_21_2 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_21, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_21_2.place(x = 920, y = 400)

        self.rad_21_3 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_21, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_21_3.place(x = 920, y = 450)

        self.rad_21_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_21, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_21_4.place(x = 920, y = 500)

    def rb_D_21(self):
        self.rad_21_1.destroy()
        self.rad_21_2.destroy()
        self.rad_21_3.destroy()
        self.rad_21_4.destroy()
rb_21 = radbutton_21()

class radbutton_22():
    def rb_P_22(self):
        self.rad_22_1 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_22, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_22_1.place(x = 920, y = 350)
        
        self.rad_22_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_22, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_22_2.place(x = 920, y = 400)

        self.rad_22_3 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_22, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_22_3.place(x = 920, y = 450)

        self.rad_22_4 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_22, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_22_4.place(x = 920, y = 500)

    def rb_D_22(self):
        self.rad_22_1.destroy()
        self.rad_22_2.destroy()
        self.rad_22_3.destroy()
        self.rad_22_4.destroy()
rb_22 = radbutton_22()

class radbutton_23():
    def rb_P_23(self):
        self.rad_23_1 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_23, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_23_1.place(x = 920, y = 350)
        
        self.rad_23_2 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_23, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_23_2.place(x = 920, y = 400)

        self.rad_23_3 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_23, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_23_3.place(x = 920, y = 450)

        self.rad_23_4 = Radiobutton(quiz, text = "Ghost", value = "Ghost", variable = a_23, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_23_4.place(x = 920, y = 500)

    def rb_D_23(self):
        self.rad_23_1.destroy()
        self.rad_23_2.destroy()
        self.rad_23_3.destroy()
        self.rad_23_4.destroy()
rb_23 = radbutton_23()

class radbutton_24():
    def rb_P_24(self):
        self.rad_24_1 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_24, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_24_1.place(x = 920, y = 350)
        
        self.rad_24_2 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_24, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_24_2.place(x = 920, y = 400)

        self.rad_24_3 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_24, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_24_3.place(x = 920, y = 450)

        self.rad_24_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_24, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_24_4.place(x = 920, y = 500)

    def rb_D_24(self):
        self.rad_24_1.destroy()
        self.rad_24_2.destroy()
        self.rad_24_3.destroy()
        self.rad_24_4.destroy()
rb_24 = radbutton_24()

class radbutton_25():
    def rb_P_25(self):
        self.rad_25_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_25, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_25_1.place(x = 920, y = 350)
        
        self.rad_25_2 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_25, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_25_2.place(x = 920, y = 400)

        self.rad_25_3 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_25, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_25_3.place(x = 920, y = 450)

        self.rad_25_4 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_25, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_25_4.place(x = 920, y = 500)

    def rb_D_25(self):
        self.rad_25_1.destroy()
        self.rad_25_2.destroy()
        self.rad_25_3.destroy()
        self.rad_25_4.destroy()
rb_25 = radbutton_25()

class radbutton_26():
    def rb_P_26(self):
        self.rad_26_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_26, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_26_1.place(x = 920, y = 350)
        
        self.rad_26_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_26, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_26_2.place(x = 920, y = 400)

        self.rad_26_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_26, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_26_3.place(x = 920, y = 450)

        self.rad_26_4 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_26, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_26_4.place(x = 920, y = 500)

    def rb_D_26(self):
        self.rad_26_1.destroy()
        self.rad_26_2.destroy()
        self.rad_26_3.destroy()
        self.rad_26_4.destroy()
rb_26 = radbutton_26()

class radbutton_27():
    def rb_P_27(self):
        self.rad_27_1 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_27, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_27_1.place(x = 920, y = 350)
        
        self.rad_27_2 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_27, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_27_2.place(x = 920, y = 400)

        self.rad_27_3 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_27, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_27_3.place(x = 920, y = 450)

        self.rad_27_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_27, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_27_4.place(x = 920, y = 500)

    def rb_D_27(self):
        self.rad_27_1.destroy()
        self.rad_27_2.destroy()
        self.rad_27_3.destroy()
        self.rad_27_4.destroy()
rb_27 = radbutton_27()

class radbutton_28():
    def rb_P_28(self):
        self.rad_28_1 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_28, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_28_1.place(x = 920, y = 350)
        
        self.rad_28_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_28, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_28_2.place(x = 920, y = 400)

        self.rad_28_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_28, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_28_3.place(x = 920, y = 450)

        self.rad_28_4 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_28, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_28_4.place(x = 920, y = 500)

    def rb_D_28(self):
        self.rad_28_1.destroy()
        self.rad_28_2.destroy()
        self.rad_28_3.destroy()
        self.rad_28_4.destroy()
rb_28 = radbutton_28()

class radbutton_29():
    def rb_P_29(self):
        self.rad_29_1 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_29, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_29_1.place(x = 920, y = 350)
        
        self.rad_29_2 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_29, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_29_2.place(x = 920, y = 400)

        self.rad_29_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_29, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_29_3.place(x = 920, y = 450)

        self.rad_29_4 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_29, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_29_4.place(x = 920, y = 500)

    def rb_D_29(self):
        self.rad_29_1.destroy()
        self.rad_29_2.destroy()
        self.rad_29_3.destroy()
        self.rad_29_4.destroy()
rb_29 = radbutton_29()

class radbutton_30():
    def rb_P_30(self):
        self.rad_30_1 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_30, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_30_1.place(x = 920, y = 350)
        
        self.rad_30_2 = Radiobutton(quiz, text = "Dragon", value = "Dragon", variable = a_30, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_30_2.place(x = 920, y = 400)

        self.rad_30_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_30, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_30_3.place(x = 920, y = 450)

        self.rad_30_4 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_30, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_30_4.place(x = 920, y = 500)

    def rb_D_30(self):
        self.rad_30_1.destroy()
        self.rad_30_2.destroy()
        self.rad_30_3.destroy()
        self.rad_30_4.destroy()
rb_30 = radbutton_30()

class radbutton_31():
    def rb_P_31(self):
        self.rad_31_1 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_31, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_31_1.place(x = 920, y = 350)
        
        self.rad_31_2 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_31, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_31_2.place(x = 920, y = 400)

        self.rad_31_3 = Radiobutton(quiz, text = "Dragon", value = "Dragon", variable = a_31, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_31_3.place(x = 920, y = 450)

        self.rad_31_4 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_31, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_31_4.place(x = 920, y = 500)

    def rb_D_31(self):
        self.rad_31_1.destroy()
        self.rad_31_2.destroy()
        self.rad_31_3.destroy()
        self.rad_31_4.destroy()
rb_31 = radbutton_31()

class radbutton_32():
    def rb_P_32(self):
        self.rad_32_1 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_32, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_32_1.place(x = 920, y = 350)
        
        self.rad_32_2 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_32, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_32_2.place(x = 920, y = 400)

        self.rad_32_3 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_32, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_32_3.place(x = 920, y = 450)

        self.rad_32_4 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_32, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_32_4.place(x = 920, y = 500)

    def rb_D_32(self):
        self.rad_32_1.destroy()
        self.rad_32_2.destroy()
        self.rad_32_3.destroy()
        self.rad_32_4.destroy()
rb_32 = radbutton_32()

class radbutton_33():
    def rb_P_33(self):
        self.rad_33_1 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_33, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_33_1.place(x = 920, y = 350)
        
        self.rad_33_2 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_33, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_33_2.place(x = 920, y = 400)

        self.rad_33_3 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_33, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_33_3.place(x = 920, y = 450)

        self.rad_33_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_33, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_33_4.place(x = 920, y = 500)

    def rb_D_33(self):
        self.rad_33_1.destroy()
        self.rad_33_2.destroy()
        self.rad_33_3.destroy()
        self.rad_33_4.destroy()
rb_33 = radbutton_33()

class radbutton_34():
    def rb_P_34(self):
        self.rad_34_1 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_34, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_34_1.place(x = 920, y = 350)
        
        self.rad_34_2 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_34, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_34_2.place(x = 920, y = 400)

        self.rad_34_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_34, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_34_3.place(x = 920, y = 450)

        self.rad_34_4 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_34, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_34_4.place(x = 920, y = 500)

    def rb_D_34(self):
        self.rad_34_1.destroy()
        self.rad_34_2.destroy()
        self.rad_34_3.destroy()
        self.rad_34_4.destroy()
rb_34 = radbutton_34()

class radbutton_35():
    def rb_P_35(self):
        self.rad_35_1 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_35, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_35_1.place(x = 920, y = 350)
        
        self.rad_35_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_35, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_35_2.place(x = 920, y = 400)

        self.rad_35_3 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_35, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_35_3.place(x = 920, y = 450)

        self.rad_35_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_35, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_35_4.place(x = 920, y = 500)

    def rb_D_35(self):
        self.rad_35_1.destroy()
        self.rad_35_2.destroy()
        self.rad_35_3.destroy()
        self.rad_35_4.destroy()
rb_35 = radbutton_35()

class radbutton_36():
    def rb_P_36(self):
        self.rad_36_1 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_36, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_36_1.place(x = 920, y = 350)
        
        self.rad_36_2 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_36, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_36_2.place(x = 920, y = 400)

        self.rad_36_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_36, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_36_3.place(x = 920, y = 450)

        self.rad_36_4 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_36, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_36_4.place(x = 920, y = 500)

    def rb_D_36(self):
        self.rad_36_1.destroy()
        self.rad_36_2.destroy()
        self.rad_36_3.destroy()
        self.rad_36_4.destroy()
rb_36 = radbutton_36()

class radbutton_37():
    def rb_P_37(self):
        self.rad_37_1 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_37, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_37_1.place(x = 920, y = 350)
        
        self.rad_37_2 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_37, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_37_2.place(x = 920, y = 400)

        self.rad_37_3 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_37, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_37_3.place(x = 920, y = 450)

        self.rad_37_4 = Radiobutton(quiz, text = "Dragon", value = "Dragon", variable = a_37, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_37_4.place(x = 920, y = 500)

    def rb_D_37(self):
        self.rad_37_1.destroy()
        self.rad_37_2.destroy()
        self.rad_37_3.destroy()
        self.rad_37_4.destroy()
rb_37 = radbutton_37()

class radbutton_38():
    def rb_P_38(self):
        self.rad_38_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_38, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_38_1.place(x = 920, y = 350)
        
        self.rad_38_2 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_38, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_38_2.place(x = 920, y = 400)

        self.rad_38_3 = Radiobutton(quiz, text = "Ghost", value = "Ghost", variable = a_38, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_38_3.place(x = 920, y = 450)

        self.rad_38_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_38, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_38_4.place(x = 920, y = 500)

    def rb_D_38(self):
        self.rad_38_1.destroy()
        self.rad_38_2.destroy()
        self.rad_38_3.destroy()
        self.rad_38_4.destroy()
rb_38 = radbutton_38()

class radbutton_39():
    def rb_P_39(self):
        self.rad_39_1 = Radiobutton(quiz, text = "Ghost", value = "Ghost", variable = a_39, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_39_1.place(x = 920, y = 350)
        
        self.rad_39_2 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_39, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_39_2.place(x = 920, y = 400)

        self.rad_39_3 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_39, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_39_3.place(x = 920, y = 450)

        self.rad_39_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_39, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_39_4.place(x = 920, y = 500)

    def rb_D_39(self):
        self.rad_39_1.destroy()
        self.rad_39_2.destroy()
        self.rad_39_3.destroy()
        self.rad_39_4.destroy()
rb_39 = radbutton_39()

class radbutton_40():
    def rb_P_40(self):
        self.rad_40_1 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_40, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_40_1.place(x = 920, y = 350)
        
        self.rad_40_2 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_40, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_40_2.place(x = 920, y = 400)

        self.rad_40_3 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_40, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_40_3.place(x = 920, y = 450)

        self.rad_40_4 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_40, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_40_4.place(x = 920, y = 500)

    def rb_D_40(self):
        self.rad_40_1.destroy()
        self.rad_40_2.destroy()
        self.rad_40_3.destroy()
        self.rad_40_4.destroy()
rb_40 = radbutton_40()

class radbutton_41():
    def rb_P_41(self):
        self.rad_41_1 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_41, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_41_1.place(x = 920, y = 350)
        
        self.rad_41_2 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_41, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_41_2.place(x = 920, y = 400)

        self.rad_41_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_41, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_41_3.place(x = 920, y = 450)

        self.rad_41_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_41, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_41_4.place(x = 920, y = 500)

    def rb_D_41(self):
        self.rad_41_1.destroy()
        self.rad_41_2.destroy()
        self.rad_41_3.destroy()
        self.rad_41_4.destroy()
rb_41 = radbutton_41()

class radbutton_42():
    def rb_P_42(self):
        self.rad_42_1 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_42, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_42_1.place(x = 920, y = 350)
        
        self.rad_42_2 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_42, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_42_2.place(x = 920, y = 400)

        self.rad_42_3 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_42, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_42_3.place(x = 920, y = 450)

        self.rad_42_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_42, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_42_4.place(x = 920, y = 500)

    def rb_D_42(self):
        self.rad_42_1.destroy()
        self.rad_42_2.destroy()
        self.rad_42_3.destroy()
        self.rad_42_4.destroy()
rb_42 = radbutton_42()

class radbutton_43():
    def rb_P_43(self):
        self.rad_43_1 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_43, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_43_1.place(x = 920, y = 350)
        
        self.rad_43_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_43, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_43_2.place(x = 920, y = 400)

        self.rad_43_3 = Radiobutton(quiz, text = "Rock", value = "Rock", variable = a_43, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_43_3.place(x = 920, y = 450)

        self.rad_43_4 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_43, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_43_4.place(x = 920, y = 500)

    def rb_D_43(self):
        self.rad_43_1.destroy()
        self.rad_43_2.destroy()
        self.rad_43_3.destroy()
        self.rad_43_4.destroy()
rb_43 = radbutton_43()

class radbutton_44():
    def rb_P_44(self):
        self.rad_44_1 = Radiobutton(quiz, text = "Grass", value = "Grass", variable = a_44, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_44_1.place(x = 920, y = 350)
        
        self.rad_44_2 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_44, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_44_2.place(x = 920, y = 400)

        self.rad_44_3 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_44, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_44_3.place(x = 920, y = 450)

        self.rad_44_4 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_44, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_44_4.place(x = 920, y = 500)

    def rb_D_44(self):
        self.rad_44_1.destroy()
        self.rad_44_2.destroy()
        self.rad_44_3.destroy()
        self.rad_44_4.destroy()
rb_44 = radbutton_44()

class radbutton_45():
    def rb_P_45(self):
        self.rad_45_1 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_45, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_45_1.place(x = 920, y = 350)
        
        self.rad_45_2 = Radiobutton(quiz, text = "Ground", value = "Ground", variable = a_45, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_45_2.place(x = 920, y = 400)

        self.rad_45_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_45, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_45_3.place(x = 920, y = 450)

        self.rad_45_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_45, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_45_4.place(x = 920, y = 500)

    def rb_D_45(self):
        self.rad_45_1.destroy()
        self.rad_45_2.destroy()
        self.rad_45_3.destroy()
        self.rad_45_4.destroy()
rb_45 = radbutton_45()

class radbutton_46():
    def rb_P_46(self):
        self.rad_46_1 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_46, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_46_1.place(x = 920, y = 350)
        
        self.rad_46_2 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_46, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_46_2.place(x = 920, y = 400)

        self.rad_46_3 = Radiobutton(quiz, text = "Fighting", value = "Fighting", variable = a_46, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_46_3.place(x = 920, y = 450)

        self.rad_46_4 = Radiobutton(quiz, text = "Psychic", value = "Psychic", variable = a_46, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_46_4.place(x = 920, y = 500)

    def rb_D_46(self):
        self.rad_46_1.destroy()
        self.rad_46_2.destroy()
        self.rad_46_3.destroy()
        self.rad_46_4.destroy()
rb_46 = radbutton_46()

class radbutton_47():
    def rb_P_47(self):
        self.rad_47_1 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_47, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_47_1.place(x = 920, y = 350)
        
        self.rad_47_2 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_47, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_47_2.place(x = 920, y = 400)

        self.rad_47_3 = Radiobutton(quiz, text = "Flying", value = "Flying", variable = a_47, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_47_3.place(x = 920, y = 450)

        self.rad_47_4 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_47, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_47_4.place(x = 920, y = 500)

    def rb_D_47(self):
        self.rad_47_1.destroy()
        self.rad_47_2.destroy()
        self.rad_47_3.destroy()
        self.rad_47_4.destroy()
rb_47 = radbutton_47()

class radbutton_48():
    def rb_P_48(self):
        self.rad_48_1 = Radiobutton(quiz, text = "Fire", value = "Fire", variable = a_48, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_48_1.place(x = 920, y = 350)
        
        self.rad_48_2 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_48, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_48_2.place(x = 920, y = 400)

        self.rad_48_3 = Radiobutton(quiz, text = "Dark", value = "Dark", variable = a_48, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_48_3.place(x = 920, y = 450)

        self.rad_48_4 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_48, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_48_4.place(x = 920, y = 500)

    def rb_D_48(self):
        self.rad_48_1.destroy()
        self.rad_48_2.destroy()
        self.rad_48_3.destroy()
        self.rad_48_4.destroy()
rb_48 = radbutton_48()

class radbutton_49():
    def rb_P_49(self):
        self.rad_49_1 = Radiobutton(quiz, text = "Bug", value = "Bug", variable = a_49, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_49_1.place(x = 920, y = 350)
        
        self.rad_49_2 = Radiobutton(quiz, text = "Poison", value = "Poison", variable = a_49, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_49_2.place(x = 920, y = 400)

        self.rad_49_3 = Radiobutton(quiz, text = "Normal", value = "Normal", variable = a_49, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_49_3.place(x = 920, y = 450)

        self.rad_49_4 = Radiobutton(quiz, text = "Water", value = "Water", variable = a_49, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_49_4.place(x = 920, y = 500)

    def rb_D_49(self):
        self.rad_49_1.destroy()
        self.rad_49_2.destroy()
        self.rad_49_3.destroy()
        self.rad_49_4.destroy()
rb_49 = radbutton_49()

class radbutton_50():
    def rb_P_50(self):
        self.rad_50_1 = Radiobutton(quiz, text = "Ice", value = "Ice", variable = a_50, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_50_1.place(x = 920, y = 350)
        
        self.rad_50_2 = Radiobutton(quiz, text = "Fairy", value = "Fairy", variable = a_50, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_50_2.place(x = 920, y = 400)

        self.rad_50_3 = Radiobutton(quiz, text = "Steel", value = "Steel", variable = a_50, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_50_3.place(x = 920, y = 450)

        self.rad_50_4 = Radiobutton(quiz, text = "Electric", value = "Electric", variable = a_50, bg = "RoyalBlue", fg = "Black", font = ("OCR A Extended", 20))
        self.rad_50_4.place(x = 920, y = 500)

    def rb_D_50(self):
        self.rad_50_1.destroy()
        self.rad_50_2.destroy()
        self.rad_50_3.destroy()
        self.rad_50_4.destroy()
rb_50 = radbutton_50()

##Pokemon Quiz

def pokemon_quiz_01():
    if a_01.get() == "Psychic":
        
        right_answer()
        increment()
        
        rad_1_1.destroy()
        rad_1_2.destroy()
        rad_1_3.destroy()
        rad_1_4.destroy()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_02)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_02())

    else:
        rad_1_1.destroy()
        rad_1_2.destroy()
        rad_1_3.destroy()
        rad_1_4.destroy()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Psychic", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_02)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_02())

def pokemon_quiz_02():
    if a_02.get() == "Poison":
        
        right_answer()
        rb_02.rb_D_02()
        
        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_03)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_03())

    else:
        rb_02.rb_D_02() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Poison", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_03)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_03())

def pokemon_quiz_03():
    if a_03.get() == "Grass":

        right_answer()
        rb_03.rb_D_03()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_04)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_04())

    else:
        rb_03.rb_D_03() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Grass", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_04)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_04())

def pokemon_quiz_04():
    if a_04.get() == "Poison":
        
        right_answer()
        rb_04.rb_D_04()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_05)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_05())

    else:
        rb_04.rb_D_04() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Poison", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_05)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_05())

def pokemon_quiz_05():
    if a_05.get() == "Poison":
        
        right_answer()
        rb_05.rb_D_05()

        increment()
       
        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_06)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_06())

    else:
        rb_05.rb_D_05() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Poison", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_06)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_06())

def pokemon_quiz_06():
    if a_06.get() == "Bug":
        
        right_answer()
        rb_06.rb_D_06()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_07)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_07())

    else:
        rb_06.rb_D_06() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Bug", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_07)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_07())

def pokemon_quiz_07():
    if a_07.get() == "Bug":
        
        right_answer()
        rb_07.rb_D_07()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_08)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_08())

    else:
        rb_07.rb_D_07() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Bug", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_08)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_08())

def pokemon_quiz_08():
    if a_08.get() == "Fire":
        
        right_answer()
        rb_08.rb_D_08()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_09)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_09())

    else:
        rb_08.rb_D_08() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Fire", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_09)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_09())

def pokemon_quiz_09():
    if a_09.get() == "Water":
        
        right_answer()
        rb_09.rb_D_09()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_10)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_10())

    else:
        rb_09.rb_D_09() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_10)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_10())

def pokemon_quiz_10():
    if a_10.get() == "Grass":
        
        right_answer()
        rb_10.rb_D_10()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_11)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_11())

    else:
        rb_10.rb_D_10() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Grass", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_11)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_11())

def pokemon_quiz_11():
    if a_11.get() == "Ground":
        
        right_answer()
        rb_11.rb_D_11()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_12)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_12())

    else:
        rb_11.rb_D_11() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Ground", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_12)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_12())

def pokemon_quiz_12():
    if a_12.get() == "Ground":
        
        right_answer()
        rb_12.rb_D_12()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_13)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_13())

    else:
        rb_12.rb_D_12() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Ground", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_13)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_13())

def pokemon_quiz_13():
    if a_13.get() == "Normal":
        
        right_answer()
        rb_13.rb_D_13()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_14)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_14())

    else:
        rb_13.rb_D_13() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_14)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_14())

def pokemon_quiz_14():
    if a_14.get() == "Flying":
        
        right_answer()
        rb_14.rb_D_14()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_15)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_15())

    else:
        rb_14.rb_D_14() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Flying", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_15)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_15())

def pokemon_quiz_15():
    if a_15.get() == "Normal":
        
        right_answer()
        rb_15.rb_D_15()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_16)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_16())

    else:
        rb_15.rb_D_15() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_16)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_16())

def pokemon_quiz_16():
    if a_16.get() == "Grass":
        
        right_answer()
        rb_16.rb_D_16()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_17)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_17())

    else:
        rb_16.rb_D_16() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Grass", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_17)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_17())

def pokemon_quiz_17():
    if a_17.get() == "Ghost":
        
        right_answer()
        rb_17.rb_D_17()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_18)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_18())

    else:
        rb_17.rb_D_17() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Ghost", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_18)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_18())

def pokemon_quiz_18():
    if a_18.get() == "Rock":
        
        right_answer()
        rb_18.rb_D_18()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_19)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_19())

    else:
        rb_18.rb_D_18() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Rock", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_19)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_19())

def pokemon_quiz_19():
    if a_19.get() == "Rock":
        
        right_answer()
        rb_19.rb_D_19()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_20)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_19())

    else:
        rb_19.rb_D_19() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Rock", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_20)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_20())

def pokemon_quiz_20():
    if a_20.get() == "Fighting":
        
        right_answer()
        rb_20.rb_D_20()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_21)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_21())

    else:
        rb_20.rb_D_20() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Fighting", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_21)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_21())

def pokemon_quiz_21():
    if a_21.get() == "Psychic":
        
        right_answer()
        rb_21.rb_D_21()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_22)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_22())

    else:
        rb_21.rb_D_21() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Psychic", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_22)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_22())

def pokemon_quiz_22():
    if a_22.get() == "Fairy":
        
        right_answer()
        rb_22.rb_D_22()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_23)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_23())

    else:
        rb_22.rb_D_22() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Fairy", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_23)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_23())

def pokemon_quiz_23():
    if a_23.get() == "Rock":
        
        right_answer()
        rb_23.rb_D_23()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_24)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_24())

    else:
        rb_23.rb_D_23() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Rock", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_24)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_24())

def pokemon_quiz_24():
    if a_24.get() == "Water":
        
        right_answer()
        rb_24.rb_D_24()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_25)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_25())

    else:
        rb_24.rb_D_24() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_25)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_25())

def pokemon_quiz_25():
    if a_25.get() == "Poison":
        
        right_answer()
        rb_25.rb_D_25()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_26)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_26())

    else:
        rb_25.rb_D_25() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Poison", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_26)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_26())

def pokemon_quiz_26():
    if a_26.get() == "Water":
        
        right_answer()
        rb_26.rb_D_26()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_27)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_27())

    else:
        rb_26.rb_D_26() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_27)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_27())

def pokemon_quiz_27():
    if a_27.get() == "Normal":
        
        right_answer()
        rb_27.rb_D_27()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_28)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_28())

    else:
        rb_27.rb_D_27() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_28)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_28())

def pokemon_quiz_28():
    if a_28.get() == "Water":
        
        right_answer()
        rb_28.rb_D_28()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_29)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_29())

    else:
        rb_28.rb_D_28() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_29)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_29())

def pokemon_quiz_29():
    if a_29.get() == "Normal":
        
        right_answer()
        rb_29.rb_D_29()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_30)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_30())

    else:
        rb_29.rb_D_29() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_30)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_30())

def pokemon_quiz_30():
    if a_30.get() == "Bug":
        
        right_answer()
        rb_30.rb_D_30()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_31)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_31())

    else:
        rb_30.rb_D_30() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Bug", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_31)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_31())

def pokemon_quiz_31():
    if a_31.get() == "Psychic":
        
        right_answer()
        rb_31.rb_D_31()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_32)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_32())

    else:
        rb_31.rb_D_31() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Psychic", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_32)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_32())

def pokemon_quiz_32():
    if a_32.get() == "Psychic":
        
        right_answer()
        rb_32.rb_D_32()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_33)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_33())

    else:
        rb_32.rb_D_32() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Psychic", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_33)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_33())

def pokemon_quiz_33():
    if a_33.get() == "Poison":
        
        right_answer()
        rb_33.rb_D_33()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_34)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_34())

    else:
        rb_33.rb_D_33() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Poison", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_34)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_34())

def pokemon_quiz_34():
    if a_34.get() == "Rock":
        
        right_answer()
        rb_34.rb_D_34()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_35)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_35())

    else:
        rb_34.rb_D_34() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Rock", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_35)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_35())

def pokemon_quiz_35():
    if a_35.get() == "Rock":
        
        right_answer()
        rb_35.rb_D_35()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_36)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_36())

    else:
        rb_35.rb_D_35() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Rock", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_36)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_36())

def pokemon_quiz_36():
    if a_36.get() == "Flying":
        
        right_answer()
        rb_36.rb_D_36()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_37)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_37())

    else:
        rb_36.rb_D_36() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Flying", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_37)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_37())

def pokemon_quiz_37():
    if a_37.get() == "Electric":
        
        right_answer()
        rb_37.rb_D_37()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_38)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_38())

    else:
        rb_37.rb_D_37() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Electric", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_38)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_38())

def pokemon_quiz_38():
    if a_38.get() == "Water":
        
        right_answer()
        rb_38.rb_D_38()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_39)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_39())

    else:
        rb_38.rb_D_38() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_39)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_39())

def pokemon_quiz_39():
    if a_39.get() == "Water":
        
        right_answer()
        rb_39.rb_D_39()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_40)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_40())

    else:
        rb_39.rb_D_39() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_40)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_40())

def pokemon_quiz_40():
    if a_40.get() == "Bug":
        
        right_answer()
        rb_40.rb_D_40()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_41)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_41())

    else:
        rb_40.rb_D_40() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Bug", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_41)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_41())

def pokemon_quiz_41():
    if a_41.get() == "Normal":
        
        right_answer()
        rb_41.rb_D_41()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_42)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_42())

    else:
        rb_41.rb_D_41() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_42)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_42())

def pokemon_quiz_42():
    if a_42.get() == "Water":
        
        right_answer()
        rb_42.rb_D_42()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_43)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_43())

    else:
        rb_42.rb_D_42() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_43)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_43())

def pokemon_quiz_43():
    if a_43.get() == "Water":
        
        right_answer()
        rb_43.rb_D_43()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_44)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_44())

    else:
        rb_43.rb_D_43() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_44)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_44())

def pokemon_quiz_44():
    if a_44.get() == "Grass":
        
        right_answer()
        rb_44.rb_D_44()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_45)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_45())

    else:
        rb_44.rb_D_44() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Grass", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_45)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_45())

def pokemon_quiz_45():
    if a_45.get() == "Normal":
        
        right_answer()
        rb_45.rb_D_45()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_46)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_46())

    else:
        rb_45.rb_D_45() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_46)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_46())

def pokemon_quiz_46():
    if a_46.get() == "Bug":
        
        right_answer()
        rb_46.rb_D_46()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_47)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_47())

    else:
        rb_46.rb_D_46() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Bug", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_47)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_47())

def pokemon_quiz_47():
    if a_47.get() == "Flying":
        
        right_answer()
        rb_47.rb_D_47()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_48)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_48())

    else:
        rb_47.rb_D_47() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Flying", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_48)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_48())

def pokemon_quiz_48():
    if a_48.get() == "Normal":
        
        right_answer()
        rb_48.rb_D_48()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_49)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_49())

    else:
        rb_48.rb_D_48() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Normal", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_49)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_49())

def pokemon_quiz_49():
    if a_49.get() == "Water":
        
        right_answer()
        rb_49.rb_D_49()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_50)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_50())

    else:
        rb_49.rb_D_49() 

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Water", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_50)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_50())

def pokemon_quiz_50():
    if a_50.get() == "Steel":
        
        right_answer()
        rb_50.rb_D_50()

        increment()

        ##Button for Viewing Score

        but_2 = Button(quiz, text = "VIEW SCORE", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = view_score)
        but_2.place(x = 920, y = 550)

    else:
        rb_50.rb_D_50()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 480)
        lbl_2.configure(text = "The answer is Wrong: " "Steel", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        ##Button for Viewing Score

        but_2 = Button(quiz, text = "VIEW SCORE", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = view_score)
        but_2.place(x = 920, y = 550)
 
##Submit Button

but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_01)
but_1.place(x = 920, y = 550)
quiz.bind("<Return>", lambda event:pokemon_quiz_01())

##Quit Game Button

quit_g_01 = Image.open("./projimg26.png")
resized = quit_g_01.resize((50,35))
quit_g_02 = ImageTk.PhotoImage(resized)
quit_g_lbl_01 = Label(quiz, text = "", image = quit_g_02).place(x = 1320, y = 735)

quit_but = Button(quiz, text = "QUIT", bg = "Royal Blue", fg = "Black", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 5, height = 1, command = quit_game)
quit_but.place(x = 1462, y = 735)

##Change Game Button

change_g_01 = Image.open("./projimg25.png")
resized = change_g_01.resize((50,35))
change_g_02 = ImageTk.PhotoImage(resized)
change_g_lbl_01 = Label(quiz, text = "", image = change_g_02).place(x = 1320, y = 695)

change_g_but = Button(quiz,text = "CHANGE GAME", bg = "Royal Blue", fg = "Black", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 12, height = 1, command = change_game)
change_g_but.place(x = 1380, y = 695)

quiz.mainloop()

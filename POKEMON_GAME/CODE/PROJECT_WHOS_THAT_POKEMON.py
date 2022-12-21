##Import Libraries

from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from random import *
import pymysql

##New Window

quiz = Tk()
quiz.title("Pokemon Quiz")
quiz.geometry("1532x790")
quiz.config(bg = "RoyalBlue")

img_00 = PhotoImage(file = "./WHOS-THAT-POKEMON.png")
Label(quiz, text = "", image = img_00).pack()

##Icon

quiz.wm_iconbitmap(r"C:\Users\joseph jenis\AppData\Local\Programs\Python\Python310\Proj\projimg02.ico")

##Audio

def audio():
    mixer.init()
    mixer.music.load("./whos_that_pokemon_audio.wav")
    mixer.music.play()

##Empty Label

def empty_label():
    lbl_00 = Label(quiz, bg = "RoyalBlue", font = ( "OCR A Extended", 20, "bold"), width = 35, height = 1)
    lbl_00.place(x = 750, y = 500)

##Right Answer Statement

def right_answer():
    r_ans = Label(quiz, text = "", bg = "Yellow")
    r_ans.place(x = 750, y = 500)
    r_ans.configure(text = "The answer is Right", font = ("OCR A Extended", 20, "bold"), width = 35, height = 1)
    r_ans.configure(bg = "Green")

##Entry Box

def entry_box():
    answer_entry = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0)
    answer_entry.place(x = 750, y = 500)

##Quit Game 

def quit_game():
    quiz.destroy()

##Change Game
    
def change_game():
    quiz.destroy()
    import PROJECT_GAME_OPTION

##Score

score_counter_WTP = IntVar()
score_counter_WTP = 0

def increment():
    global score_counter_WTP
    score_counter_WTP = score_counter_WTP + 1

def view_score():   
    
    score_label = Label(quiz, text = score_counter_WTP, bg = "Black", fg = "White", font = ("OCR A Extended", 30), width = 65, height = 15) 
    score_label.pack()

    score_label_0 = Label(quiz, text = "Your Score is: ", bg = "Black", fg = "White", font = ("OCR A Extended", 30), width = 65, height = 5) 
    score_label_0.place(x = 0, y = 0)

    quit_but = Button(quiz, text = "QUIT", bg = "Black", fg = "White", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 5, height = 1, command = quit_game)
    quit_but.place(x = 1462, y = 735)

    change_g_but = Button(quiz,text = "CHANGE GAME", bg = "Black", fg = "White", bd = 0, cursor = "hand2", font = ("OCR A Extended", 15), width = 12, height = 1, command = change_game)
    change_g_but.place(x = 1380, y = 695)

    ##Creating Score column in MySql Database

    try:
        con = pymysql.connect(host = "localhost", user = "root", password = "root", database = "game_register")
        mycursor = con.cursor()

        query = "ALTER TABLE score_game_1 ADD Score_WTP int(20)"
        mycursor.execute(query)
        con.commit()
        con.close()

    except:
        mycursor.execute("use game_register")

    mycursor.execute("insert into score_game_1 (Score_WTP) values ('{}');".format(score_counter_WTP))
    con.commit()
    con.close()

##Entrybox for Answers

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

a_e_01 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_01)
a_e_01.place(x = 750, y = 500)

class ANS_ENT():
    def ans_ent_02(self):
        self.a_e_02 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_02)
        self.a_e_02.place(x = 750, y = 500)

    def ans_ent_03(self):
        self.a_e_03 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_03)
        self.a_e_03.place(x = 750, y = 500)

    def ans_ent_04(self):
        self.a_e_04 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_04)
        self.a_e_04.place(x = 750, y = 500)

    def ans_ent_05(self):
        self.a_e_05 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_05)
        self.a_e_05.place(x = 750, y = 500)

    def ans_ent_06(self):
        self.a_e_06 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_06)
        self.a_e_06.place(x = 750, y = 500)

    def ans_ent_07(self):
        self.a_e_07 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_07)
        self.a_e_07.place(x = 750, y = 500)

    def ans_ent_08(self):
        self.a_e_08 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_08)
        self.a_e_08.place(x = 750, y = 500)

    def ans_ent_09(self):
        self.a_e_09 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_09)
        self.a_e_09.place(x = 750, y = 500)

    def ans_ent_10(self):
        self.a_e_10 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_10)
        self.a_e_10.place(x = 750, y = 500)

    def ans_ent_11(self):
        self.a_e_11 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_11)
        self.a_e_11.place(x = 750, y = 500)

    def ans_ent_12(self):
        self.a_e_12 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_12)
        self.a_e_12.place(x = 750, y = 500)

    def ans_ent_13(self):
        self.a_e_13 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_13)
        self.a_e_13.place(x = 750, y = 500)

    def ans_ent_14(self):
        self.a_e_14 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_14)
        self.a_e_14.place(x = 750, y = 500)

    def ans_ent_15(self):
        self.a_e_15 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_15)
        self.a_e_15.place(x = 750, y = 500)

    def ans_ent_16(self):
        self.a_e_16 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_16)
        self.a_e_16.place(x = 750, y = 500)

    def ans_ent_17(self):
        self.a_e_17 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_17)
        self.a_e_17.place(x = 750, y = 500)

    def ans_ent_18(self):
        self.a_e_18 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_18)
        self.a_e_18.place(x = 750, y = 500)

    def ans_ent_19(self):
        self.a_e_19 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_19)
        self.a_e_19.place(x = 750, y = 500)

    def ans_ent_20(self):
        self.a_e_20 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_20)
        self.a_e_20.place(x = 750, y = 500)

    def ans_ent_21(self):
        self.a_e_21 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_21)
        self.a_e_21.place(x = 750, y = 500)

    def ans_ent_22(self):
        self.a_e_22 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_22)
        self.a_e_22.place(x = 750, y = 500)

    def ans_ent_23(self):
        self.a_e_23 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_23)
        self.a_e_23.place(x = 750, y = 500)

    def ans_ent_24(self):
        self.a_e_24 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_24)
        self.a_e_24.place(x = 750, y = 500)

    def ans_ent_25(self):
        self.a_e_25 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_25)
        self.a_e_25.place(x = 750, y = 500)

    def ans_ent_26(self):
        self.a_e_26 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_26)
        self.a_e_26.place(x = 750, y = 500)

    def ans_ent_27(self):
        self.a_e_27 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_27)
        self.a_e_27.place(x = 750, y = 500)

    def ans_ent_28(self):
        self.a_e_28 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_28)
        self.a_e_28.place(x = 750, y = 500)

    def ans_ent_29(self):
        self.a_e_29 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_29)
        self.a_e_29.place(x = 750, y = 500)

    def ans_ent_30(self):
        self.a_e_30 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_30)
        self.a_e_30.place(x = 750, y = 500)

    def ans_ent_31(self):
        self.a_e_31 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_31)
        self.a_e_31.place(x = 750, y = 500)

    def ans_ent_32(self):
        self.a_e_32 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_32)
        self.a_e_32.place(x = 750, y = 500)

    def ans_ent_33(self):
        self.a_e_33 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_33)
        self.a_e_33.place(x = 750, y = 500)

    def ans_ent_34(self):
        self.a_e_34 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_34)
        self.a_e_34.place(x = 750, y = 500)

    def ans_ent_35(self):
        self.a_e_35 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_35)
        self.a_e_35.place(x = 750, y = 500)

    def ans_ent_36(self):
        self.a_e_36 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_36)
        self.a_e_36.place(x = 750, y = 500)

    def ans_ent_37(self):
        self.a_e_37 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_37)
        self.a_e_37.place(x = 750, y = 500)

    def ans_ent_38(self):
        self.a_e_38 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_38)
        self.a_e_38.place(x = 750, y = 500)

    def ans_ent_39(self):
        self.a_e_39 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_39)
        self.a_e_39.place(x = 750, y = 500)

    def ans_ent_40(self):
        self.a_e_40 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_40)
        self.a_e_40.place(x = 750, y = 500)

    def ans_ent_41(self):
        self.a_e_41 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_41)
        self.a_e_41.place(x = 750, y = 500)

    def ans_ent_42(self):
        self.a_e_42 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_42)
        self.a_e_42.place(x = 750, y = 500)

    def ans_ent_43(self):
        self.a_e_43 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_43)
        self.a_e_43.place(x = 750, y = 500)

    def ans_ent_44(self):
        self.a_e_44 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_44)
        self.a_e_44.place(x = 750, y = 500)

    def ans_ent_45(self):
        self.a_e_45 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_45)
        self.a_e_45.place(x = 750, y = 500)

    def ans_ent_46(self):
        self.a_e_46 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_46)
        self.a_e_46.place(x = 750, y = 500)

    def ans_ent_47(self):
        self.a_e_47 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_47)
        self.a_e_47.place(x = 750, y = 500)

    def ans_ent_48(self):
        self.a_e_48 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_48)
        self.a_e_48.place(x = 750, y = 500)

    def ans_ent_49(self):
        self.a_e_49 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_49)
        self.a_e_49.place(x = 750, y = 500)

    def ans_ent_50(self):
        self.a_e_50 = Entry(quiz, width = 35, bg = "White", font = ("OCR A Extended", 20, "bold"), bd = 0, textvariable = a_50)
        self.a_e_50.place(x = 750, y = 500)

AE = ANS_ENT()

##Question Image
    
q_image_01 = Image.open('./Question_Image/pokemon_01.png')
resized = q_image_01.resize((500,400))
q_image_02 = ImageTk.PhotoImage(resized)
lbl_1 = Label(quiz, text = "", image = q_image_02).place(x = 145, y = 300)

audio()

class QUEST_IMG():
    def question_image_02(self):
        q_image_01 = Image.open("./Question_Image/pokemon_02.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()
      
        audio()

        AE.ans_ent_02()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_02)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_02())

    def question_image_03(self):
        q_image_01 = Image.open("./Question_Image/pokemon_03.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_03()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_03)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_03())

    def question_image_04(self):
        q_image_01 = Image.open("./Question_Image/pokemon_04.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_04()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_04)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_04())

    def question_image_05(self):
        q_image_01 = Image.open("./Question_Image/pokemon_05.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_05()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_05)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_05())

    def question_image_06(self):
        q_image_01 = Image.open("./Question_Image/pokemon_06.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_06()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_06)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_06())

    def question_image_07(self):
        q_image_01 = Image.open("./Question_Image/pokemon_07.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_07()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_07)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_07())

    def question_image_08(self):
        q_image_01 = Image.open("./Question_Image/pokemon_08.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_08()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_08)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_08())

    def question_image_09(self):
        q_image_01 = Image.open("./Question_Image/pokemon_09.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_09()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_09)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_09())

    def question_image_10(self):
        q_image_01 = Image.open("./Question_Image/pokemon_10.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_10()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_10)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_10())

    def question_image_11(self):
        q_image_01 = Image.open("./Question_Image/pokemon_11.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_11()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_11)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_11())

    def question_image_12(self):
        q_image_01 = Image.open("./Question_Image/pokemon_12.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_12()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_12)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_12())

    def question_image_13(self):
        q_image_01 = Image.open("./Question_Image/pokemon_13.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_13()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_13)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_13())

    def question_image_14(self):
        q_image_01 = Image.open("./Question_Image/pokemon_14.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_14()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_14)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_14())

    def question_image_15(self):
        q_image_01 = Image.open("./Question_Image/pokemon_15.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_15()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_15)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_15())

    def question_image_16(self):
        q_image_01 = Image.open("./Question_Image/pokemon_16.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_16()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_16)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_16())

    def question_image_17(self):
        q_image_01 = Image.open("./Question_Image/pokemon_17.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_17()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_17)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_17())

    def question_image_18(self):
        q_image_01 = Image.open("./Question_Image/pokemon_18.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_18()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_18)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_18())

    def question_image_19(self):
        q_image_01 = Image.open("./Question_Image/pokemon_19.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_19()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_19)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_19())

    def question_image_20(self):
        q_image_01 = Image.open("./Question_Image/pokemon_20.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_20()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_20)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_20())

    def question_image_21(self):
        q_image_01 = Image.open("./Question_Image/pokemon_21.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_21()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_21)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_21())

    def question_image_22(self):
        q_image_01 = Image.open("./Question_Image/pokemon_22.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_22()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_22)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_22())

    def question_image_23(self):
        q_image_01 = Image.open("./Question_Image/pokemon_23.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_23()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_23)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_23())

    def question_image_24(self):
        q_image_01 = Image.open("./Question_Image/pokemon_24.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_24()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_24)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_24())

    def question_image_25(self):
        q_image_01 = Image.open("./Question_Image/pokemon_25.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_25()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_25)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_25())

    def question_image_26(self):
        q_image_01 = Image.open("./Question_Image/pokemon_26.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_26()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_26)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_26())

    def question_image_27(self):
        q_image_01 = Image.open("./Question_Image/pokemon_27.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_27()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_27)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_27())

    def question_image_28(self):
        q_image_01 = Image.open("./Question_Image/pokemon_28.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_28()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_28)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_28())

    def question_image_29(self):
        q_image_01 = Image.open("./Question_Image/pokemon_29.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_29()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_29)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_29())

    def question_image_30(self):
        q_image_01 = Image.open("./Question_Image/pokemon_30.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_30()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_30)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_30())

    def question_image_31(self):
        q_image_01 = Image.open("./Question_Image/pokemon_31.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_31()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_31)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_31())

    def question_image_32(self):
        q_image_01 = Image.open("./Question_Image/pokemon_32.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_32()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_32)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_32())

    def question_image_33(self):
        q_image_01 = Image.open("./Question_Image/pokemon_33.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_33()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_33)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_33())

    def question_image_34(self):
        q_image_01 = Image.open("./Question_Image/pokemon_34.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_34()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_34)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_34())

    def question_image_35(self):
        q_image_01 = Image.open("./Question_Image/pokemon_35.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_35()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_35)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_35())

    def question_image_36(self):
        q_image_01 = Image.open("./Question_Image/pokemon_36.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_36()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_36)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_36())

    def question_image_37(self):
        q_image_01 = Image.open("./Question_Image/pokemon_37.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_37()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_37)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_37())

    def question_image_38(self):
        q_image_01 = Image.open("./Question_Image/pokemon_38.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_38()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_38)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_38())

    def question_image_39(self):
        q_image_01 = Image.open("./Question_Image/pokemon_39.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_39()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_39)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_39())

    def question_image_40(self):
        q_image_01 = Image.open("./Question_Image/pokemon_40.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_40()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_40)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_40())

    def question_image_41(self):
        q_image_01 = Image.open("./Question_Image/pokemon_41.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_41()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_41)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_41())

    def question_image_42(self):
        q_image_01 = Image.open("./Question_Image/pokemon_42.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_42()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_42)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_42())

    def question_image_43(self):
        q_image_01 = Image.open("./Question_Image/pokemon_43.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_43()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_43)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_43())

    def question_image_44(self):
        q_image_01 = Image.open("./Question_Image/pokemon_44.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_44()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_44)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_44())

    def question_image_45(self):
        q_image_01 = Image.open("./Question_Image/pokemon_45.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_45()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_45)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_45())

    def question_image_46(self):
        q_image_01 = Image.open("./Question_Image/pokemon_46.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_46()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_46)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_46())

    def question_image_47(self):
        q_image_01 = Image.open("./Question_Image/pokemon_47.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_47()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_47)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_47())

    def question_image_48(self):
        q_image_01 = Image.open("./Question_Image/pokemon_48.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_48()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_48)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_48())

    def question_image_49(self):
        q_image_01 = Image.open("./Question_Image/pokemon_49.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_49()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_49)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_49())

    def question_image_50(self):
        q_image_01 = Image.open("./Question_Image/pokemon_50.png")
        
        resized = q_image_01.resize((500,400))
        q_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = q_image_02)
        lbl_1.image = q_image_02
        lbl_1.place(x = 145, y = 300)

        empty_label()

        audio()

        AE.ans_ent_50()

        but_1 = Button(quiz, text = "SUBMIT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = pokemon_quiz_50)
        but_1.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:pokemon_quiz_50())

QI = QUEST_IMG()
    
##Answer Image
        
class ANS_IMG():    
    def answer_image_01(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_01.1.png")

        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_02(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_02.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_03(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_03.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_04(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_04.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_05(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_05.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_06(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_06.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_07(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_07.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_08(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_08.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_09(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_09.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_10(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_10.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_11(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_11.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_12(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_12.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_13(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_13.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_14(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_14.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_15(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_15.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_16(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_16.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_17(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_17.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_18(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_18.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_19(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_19.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_20(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_20.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_21(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_21.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_22(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_22.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_23(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_23.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_24(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_24.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_25(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_25.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_26(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_26.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_27(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_27.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_28(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_28.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_29(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_29.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_30(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_30.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_31(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_31.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_32(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_32.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_33(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_33.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_34(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_34.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_35(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_35.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_36(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_36.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_37(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_37.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_38(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_38.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_39(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_39.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_40(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_40.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_41(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_41.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_42(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_42.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_43(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_43.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_44(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_44.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_45(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_45.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_46(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_46.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_47(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_47.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_48(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_48.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_49(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_49.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

    def answer_image_50(self):
        a_image_01 = Image.open("./Answer_Image/pokemon_50.1.png")
        
        resized = a_image_01.resize((500,400))
        a_image_02 = ImageTk.PhotoImage(resized)
        
        lbl_1 = Label(quiz, text = "", image = a_image_02)
        lbl_1.image = a_image_02
        lbl_1.place(x = 145, y = 300)

AI = ANS_IMG()

##Pokemon Quiz

def pokemon_quiz_01():
    if a_01.get() == "Alakazam":
        AI.answer_image_01()
        
        right_answer()

        increment()
        
        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_02)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_02())

    else:
        AI.answer_image_01()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Alakazam", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_02)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_02())

def pokemon_quiz_02():
    if a_02.get() == "Arbok":
        AI.answer_image_02()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_03)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_03())

    else:
        AI.answer_image_02()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Arbok", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_03)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_03())

def pokemon_quiz_03():
    if a_03.get() == "Bayleef":
        AI.answer_image_03()

        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_04)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_04())

    else:
        AI.answer_image_03()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Bayleef", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_04)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_04())

def pokemon_quiz_04():
    if a_04.get() == "Bellsprout":
        AI.answer_image_04()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_05)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_05())

    else:
        AI.answer_image_04()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Bellsprout", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_05)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_05())

def pokemon_quiz_05():
    if a_05.get() == "Bulbasaur":
        AI.answer_image_05()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_06)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_06())

    else:
        AI.answer_image_05()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Bulbasaur", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_06)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_06())

def pokemon_quiz_06():
    if a_06.get() == "Butterfree":
        AI.answer_image_06()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_07)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_07())

    else:
        AI.answer_image_06()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Butterfree", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_07)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_07())

def pokemon_quiz_07():
    if a_07.get() == "Caterpie":
        AI.answer_image_07()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_08)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_08())

    else:
        AI.answer_image_07()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Caterpie", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_08)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_08())

def pokemon_quiz_08():
    if a_08.get() == "Charizard":
        AI.answer_image_08()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_09)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_09())

    else:
        AI.answer_image_08()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Charizard", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_09)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_09())

def pokemon_quiz_09():
    if a_09.get() == "Blastoise":
        AI.answer_image_09()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_10)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_10())

    else:
        AI.answer_image_09()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Blastoise", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_10)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_10())

def pokemon_quiz_10():
    if a_10.get() == "Chikorita":
        AI.answer_image_10()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_11)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_11())

    else:
        AI.answer_image_10()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Chikorita", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_11)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_11())

def pokemon_quiz_11():
    if a_11.get() == "Cubone":
        AI.answer_image_11()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_12)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_12())

    else:
        AI.answer_image_11()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Cubone", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_12)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_12())

def pokemon_quiz_12():
    if a_12.get() == "Diglett":
        AI.answer_image_12()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_13)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_13())

    else:
        AI.answer_image_12()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Diglett", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_13)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_13())

def pokemon_quiz_13():
    if a_13.get() == "Ditto":
        AI.answer_image_13()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_14)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_14())

    else:
        AI.answer_image_13()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Ditto", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_14)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_14())

def pokemon_quiz_14():
    if a_14.get() == "Dragonite":
        AI.answer_image_14()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_15)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_15())

    else:
        AI.answer_image_14()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Dragonite", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_15)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_15())

def pokemon_quiz_15():
    if a_15.get() == "Eevee":
        AI.answer_image_15()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_16)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_16())

    else:
        AI.answer_image_15()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Eevee", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_16)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_16())

def pokemon_quiz_16():
    if a_16.get() == "Exeggutor":
        AI.answer_image_16()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_17)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_17())

    else:
        AI.answer_image_16()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Exeggutor", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_17)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_17())

def pokemon_quiz_17():
    if a_17.get() == "Gengar":
        AI.answer_image_17()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_18)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_18())

    else:
        AI.answer_image_17()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Gengar", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_18)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_18())

def pokemon_quiz_18():
    if a_18.get() == "Geodude":
        AI.answer_image_18()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_19)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_19())

    else:
        AI.answer_image_18()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Geodude", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_19)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_19())

def pokemon_quiz_19():
    if a_19.get() == "Golem":
        AI.answer_image_19()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_20)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_20())

    else:
        AI.answer_image_19()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Golem", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_20)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_20())

def pokemon_quiz_20():
    if a_20.get() == "Hitmonlee":
        AI.answer_image_20()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_21)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_21())

    else:
        AI.answer_image_20()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Hitmonlee", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_21)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_21())

def pokemon_quiz_21():
    if a_21.get() == "Hypno":
        AI.answer_image_21()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_22)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_22())

    else:
        AI.answer_image_21()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Hypno", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_22)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_22())

def pokemon_quiz_22():
    if a_22.get() == "Jigglypuff":
        AI.answer_image_22()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_23)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_23())

    else:
        AI.answer_image_22()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Jigglypuff", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_23)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_23())

def pokemon_quiz_23():
    if a_23.get() == "Kabuto":
        AI.answer_image_23()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_24)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_24())

    else:
        AI.answer_image_23()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Kabuto", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_24)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_24())

def pokemon_quiz_24():
    if a_24.get() == "Kingler":
        AI.answer_image_24()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_25)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_25())

    else:
        AI.answer_image_24()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Kingler", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_25)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_25())

def pokemon_quiz_25():
    if a_25.get() == "Koffing":
        AI.answer_image_25()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_26)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_26())

    else:
        AI.answer_image_25()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Koffing", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_26)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_26())

def pokemon_quiz_26():
    if a_26.get() == "Lapras":
        AI.answer_image_26()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_27)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_27())

    else:
        AI.answer_image_26()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Lapras", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_27)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_27())

def pokemon_quiz_27():
    if a_27.get() == "Lickitung":
        AI.answer_image_27()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_28)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_28())

    else:
        AI.answer_image_27()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Lickitung", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_28)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_28())

def pokemon_quiz_28():
    if a_28.get() == "Magikarp":
        AI.answer_image_28()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_29)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_29())

    else:
        AI.answer_image_28()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Magikarp", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_29)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_29())

def pokemon_quiz_29():
    if a_29.get() == "Meowth":
        AI.answer_image_29()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_30)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_30())

    else:
        AI.answer_image_29()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Meowth", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_30)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_30())

def pokemon_quiz_30():
    if a_30.get() == "Metapod":
        AI.answer_image_30()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_31)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_31())

    else:
        AI.answer_image_30()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Metapod", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_31)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_31())

def pokemon_quiz_31():
    if a_31.get() == "Mewtwo":
        AI.answer_image_31()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_32)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_32())

    else:
        AI.answer_image_31()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Mewtwo", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_32)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_32())

def pokemon_quiz_32():
    if a_32.get() == "Mr. Mime":
        AI.answer_image_32()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_33)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_33())

    else:
        AI.answer_image_32()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Mr. Mime", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_33)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_33())

def pokemon_quiz_33():
    if a_33.get() == "Muk":
        AI.answer_image_33()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_34)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_34())

    else:
        AI.answer_image_33()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Muk", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_34)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_34())

def pokemon_quiz_34():
    if a_34.get() == "Omanyte":
        AI.answer_image_34()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_35)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_35())

    else:
        AI.answer_image_34()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Omanyte", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_35)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_35())

def pokemon_quiz_35():
    if a_35.get() == "Onix":
        AI.answer_image_35()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_36)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_36())

    else:
        AI.answer_image_35()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Onix", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_36)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_36())

def pokemon_quiz_36():
    if a_36.get() == "Pidgeot":
        AI.answer_image_36()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_37)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_37())

    else:
        AI.answer_image_36()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Pidgeot", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_37)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_37())

def pokemon_quiz_37():
    if a_37.get() == "Pikachu":
        AI.answer_image_37()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_38)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_38())

    else:
        AI.answer_image_37()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Pikachu", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_38)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_38())

def pokemon_quiz_38():
    if a_38.get() == "Poliwrath":
        AI.answer_image_38()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_39)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_39())

    else:
        AI.answer_image_38()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Poliwrath", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_39)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_39())

def pokemon_quiz_39():
    if a_39.get() == "Psyduck":
        AI.answer_image_39()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_40)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_40())

    else:
        AI.answer_image_39()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Psyduck", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_40)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_40())

def pokemon_quiz_40():
    if a_40.get() == "Scyther":
        AI.answer_image_40()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_41)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_41())

    else:
        AI.answer_image_40()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Scyther", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_41)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_41())

def pokemon_quiz_41():
    if a_41.get() == "Snorlax":
        AI.answer_image_41()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_42)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_42())

    else:
        AI.answer_image_41()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Snorlax", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_42)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_42())

def pokemon_quiz_42():
    if a_42.get() == "Squirtle":
        AI.answer_image_42()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_43)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_43())

    else:
        AI.answer_image_42()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Squirtle", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_43)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_43())

def pokemon_quiz_43():
    if a_43.get() == "Staryu":
        AI.answer_image_43()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_44)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_44())

    else:
        AI.answer_image_43()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Staryu", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_44)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_44())

def pokemon_quiz_44():
    if a_44.get() == "Tangela":
        AI.answer_image_44()
        
        right_answer()
        
        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_45)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_45())

    else:
        AI.answer_image_44()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Tangela", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_45)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_45())

def pokemon_quiz_45():
    if a_45.get() == "Tauros":
        AI.answer_image_45()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_46)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_46())

    else:
        AI.answer_image_45()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Tauros", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_46)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_46())

def pokemon_quiz_46():
    if a_46.get() == "Venonat":
        AI.answer_image_46()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_47)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_47())

    else:
        AI.answer_image_46()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Venonat", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_47)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_47())

def pokemon_quiz_47():
    if a_47.get() == "Zubat":
        AI.answer_image_47()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_48)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_48())

    else:
        AI.answer_image_47()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Zubat", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_48)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_48())

def pokemon_quiz_48():
    if a_48.get() == "Chansey":
        AI.answer_image_48()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_49)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_49())

    else:
        AI.answer_image_48()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Chansey", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_49)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_49())

def pokemon_quiz_49():
    if a_49.get() == "Gyarados":
        AI.answer_image_49()
        
        right_answer()

        increment()

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_50)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_50())

    else:
        AI.answer_image_49()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Gyarados", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        but_2 = Button(quiz, text = "NEXT", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = QI.question_image_50)
        but_2.place(x = 920, y = 550)
        quiz.bind("<Return>", lambda event:QI.question_image_50())

def pokemon_quiz_50():
    if a_50.get() == "Magnemite":
        AI.answer_image_50()
        
        right_answer()
        
        increment()

        ##Button for viewing score

        but_2 = Button(quiz, text = "VIEW SCORE", bg = "Orange", fg = "Black", font = ("OCR A Extended", 20), width = 10, height = 2, command = view_score)
        but_2.place(x = 920, y = 550)

    else:
        AI.answer_image_50()

        lbl_2 = Label(quiz, text = "", bg = "Yellow")
        lbl_2.place(x = 750, y = 500)
        lbl_2.configure(text = "The answer is Wrong: " "Magnemite", font = ("OCR A Extended", 20, "bold"), width = 35)
        lbl_2.configure(bg = "Red")

        ##Button for viewing score

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

##Import Libraries

from tkinter import *
from PIL import ImageTk, Image
import customtkinter

##New Window

optionc = Tk()
optionc.title("SELECT")
optionc.config(bg = "Royal Blue")
optionc.geometry("1024x640")

##Icon

optionc.wm_iconbitmap(r"C:\Users\joseph jenis\AppData\Local\Programs\Python\Python310\Proj\projimg02.ico")

##Background Image

bg_img_1 = Image.open("./projimg23.png")
resized = bg_img_1.resize((1532,790))
bg_img_2 = ImageTk.PhotoImage(resized)
lbl1 = Label(optionc, text = "", image = bg_img_2).place(x = 0, y = 0)

img_00 = PhotoImage(file = "./SELECT-YOUR-GAME-.png")
Label(optionc, text = "", image = img_00).pack()

##Functions

def game_01():
    optionc.destroy()
    import PROJECT_WHOS_THAT_POKEMON

def game_02():
    optionc.destroy()
    import PROJECT_WHOS_THAT_POKEMON_MCQ

def game_03():
    optionc.destroy()
    import PROJECT_GUESS_THEIR_TYPE

def quit_game():
    optionc.destroy()

##Function for Instruction

def instruct_01():
    instruct_lbl_01 = Label(optionc, text = "1) Each question in \n the quiz is \n of multiple-choice. \n \n 2) Guess the Pokemon \n and type it in \n the entry box  \n given \n next to the image. \n \n 3) The score will be \n displayed at the \n end of the game.", bg = "White", fg = "Black", font = ("OCR A Extended", 15))
    instruct_lbl_01.place(x = 890, y = 350)

def instruct_02():
    instruct_lbl_02 = Label(optionc, text = "1) Each question in \n the quiz is \n of multiple-choice. \n \n 2) Guess the Pokemon \n and click on the \n button next to \n your response that \n you think is right. \n \n 3) The score will be \n displayed at the \n end of the game.", bg = "White", fg = "Black", font = ("OCR A Extended", 15))
    instruct_lbl_02.place(x = 890, y = 350)

def instruct_03():
    instruct_lbl_03 = Label(optionc, text = "1) Each question in \n the quiz is \n of multiple-choice. \n \n 2) Guess the Pokemon \n Type and click on the \n button next to \n your response that \n you think is right. \n \n 3) The score will be \n displayed at the \n end of the game.", bg = "White", fg = "Black", font = ("OCR A Extended", 15))
    instruct_lbl_03.place(x = 890, y = 350)

##Button

but_01  = Button(optionc, text = "WHO'S THAT POKEMON?", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 20, height = 2, command = game_01)
but_01.place(x = 200, y = 300)

but_02  = Button(optionc, text = "WHO'S THAT POKEMON? (MCQ)", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 30, height = 2, command = game_02)
but_02.place(x = 200, y = 450)

but_03  = Button(optionc, text = "GUESS THEIR TYPES", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 20, height = 2, command = game_03)
but_03.place(x = 200, y = 600)

##Buttons for Instructions

but_001  = Button(optionc, text = "INSTRUCTIONS", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 15), width = 15, height = 1, command = instruct_01)
but_001.place(x = 535, y = 340)

but_002  = Button(optionc, text = "INSTRUCTIONS", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 15), width = 15, height = 1, command = instruct_02)
but_002.place(x = 695, y = 490)

but_003  = Button(optionc, text = "INSTRUCTIONS", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 15), width = 15, height = 1, command = instruct_03)
but_003.place(x = 535, y = 640)

##Quit Game Button

quit_but = Button(optionc, text = "QUIT", bg = "#484159", fg = "Black", bd = 0, cursor = "hand2", font = ("OCR A Extended", 20), width = 5, height = 1, command = quit_game)
quit_but.place(x = 1440, y = 735)

optionc.mainloop()
